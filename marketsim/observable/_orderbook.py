from marketsim import (meta, types, context, Side, event,  
                       mathutils, getLabel, registry, ops, defs, _, orderbook)

from _computed import IndicatorBase
    
import _wrap 
from marketsim.types import *

import _computed

from marketsim.gen._out.observable.orderbook._TickSize import TickSize

from marketsim.gen._out.observable.orderbook._BestPrice import BestPrice as QueuePrice
from marketsim.gen._out.observable.orderbook._LastPrice import LastPrice as QueueLastPrice


from marketsim.gen._intrinsic.orderbook.last_trade import LastTrade as QueueLastTrade
from marketsim.gen._out.observable.orderbook._LastTradePrice import LastTradePrice as QueueLastTradePrice
from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume as QueueLastTradeVolume

from _ewma import EWMA

from marketsim.gen._out.observable.orderbook._WeightedPrice import WeightedPrice as QueueWeightedPrice
from marketsim.gen._out.observable.orderbook.ask._WeightedPrice import WeightedPrice as AskWeightedPrice
from marketsim.gen._out.observable.orderbook.bid._WeightedPrice import WeightedPrice as BidWeightedPrice

from marketsim.gen._out.observable.orderbook.ask._LastTradePrice import LastTradePrice as AskLastTradePrice
from marketsim.gen._out.observable.orderbook.bid._LastTradePrice import LastTradePrice as BidLastTradePrice

from marketsim.gen._out.observable.orderbook.ask._LastPrice import LastPrice as AskLastPrice
from marketsim.gen._out.observable.orderbook.bid._LastPrice import LastPrice as BidLastPrice

from marketsim.gen._out.observable.orderbook.ask._Price import Price as AskPrice
from marketsim.gen._out.observable.orderbook.bid._Price import Price as BidPrice

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
