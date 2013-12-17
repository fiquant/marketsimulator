from marketsim import meta, Side, event, _, types, event, getLabel, mathutils, ops

from _computed import IndicatorBase
from marketsim.trader._proxy import SingleProxy

#### ------------------------------------------------------- Accessors

class rough_balance(ops.Function[float]):
    """ Approximation for trader's cleared balance. :: 
    
        Rb(trader) = Balance(trader) + VolumeTraded(trader)*MidPrice(Asset(trader))
    
    (so, bigger the trader position worse the approximation).
    """
    
    def __init__(self, trader):
        self.trader = trader
        
    def __call__(self):
        return self.trader.PnL + self.trader.amount*self.trader.book.price if self.trader.book.price else 0
   
    @property
    def digits(self):
        return self.trader.orderBook._digitsToShow
    
    @property
    def label(self):
        return "InstEfficiency_{" + getLabel(self.trader) + "}"
    
    _properties = { 'trader' : types.IAccount }

from marketsim.gen._out.observable.trader._Balance import Balance as profit_and_loss
from marketsim.gen._out.observable.trader._Position import Position as volume_traded

#### ------------------------------------------------------- Events

class OnTraded(event.Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader = None):
        event.Event.__init__(self)
        self.trader = trader if trader else SingleProxy()
        
    def bind(self, ctx):
        event.subscribe(self.trader.on_traded, self.fire, self, ctx)
        
    _properties = { 'trader' : types.ITrader }
    
class OnOrderMatched(event.Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader = None):
        event.Event.__init__(self)
        self.trader = trader if trader else SingleProxy()
        
    def bind(self, ctx):
        event.subscribe(self.trader.on_order_matched, self.fire, self, ctx)
        
    _properties = { 'trader' : types.ITrader }
    

#### ------------------------------------------------------- Observables
    
def InstEfficiency(trader):
    """ Creates an indicator bound to rough estimation of a trader's balance if cleared
    """
    
    return IndicatorBase(OnTraded(trader), rough_balance(trader))

def PnL(trader):
    
    return IndicatorBase(OnTraded(trader), profit_and_loss(trader))

VolumeTraded = volume_traded

class Base(object):

    def __init__(self, trader):
        self.trader = trader

    def bind(self, ctx):
        event.subscribe(self.trader.on_order_matched, _(self).onOrderMatched, self, ctx)
        event.subscribe(self.trader.on_order_disposed, _(self).onOrderDisposed, self, ctx)

    _properties = { 'trader' : types.IAccount }

import _computed

class Proxy(_computed.Proxy):

    def __init__(self, trader = None):
        if trader is None:
            trader = SingleProxy()
        self.trader = trader
        self._alias = ["Trader's", self.__class__.__name__ ]

    _properties = { 'trader' : types.IAccount }


from marketsim.gen._out.observable.trader._PendingVolume import PendingVolume