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

import _computed

class Proxy(_computed.Proxy):
    
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self._alias = ["Asset's", self.__class__.__name__ ]

    _properties = { 'orderbook' : types.IOrderBook }

class QueueProxy(_computed.Proxy):
    
    def __init__(self, orderqueue):
        self.orderqueue = orderqueue
        self._alias = ["Queue's", self.__class__.__name__ ]

    _properties = { 'orderqueue' : types.IOrderQueue }
    
class QueuePrice(QueueProxy):
    
    @property
    def _impl(self):
        return self.orderqueue.bestPrice
    
class QueueLastTrade(QueueProxy):
    
    @property
    def _impl(self):
        return self.orderqueue.lastTrade
    
class QueueLastTradePrice(QueueLastTrade):
    
    def __call__(self):
        return QueueLastTrade.__call__(self)[0]

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

def QueueWeightedPrice(orderqueue, alpha):
    lastTradePrice  = QueueLastTradePrice(orderqueue)
    lastTradeVolume = QueueLastTradeVolume(orderqueue)
    pv = EWMA(lastTradePrice * lastTradeVolume, alpha)
    w = EWMA(lastTradeVolume, alpha)
    return pv / w
    
def AskWeightedPrice(book, alpha):
    return QueueWeightedPrice(orderbook.Asks(book), alpha)
    
def BidWeightedPrice(book, alpha):
    return QueueWeightedPrice(orderbook.Bids(book), alpha)
    
def AskLastTradePrice(book):
    return QueueLastTradePrice(orderbook.Asks(book))
    
def BidLastTradePrice(book):
    return QueueLastTradePrice(orderbook.Bids(book))
    
def AskPrice(book):
    return QueuePrice(orderbook.Asks(book))

def BidPrice(book):
    return QueuePrice(orderbook.Bids(book))

def MidPrice(book):
    return (AskPrice(book) + BidPrice(book)) / 2

class LastTrade(Proxy):
    
    @property
    def _impl(self):
        return self.orderbook.lastTrade
    
class LastTradePrice(LastTrade): 
    # TODO: we'll need to say to typechecker that 
    # it is Observable[Price] but not Observable[PriceVolume]
    
    def __call__(self):
        return LastTrade.__call__(self)[0]
    
    @property
    def label(self):
        return 'LastTradePrice_{' + self.orderbook.label + '}'
        

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
