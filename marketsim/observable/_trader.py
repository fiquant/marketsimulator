from marketsim import meta, Side, Event, _, types, event, getLabel, mathutils, ops

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
    
    _properties = { 'trader' : types.ISingleAssetTrader }

class profit_and_loss(ops.Function[float]):
    """ Returns balance of the given *trader*
    """
    
    def __init__(self, trader):
        self.trader = trader
        self._alias = ["Trader's", "Balance"]
        
    @property
    def label(self):
        return "P&L_{" + getLabel(self.trader) + "}"
    
    @property
    def digits(self):
        return self.trader._digitsToShow
    
    
    def __call__(self):
        return self.trader.PnL
    
    _properties = { 'trader' : types.ITrader }
    
class volume_traded(ops.Function[float]):
    """ Returns trader's position (i.e. number of assets traded)
    """
    
    def __init__(self, trader):
        self.trader = trader
        self._alias = ["Trader's", "Position"]
    
    def __call__(self):
        return self.trader.amount
    
    @property
    def digits(self):
        return 0
    
    @property
    def label(self):
        return "Amount_{" + getLabel(self.trader) + "}"
    
    _properties = { 'trader' : types.ISingleAssetTrader }

#### ------------------------------------------------------- Events

class OnTraded(Event):
    """ Multicast event that is fired once a trade is done by *trader*
    """

    def __init__(self, trader):
        Event.__init__(self)
        self.trader = trader
        
    def bind(self, ctx):
        event.subscribe(self.trader.on_traded, self.fire, self, ctx)
        
    _properties = { 'trader' : types.ITrader }
    

#### ------------------------------------------------------- Observables
    
def InstEfficiency(trader):
    """ Creates an indicator bound to rough estimation of a trader's balance if cleared
    """
    
    return IndicatorBase(OnTraded(trader), rough_balance(trader))

def PnL(trader):
    
    return IndicatorBase(OnTraded(trader), profit_and_loss(trader))
    
def VolumeTraded(aTrader = None):
    """ Returns an indicator bound to trader's position 
    """
    if aTrader is None:
        aTrader = SingleProxy()
        
    return IndicatorBase(\
        OnTraded(aTrader), 
        volume_traded(aTrader))
    
class Base(object):

    def __init__(self, trader):
        self.trader = trader
        
    def bind(self, ctx):
        event.subscribe(self.trader.on_order_matched, _(self)._onOrderMatched, self, ctx)
        event.subscribe(self.trader.on_order_cancelled, _(self)._onOrderCancelled, self, ctx)
        
    _properties = { 'trader' : types.ITrader }
            
class PendingVolume_Impl(Base, ops.Observable[float]): # should be int
    
    def __init__(self, trader):
        Base.__init__(self, trader)
        ops.Observable[float].__init__(self)
        self._pendingVolume = 0
        
    @property
    def label(self):
        return "PendingVolume_{%s}" % self.trader.label
        
    def _onOrderSent(self, order):
        Base._onOrderSent(self, order)
        if 'volume' in dir(order):
            self._pendingVolume += order.volumeSigned
            self.fire(self)
        
    def _onOrderMatched(self, t, order, other, (price, volume)):
        self._pendingVolume -= order.volumeSigned
        self.fire(self)

    def _onOrderCancelled(self, t, order):
        self._pendingVolume -= order.volumeSigned
        self.fire(self)

    def __call__(self):
        return self._pendingVolume
    
import _computed

class Proxy(_computed.Proxy):
    
    def __init__(self, trader = None):
        if trader is None:
            trader = SingleProxy()
        self.trader = trader
        self._alias = ["Trader's", self.__class__.__name__ ]

    _properties = { 'trader' : types.ISingleAssetTrader }

    
class PendingVolume(Proxy):

    @property
    def _impl(self):
        if '_pendingVolume' not in dir(self.trader):
            self.trader._pendingVolume = PendingVolume_Impl(self.trader)
        return self.trader._pendingVolume
