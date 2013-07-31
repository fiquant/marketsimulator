from marketsim import (trader, orderbook, event, _, Side, order, types, mathutils, 
                       scheduler, ops, Event, observable, registry, combine)

from marketsim.types import *

from _single_order import SingleOrder
from _array import Array
import _wrap

class MarketMaker(types.ISingleAssetStrategy):
    
    def getImpl(self):
        midPrice = observable.MidPrice(orderbook.OfTrader())
        volumeTraded = observable.VolumeTraded(trader.SingleProxy())
        
        return Array([
                SingleOrder(
                    order.Mutable(
                        combine.SidePriceVolume(
                            ops.constant(side),
                            observable.OnEveryDt(
                                0.9,
                                midPrice - sign - volumeTraded / self.volume
                            ),
                            ops.constant(self.volume))))\
                    for side, sign in {Side.Buy : -1, Side.Sell : 1}.iteritems()
            ])

_wrap.strategy(MarketMaker, ['Market maker'],
             """

             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('volume', '20.', 'Volume') ], globals())