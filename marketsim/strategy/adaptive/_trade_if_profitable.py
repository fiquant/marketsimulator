from marketsim import (trader, order, orderbook, scheduler, observable, order, 
                       request, registry, types, meta, _, ops, event)

from marketsim.types import *

from .._basic import Strategy
from .._wrap import wrapper2

from .. import v0
from ..side import FundamentalValue

class Mediator(Strategy):

    def updateContext(self, ctx):
        ctx.orderProcessor_1 = ctx.orderProcessor
        ctx.orderProcessor = self
        
    def bind(self, ctx):
        self._orderProcessor = ctx.orderProcessor_1
        

class _Estimator_Impl(Mediator):
    
    def __init__(self):
        Mediator.__init__(self)
        self._balance = 0
        self._position = 0
        
    @property
    def amount(self):
        return self._position
    
    @property
    def PnL(self):
        return self._balance
        
    def send(self, order):
        Strategy.send(self, 
                      request.EvalMarketOrder(
                                order.side, 
                                order.volumeUnmatched, 
                                _(self, 
                                  order.side, 
                                  order.volumeUnmatched)._update))
        Strategy.send(self, order)
        
        
    def _update(self, side, volume, (price, volumeUnmatched)):
        matched = volume - volumeUnmatched
        self._position += -matched if side == Side.Sell else matched
        self._balance += price if side == Side.Sell else -price

exec wrapper2("Estimator", 
             "",
             [('inner',   'FundamentalValue()', 'ISingleAssetStrategy')], register=False)

class Suspendable(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        self._suspended = False
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, flag = True):
        self._suspended = flag
        
    def send(self, order):
        if not self._suspended:
            Strategy.send(self, order)

class _tradeIfProfitable_Impl(Strategy):

    def _wakeUp(self, _):
        if not self.suspended:
            self._strategy.suspend(self._efficiency() < 0)

    def __init__(self):
        Strategy.__init__(self)
        self._estimator_strategy = self.estimator(self.strategy) # TODO: dependency tracking
        self._estimator = trader.SingleAsset(orderbook.OfTrader(trader.ParentProxy()),
                                             self._estimator_strategy)

        self._strategy = self.strategy
        self._efficiency = self.efficiency(self._estimator) # TODO: dependency tracking
        
        event.subscribe(self._efficiency, _(self)._wakeUp, self)

    @property
    def _children_to_visit(self):
        yield self._estimator
        yield self._strategy
        yield self._efficiency
        yield self._estimator_strategy
         
    def updateContext(self, context):
        context.parentTrader = context.trader
                
    def suspend(self, s=True):
        Strategy.suspend(self, s)
        self._strategy.suspend(s)
        self._estimator_strategy.suspend(s)

@registry.expose(alias=["trader's efficiency trend"])
@sig(args=(ISingleAssetTrader,), rv=ISingleAssetTrader)
def efficiencyTrend(trader):
    """ Returns derivative of a *trader*'s "cleared" balance
    """
    return observable.trend(observable.Efficiency(trader), alpha=0.065)

@registry.expose(alias=['Virtual market orders with unit volume'])
@sig(args=(ISingleAssetStrategy,), rv=ISingleAssetStrategy)
def virtualWithUnitVolume(strategy):
    """ Creates for a *strategy* a clone with same parameters but sending virtual market orders of unit volume
    """
    return strategy.With(volumeDistr=ops.constant(1), orderFactory=order.VirtualMarketFactory)    

exec wrapper2("tradeIfProfitable", 
             "",
             [('strategy',   'v0.FundamentalValue()', 'ISingleAssetStrategy'), 
              ('efficiency', 'efficiencyTrend',       'ISingleAssetTrader -> ISingleAssetTrader'),
              ('estimator',  'virtualWithUnitVolume', 'ISingleAssetStrategy -> ISingleAssetStrategy')], register=False)

        
@registry.expose(['Adaptive', 'TradeIfProfitable'])
class TradeIfProfitable(tradeIfProfitable):
    """ Strategy that estimates efficiency of original *strategy* 
    (normally as derivative of "cleared" balance for its clone sending unit volume orders)
    
    Parameters: 
    
        |strategy| 
            original strategy that can be suspended
            
        |efficiency| 
            function estimating is the strategy efficient or not
            
        |estimator| 
            function creating phantom strategy used for efficiency estimation
    """
    
    def __init__(self, strategy = v0.FundamentalValue(), 
                 efficiency=efficiencyTrend, 
                 estimator=virtualWithUnitVolume, 
                 **kwargs):
        tradeIfProfitable.__init__(self, strategy.With(**kwargs), efficiency, estimator)
        self._constructAs = 'marketsim.strategy.TradeIfProfitable'
    
    def With(self, 
             strategy = None, 
             efficiency = None,
             estimator = None,
             **kwargs):
        
        if strategy is None: strategy = self.strategy
        
        # TODO: we should also make _properties as union of all members _properties
        # during this union we should also check that there is no conflicts
        # With method should be implemented as walk over _properties
        # but there is no clear answer about what shall we do in case of chooseTheBest 
        # OR: we may consider these classes as decorators to exisiting strategies and believe
        # that parameters are passed to strategies not to 'efficiency' or 'estimator'
        # if someone wants to change 'efficiency' or 'estimator' parameters he should do it explicitly 
        return tradeIfProfitable.With(self, strategy.With(**kwargs), efficiency, estimator)
