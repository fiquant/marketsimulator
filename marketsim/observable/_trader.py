from marketsim import meta, Side, event, _, types, event, getLabel, mathutils, ops

from _computed import IndicatorBase
from marketsim.trader._proxy import SingleProxy

#### ------------------------------------------------------- Accessors

from marketsim.gen._out.observable.trader._RoughPnL import RoughPnL

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
    
InstEfficiency = RoughPnL
PnL = profit_and_loss

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