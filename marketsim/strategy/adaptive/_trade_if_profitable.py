from marketsim import (trader, Event, order, orderbook, scheduler, observable, order, 
                       request, registry, types, meta, _, ops, event)

from marketsim.types import *

from .._basic import Strategy
from .._wrap import wrapper2

from .. import v0
from ..side import FundamentalValue

from _virtual_market import VirtualMarket
from _suspendable import Suspendable

class _Account_Impl(Strategy, types.IAccount):
    
    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.inner.on_order_created, _(self).send, self)
        event.subscribe(observable.OnOrderMatched(), _(self)._onOrderMatched, self)
        self.on_traded = Event()
        self._balance = 0
        self._position = 0
        
    def _onOrderMatched(self, trader, order, price, volume):
        if getattr(order, '_strategy', None) == self.inner:
            pv = price * volume
            self._balance += pv if order.side == Side.Sell else -pv
            self._position += volume if order.side == Side.Buy else -volume
            self.on_traded.fire(self)
    
    @property
    def amount(self):
        return self._position
    
    @property
    def PnL(self):
        return self._balance
        
    
    def send(self, order, source):
        order._strategy = source
        self._send(order)

exec wrapper2("Account", 
             "",
             [
              ('inner',     'FundamentalValue()', 'ISingleAssetStrategy'),
             ], register=False)


def cachedattr(obj, name, setter):
    if not hasattr(obj, name):
        setattr(obj, name, setter())
        
    return getattr(obj, name)


@sig(args=(IAccount,), rv=IFunction[float])
def efficiency(trader):
    return cachedattr(trader, '_efficiency', 
                      lambda: observable.Efficiency(VirtualMarket(trader)))

@sig(args=(IAccount,), rv=IFunction[float])
def efficiencyTrend2(trader):
    return cachedattr(trader, '_efficiencytrend', 
                      lambda: observable.trend(efficiency(trader), alpha=0.065))

@sig(args=(ISingleAssetStrategy,), rv=IFunction[float])
def efficiencyTrend3(strategy):
    return cachedattr(strategy, '_efficiencytrend2', 
                      lambda: observable.trend(
                                    observable.Efficiency(
                                        VirtualMarket(strategy)),
                                    alpha=0.065))


class TradeIfProfitable(types.ISingleAssetStrategy):
    
    def getImpl(self):
        efficiency = self.evaluator(self.inner)
        return Suspendable(self.inner, efficiency >= 0)
    
from .. import _wrap

_wrap.strategy(TradeIfProfitable, ['Adaptive', 'Trade-if-profitable'], 
             """ 
             """,
             [
              ('inner', 'FundamentalValue()', 'ISingleAssetStrategy'),
              ('evaluator', 'efficiencyTrend3', 'ISingleAssetStrategy -> IFunction[float]')
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
