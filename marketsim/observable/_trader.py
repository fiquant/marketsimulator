from marketsim import meta, Event, types, event, getLabel, trader

from _computed import IndicatorBase

#### ------------------------------------------------------- Accessors

class rough_balance(object):
    """ Approximation for trader's cleared balance. :: 
    
        Rb(trader) = Balance(trader) + VolumeTraded(trader)*MidPrice(Asset(trader))
    
    (so, bigger the trader position worse the approximation).
    """
    
    def __init__(self, trader):
        self.trader = trader
        
    _types = [meta.function((), float)]
    
    def __call__(self):
        return self.trader.PnL + self.trader.amount*self.trader.book.price if self.trader.book.price else 0
   
    @property
    def digits(self):
        return self.trader.orderBook._digitsToShow
    
    @property
    def label(self):
        return "InstEfficiency_{" + getLabel(self.trader) + "}"
    
    _properties = { 'trader' : types.ISingleAssetTrader }

class profit_and_loss(object):
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
        return self.trader.orderBook._digitsToShow
    
    
    def __call__(self):
        return self.trader.PnL
    
    _properties = { 'trader' : types.ITrader }
    
class volume_traded(object):
    """ Returns trader's position (i.e. number of assets traded)
    """
    
    def __init__(self, trader):
        self.trader = trader
        self._alias = ["Trader's", "Position"]
        
    _types = [meta.function((), float)]
    
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
        event.subscribe(self.trader.on_traded, self.fire, self)
        
    _properties = { 'trader' : types.ISingleAssetTrader }
    

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
        aTrader = trader.SASM_Proxy()
        
    return IndicatorBase(\
        OnTraded(aTrader), 
        volume_traded(aTrader))
    
