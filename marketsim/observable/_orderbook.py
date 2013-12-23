from marketsim import (meta, types, context, Side, event,  
                       mathutils, getLabel, registry, ops, defs, _, orderbook)

from _computed import IndicatorBase
    
import _wrap 
from marketsim.types import *

import _computed

class Proxy(_computed.Proxy):
    
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self._alias = ["Asset's", self.__class__.__name__ ]

    _properties = { 'orderbook' : types.IOrderBook }

from marketsim.gen._out.observable.orderbook._TickSize import TickSize

class QueueProxy(_computed.Proxy):
    
    def __init__(self, orderqueue):
        self.orderqueue = orderqueue
        self._alias = ["Queue's", self.__class__.__name__ ]

    _properties = { 'orderqueue' : types.IOrderQueue }
    
from marketsim.gen._out.observable.orderbook._BestPrice import BestPrice as QueuePrice
from marketsim.gen._out.observable.orderbook._LastPrice import LastPrice as QueueLastPrice


from marketsim.gen._intrinsic.orderbook.last_trade import LastTrade as QueueLastTrade
from marketsim.gen._out.observable.orderbook._LastTradePrice import LastTradePrice as QueueLastTradePrice
from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume as QueueLastTradeVolume

from _ewma import EWMA

from marketsim.gen._out.observable.orderbook._WeightedPrice import WeightedPrice as QueueWeightedPrice
from marketsim.gen._out.observable.orderbook._AskWeightedPrice import AskWeightedPrice
from marketsim.gen._out.observable.orderbook._BidWeightedPrice import BidWeightedPrice

@registry.expose(alias = ["Asset's", "Ask", "Last trade price"], args = (None,))
def AskLastTradePrice(book):
    return QueueLastTradePrice(orderbook.Asks(book))
    
@registry.expose(alias = ["Asset's", "Bid", "Last trade price"], args = (None,))
def BidLastTradePrice(book):
    return QueueLastTradePrice(orderbook.Bids(book))

from marketsim.gen._out.observable.orderbook._AskLastPrice import AskLastPrice
from marketsim.gen._out.observable.orderbook._BidLastPrice import BidLastPrice

from marketsim.gen._out.observable.orderbook._AskPrice import AskPrice
from marketsim.gen._out.observable.orderbook._BidPrice import BidPrice

from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
from marketsim.gen._out.observable.orderbook._Spread import Spread

from marketsim.gen._out.observable.orderbook._LastTradePrice import LastTradePrice
from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume

### -------------------------------------------------------------------   Observables

from marketsim.gen._out.observable.orderbook._VolumeLevels import VolumeLevels as volume_levels
from marketsim.gen._out.observable.orderbook._Queue import Queue
        
def VolumeLevels(interval, orderbook, side, volumeDelta, volumeCount):

    return IndicatorBase(event.Every(ops.constant(interval)),
                         volume_levels(Queue(orderbook, ops.constant(side)), volumeDelta, volumeCount),
                         {'smooth':True, 'volumeLevels' : True, 
                          'fillBelow' : side == Side.Buy, 'fillAbove' : side == Side.Sell})
