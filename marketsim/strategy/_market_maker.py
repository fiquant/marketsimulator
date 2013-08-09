from marketsim import (trader, orderbook, event, _, Side, order, types, mathutils, 
                       scheduler, ops, Event, observable, registry, combine)

from marketsim.types import *

from _single_order import SingleOrder2
from _market_data import Async
from _array import Array
import _wrap

const = ops.constant

class MarketMaker(types.ISingleAssetStrategy):
    
    def getImpl(self):
        midPrice = observable.MidPrice(orderbook.OfTrader())
        volumeTraded = observable.VolumeTraded(trader.SingleProxy())

        return Array([
                SingleOrder2(
                    order.factory.Iceberg(
                        const(self.volume),
                        order.factory.FloatingPrice(
                            Async(observable.OnEveryDt(
                                    0.9,
                                    midPrice - sign - volumeTraded / self.volume
                            )),
                            order._limit.Price_Factory(
                                side = const(side),
                                volume = const(self.volume * 1000000)))))\
                    for side, sign in {Side.Buy : -1, Side.Sell : 1}.iteritems()
            ])

_wrap.strategy(MarketMaker, ['Market maker'],
             """

             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('volume', '20.', 'Volume') ], globals())