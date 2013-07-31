from marketsim import (observable, combine, event, _, Side, order, types, mathutils, 
                       scheduler, ops, Event, registry)
from marketsim.types import *
from _single_order import SingleOrder

from _array import Array
import _wrap

class MarketData(types.ISingleAssetStrategy):
    
    def getImpl(self):
        quotes = observable.Quote(self.ticker, self.start, self.end) # TODO: should be in definitions
        return Array([
                SingleOrder(
                    order.Mutable(
                        combine.SidePriceVolume(
                            ops.constant(side), 
                            ops.constant(sign*self.delta) + quotes, 
                            ops.constant(self.volume))))\
                    for side, sign in {Side.Buy : -1, Side.Sell : 1}.iteritems()
            ])
            
_wrap.strategy(MarketData, ['Market data'],
             """ A Strategy that allows to drive the asset price based on historical market data
             by creating large volume orders for the given price.
 
             Every time step of 1 in the simulation corresponds to a 1 day in the market data.
 
             At each time step the previous Limit Buy/Sell orders are cancelled and new ones
             are created based on the next price of the market data.
 
             |ticker|
                Ticker of the asset
 
             |start|
                Start date in DD-MM-YYYY format
 
             |end|
                End date in DD-MM-YYYY format
 
             |delta|
                Price difference between orders placed and underlying quotes
 
             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('ticker', '"^GSPC"',  'str'),
                ('start', '"2001-1-1"', 'str'),
                ('end', '"2010-1-1"', 'str'),
                ('delta', '1', 'positive'),
                  ('volume', '1000', 'Volume')], globals())
