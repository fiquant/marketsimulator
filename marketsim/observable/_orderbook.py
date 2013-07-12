from marketsim import (meta, Event, types, context, Side, event, scheduler, 
                       mathutils, getLabel, ops, _, orderbook)

from _computed import IndicatorBase

### ------------------------------------------------  data accessors

class mid_price(ops.Function[float]):
    """ Returns middle price in the given *orderbook*
    """
    
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self._alias = ["Asset's", "Mid-price"]
        
    def __call__(self):
        return self.orderbook.price

    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    @property
    def label(self):
        return "Price_{" + getLabel(self.orderbook) + "}"
    
    _properties = { 'orderbook' : types.IOrderBook }

class cross_spread(ops.Function[float]):
    
    def __init__(self, book_A, book_B):
        self.book_A = book_A
        self.book_B = book_B
        
    def __call__(self):
        asks = self.book_A.asks
        bids = self.book_B.bids
        return asks.best.price - bids.best.price if not asks.empty and not bids.empty else None
    
    @property
    def label(self):
        return "Price("+self.book_A.asks.label+") - Price("+self.book_B.bids.label+")"

class side_price(ops.Function[float]):
    """ Returns *orderbook* *side* price 
    """
    
    def __init__(self, orderbook, side):
        self.orderbook = orderbook
        self.side = side
    
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        return queue.best.price if not queue.empty else None
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    _properties = { 'orderbook' : types.IOrderBook  }
    
class last_side_price(ops.Function[float]):
    """ Returns *orderbook* last trade *side* price 
    """
    
    def __init__(self, orderbook, side):
        self.orderbook = orderbook
        self.side = side
        
    def __call__(self):
        queue = self.orderbook.queue(self.side)
        return queue.lastPrice
    
    @property
    def digits(self):
        return self.orderbook._digitsToShow
    
    _properties = { 'orderbook' : types.IOrderBook  }
    
class ask_price(side_price):
    
    def __init__(self, orderbook):
        side_price.__init__(self, orderbook, Side.Sell)
        self._alias = ["Asset's", "Ask price"]

    @property
    def label(self):
        return "Ask_{"+self.orderbook.label+"}" 
    
class bid_price(side_price):
    
    def __init__(self, orderbook):
        side_price.__init__(self, orderbook, Side.Buy)
        self._alias = ["Asset's", "Bid price"]

    @property
    def label(self):
        return "Bid_{"+self.orderbook.label+"}" 
    
class price_at_volume(ops.Function[float]):

    def __init__(self, orderbook, side, volumeAt):
        self.orderbook = orderbook
        self.side = side
        self.volumeAt = volumeAt
        self._alias = ["Asset's", "Price at Volume"]
    
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

class volume_levels(ops.Function[float]): # should be () -> meta.listOf(float)
    
    def __init__(self, orderbook, side, volumeDelta, volumeCount):
        self.orderbook = orderbook
        self.side = side
        self.volumeDelta = volumeDelta
        self.volumeCount = volumeCount
        self._alias = ["Asset's", "Volume levels"]
    
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

### -------------------------------------------------------------------   Events
    
class OnPriceChanged(Event):
    """ Event that is fired once mid-price in the *orderbook* has changed
    """
    
    def __init__(self, orderbook):
        Event.__init__(self)
        self.orderbook = orderbook
        
    def updateContext(self, _):
        pass
        
    def bind(self, ctx):
        event.subscribe(self.orderbook.on_price_changed, self.fire, self, ctx)
        
    _properties = { 'orderbook' : types.IOrderBook }

import _computed

class Proxy(_computed.Proxy):
    
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self._alias = ["Asset's", self.__class__.__name__ ]

    _properties = { 'orderbook' : types.IOrderBook }
    
class Price(Proxy):
    
    @property
    def _impl(self):
        return self.orderbook.midPrice

class QueueProxy(_computed.Proxy):
    
    def __init__(self, orderqueue):
        self.orderqueue = orderqueue
        self._alias = ["Queue's", self.__class__.__name__ ]

    _properties = { 'orderqueue' : types.IOrderQueue }
    
class QueuePrice(QueueProxy):
    
    @property
    def _impl(self):
        return self.orderqueue.bestPrice
    
def AskPrice(book):
    return QueuePrice(orderbook.Asks(book))

def BidPrice(book):
    return QueuePrice(orderbook.Bids(book))

class LastTrade(Proxy):
    
    @property
    def _impl(self):
        return self.orderbook.lastTrade
    
class LastTradePrice(types.Observable):
    
    def __init__(self, orderbook):
        types.Observable.__init__(self)
        self.orderbook = orderbook
        self._lastTrade = LastTrade(orderbook)
        event.subscribe(self._lastTrade, _(self).fire, self)
        
    def __call__(self):
        return self._lastTrade()[0]
    
    @property
    def label(self):
        return 'LastTradePrice_{' + self.orderbook.label + '}'
    
    @property
    def _digitsToShow(self):
        return self.orderbook._digitsToShow

    @property
    def attributes(self):
        return {}
        

### -------------------------------------------------------------------   Observables
        
def PriceAtVolume(interval, orderbook, side, volume):

    return IndicatorBase(scheduler.Timer(ops.constant(interval)),
                         price_at_volume(orderbook, side, volume), 
                         {'smooth':True, 'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})

def VolumeLevels(interval, orderbook, side, volumeDelta, volumeCount):

    return IndicatorBase(scheduler.Timer(ops.constant(interval)),
                         volume_levels(orderbook, side, volumeDelta, volumeCount), 
                         {'smooth':True, 'volumeLevels' : True, 
                          'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})
