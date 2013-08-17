from marketsim import (trader, Event, order, orderbook, scheduler, observable, order, 
                       request, registry, types, meta, _, ops, event)

from marketsim.types import *

from .._basic import Strategy
from .._wrap import wrapper2

from .. import v0
from ..side import FundamentalValue

class Mediator(Strategy):

    def updateContext(self, ctx):
        self._orderProcessor_1 = ctx.orderProcessor
        ctx.orderProcessor = self
        
    def bind(self, ctx):
        self._orderProcessor = self._orderProcessor_1
        del self._orderProcessor_1
        
    @property
    def orderProcessor(self):
        return getattr(self, '_orderProcessor_1', 
                       getattr(self, '_orderProcessor', None))
        
    @property
    def orderBook(self):
        return self.orderProcessor.orderBook
    
    @property
    def orderBooks(self):
        return self.orderProcessor.orderBooks

        

class _Estimator_Impl(Mediator, types.IAccount):
    
    def __init__(self):
        Mediator.__init__(self)
        self._balance = 0
        self._position = 0
        self.on_traded = Event()
        
    @property
    def amount(self):
        return self._position
    
    @property
    def PnL(self):
        return self._balance
        
    def send(self, order):
        self._send(self, 
                      request.EvalMarketOrder(
                                order.side, 
                                order.volumeUnmatched, 
                                _(self, 
                                  order.side, 
                                  order.volumeUnmatched)._update))
        self._send(self, order)
        
        
    def _update(self, side, volume, (price, volumeUnmatched)):
        matched = volume - volumeUnmatched
        self._position += -matched if side == Side.Sell else matched
        self._balance += price if side == Side.Sell else -price
        self.on_traded.fire(self)

exec wrapper2("Estimator", 
             "",
             [
              ('inner',   'FundamentalValue()', 'ISingleAssetStrategy')
             ], register=False)

class _Suspendable_Impl(Mediator):
    
    def __init__(self):
        Mediator.__init__(self)
        
    @property
    def suspended(self):
        return not self.predicate()
    
    def send(self, order):
        if self.predicate():
            self._send(self, order)

exec wrapper2("Suspendable", 
             "",
             [
              ('inner',     'FundamentalValue()', 'ISingleAssetStrategy'),
              ('predicate', 'ops.constant(True)', 'IFunction[bool]')
             ], register=False)

class TradeIfProfitable(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        return {
            'estimator' : Estimator(self.inner)
        }
    
    def getImpl(self):
        efficiency = observable.trend(observable.Efficiency(_.estimator), alpha=0.065)
        return Suspendable(_.estimator, efficiency >= 0)
    
from .. import _wrap

_wrap.strategy(TradeIfProfitable, ['Adaptive', 'Trade-if-profitable'], 
             """ 
             """,
             [
              ('inner', 'FundamentalValue()', 'ISingleAssetStrategy'),
             ], 
             globals())

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
