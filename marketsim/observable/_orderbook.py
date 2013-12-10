from marketsim import (meta, types, context, Side, event,  
                       mathutils, getLabel, registry, ops, defs, _, orderbook)

from _computed import IndicatorBase
    
import _wrap 
from marketsim.types import *

class price_at_volume(ops.Function[float]):

    def __init__(self, orderbook = None, side = Side.Sell, volumeAt = 100):
        self.orderbook = orderbook if orderbook else marketsim.orderbook.Proxy()
        self.side = side
        self.volumeAt = volumeAt
            
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        for (volume, price) in queue.getVolumePrices([self.volumeAt]):
            return price
        return None
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "PriceAtVolume_{"+str(self.volumeAt)+"}("+self.orderbook.queue(self.side).label+")" 
    
    _properties = { 'orderbook' : types.IOrderBook, 
                    'side'      : types.Side, 
                    'volumeAt'  : float }

registry.expose(alias = ["Asset's", "Ask", "Price at volume"], args = (None, Side.Sell))(price_at_volume)
registry.expose(alias = ["Asset's", "Bid", "Price at volume"], args = (None, Side.Buy))(price_at_volume)

class volume_levels(ops.Function[types.IVolumeLevels]): 
    
    def __init__(self, 
                 orderbook = None, 
                 side = Side.Sell, 
                 volumeDelta = 30, 
                 volumeCount = 10):
        
        self.orderbook = orderbook if orderbook else marketsim.orderbook.Proxy()
        self.side = side
        self.volumeDelta = volumeDelta
        self.volumeCount = volumeCount
    
    @property    
    def volumes(self):
        return [self.volumeDelta * i for i in range(self.volumeCount)]
        
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        return [price for (volume, price) in queue.getVolumePrices(self.volumes)]
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "VolumeLevels("+self.orderbook.queue(self.side).label+")" 
    
    _properties = { 'orderbook'     : types.IOrderBook, 
                    'side'          : types.Side, 
                    'volumeDelta'   : float,
                    'volumeCount'   : int  }

registry.expose(alias = ["Asset's", "Ask", "Volume levels"], args = (None, Side.Sell))(volume_levels)
registry.expose(alias = ["Asset's", "Bid", "Volume levels"], args = (None, Side.Buy))(volume_levels)

import _computed

class Proxy(_computed.Proxy):
    
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self._alias = ["Asset's", self.__class__.__name__ ]

    _properties = { 'orderbook' : types.IOrderBook }
 
@registry.expose(alias = ["Asset's", "Tick size"])   
class TickSize(types.IFunction[float]):
    
    def __init__(self, orderbook = None):
        self.orderbook = orderbook if orderbook else marketsim.orderbook.Proxy()

    _properties = { 'orderbook' : types.IOrderBook }
    
    def __call__(self):
        return self.orderbook.tickSize
    
    

class QueueProxy(_computed.Proxy):
    
    def __init__(self, orderqueue):
        self.orderqueue = orderqueue
        self._alias = ["Queue's", self.__class__.__name__ ]

    _properties = { 'orderqueue' : types.IOrderQueue }
    
from marketsim.gen._out.observable.orderbook._BestPrice import BestPrice as QueuePrice

class QueueLastPrice(ops.Observable[float]):
    
    def __init__(self, orderqueue):
        ops.Observable[float].__init__(self)
        self._price = QueuePrice(orderqueue)
        event.subscribe(self._price, _(self)._update, self)
        self._lastPrice = None
        
    def __call__(self):
        return self._lastPrice
    
    def _update(self, src):
        p = self._price()
        if p is not None:
            self._lastPrice = p
            self.fire(self)
        
    
class QueueLastTrade(QueueProxy):
    
    @property
    def _impl(self):
        return self.orderqueue.lastTrade
    
class QueueLastTradePrice(QueueLastTrade):
    
    def __call__(self):
        trade = QueueLastTrade.__call__(self)
        return trade[0] if trade is not None else None

    @property
    def label(self):
        return 'LastTradePrice_{' + self.orderqueue.label + '}'
    
class QueueLastTradeVolume(QueueLastTrade):
    
    def __call__(self):
        return QueueLastTrade.__call__(self)[1]

    @property
    def label(self):
        return 'LastTradeVolume_{' + self.orderqueue.label + '}'
    
from _ewma import EWMA

class QueueWeightedPrice(ops.Function[float]):
    
    def getDefinitions(self):
        return {
            "volume"      : QueueLastTradeVolume(_.orderqueue) , 
            'orderqueue'  : self.orderqueue
        }
        
    def getImpl(self):
        price  = QueueLastTradePrice(_.orderqueue)
        return EWMA(price * _.volume, self.alpha) / EWMA(_.volume, self.alpha)
    
    @property
    def label(self):
        return 'WeightedPrice_{%g}(%s)' % (self.alpha, self.orderqueue.label)
    
_wrap.function(QueueWeightedPrice, ["OrderQueue's", "Trade weighted price"], 
               """ Moving average of trade prices weighted by volumes of an order queue
               """, 
               [
                    ('orderqueue', 'orderbook.Asks(orderbook.Proxy())', 'types.IOrderQueue'), 
                    ('alpha'     , 0.15,                                'positive')
               ], globals())
   
 
@registry.expose(alias = ["Asset's", "Ask", "Weighted trade price"], args = (None, 0.15))
def AskWeightedPrice(book = None, alpha = 0.15):
    return QueueWeightedPrice(orderbook.Asks(book), alpha)
    
@registry.expose(alias = ["Asset's", "Bid", "Weighted trade price"], args = (None, 0.15))
def BidWeightedPrice(book, alpha):
    return QueueWeightedPrice(orderbook.Bids(book), alpha)
    
@registry.expose(alias = ["Asset's", "Ask", "Last trade price"], args = (None,))
def AskLastTradePrice(book):
    return QueueLastTradePrice(orderbook.Asks(book))
    
@registry.expose(alias = ["Asset's", "Bid", "Last trade price"], args = (None,))
def BidLastTradePrice(book):
    return QueueLastTradePrice(orderbook.Bids(book))

@registry.expose(alias = ["Asset's", "Ask", "Last price"], args = (None,))
def AskLastPrice(book):
    return QueueLastPrice(orderbook.Asks(book))

@registry.expose(alias = ["Asset's", "Bid", "Last price"], args = (None,))
def BidLastPrice(book):
    return QueueLastPrice(orderbook.Bids(book))
    
@registry.expose(alias = ["Asset's", "Ask", "Price"], args = (None,))
def AskPrice(book):
    return QueuePrice(orderbook.Asks(book))

@registry.expose(alias = ["Asset's", "Bid", "Price"], args = (None,))
def BidPrice(book):
    return QueuePrice(orderbook.Bids(book))

class MidPrice(ops.Observable[float]):
    
    def getDefinitions(self):
        return {
            'book' : self.orderBook
        }
        
    def getImpl(self):
        return (AskPrice(_.book) + BidPrice(_.book)) / 2

    def __repr__(self):
        return self.label

    @property
    def label(self):
        return "MidPrice(%s)" % self.orderBook.label

_wrap.observable(MidPrice, ["Asset's", "MidPrice"], 
               """ Arithmetic mean of ask and bid price of an asset
               """, 
               [
                    ('orderBook', 'orderbook.Proxy()', 'types.IOrderBook')
               ], globals())        

class Spread(ops.Observable[float]):
    
    def getDefinitions(self):
        return {
            'book' : self.orderBook
        }
        
    def getImpl(self):
        return AskPrice(_.book) - BidPrice(_.book)
    
    @property
    def label(self):
        return "Spread(%s)" % self.orderBook.label

_wrap.observable(Spread, ["Asset's", "Spread"], 
               """ Difference between ask and bid asset's price
               """, 
               [
                    ('orderBook', 'orderbook.Proxy()', 'types.IOrderBook')
               ], globals())        

class LastTrade(Proxy):
    
    @property
    def _impl(self):
        return self.orderbook.lastTrade
    
    @property
    def attributes(self):
        return { 'transparency' : 80 }
    
class LastTradePrice(LastTrade): 
    # TODO: we'll need to say to typechecker that 
    # it is Observable[Price] but not Observable[PriceVolume]
    
    def __call__(self):
        trade = LastTrade.__call__(self)
        return trade[0] if trade is not None else None
    
    @property
    def label(self):
        return 'LastTradePrice_{' + self.orderbook.label + '}'
        

### -------------------------------------------------------------------   Observables
        
def PriceAtVolume(interval, orderbook, side, volume):

    return IndicatorBase(event.Every(ops.constant(interval)),
                         price_at_volume(orderbook, side, volume), 
                         {'smooth':True, 'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})

def VolumeLevels(interval, orderbook, side, volumeDelta, volumeCount):

    return IndicatorBase(event.Every(ops.constant(interval)),
                         volume_levels(orderbook, side, volumeDelta, volumeCount), 
                         {'smooth':True, 'volumeLevels' : True, 
                          'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})
