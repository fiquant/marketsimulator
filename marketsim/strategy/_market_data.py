from marketsim import (observable, combine, event, _, Side, order, types, mathutils, 
                       scheduler, ops, Event, registry)
from marketsim.types import *
from _single_order import SingleOrder2

from _array import Array
import _wrap

const = ops.constant

class BreaksAtChanges(ops.Observable[float]):
    
    def __init__(self, source):
        ops.Observable[float].__init__(self)
        self.source = source
        self._value = None
        event.subscribe(source, _(self)._clean, self)
        
    _properties = {
        'source' : types.IObservable[float]
    }
    
    def bind(self, ctx):
        self._scheduler = ctx.world
    
    def _clean(self, dummy):
        self._setup(None)
        self._scheduler.async(_(self, self.source())._setup)
        
    def _setup(self, x):
        self._value = x
        self.fire(self)
    
    def __call__(self):
        return self._value
    
    

class MarketData(types.ISingleAssetStrategy):
    
    def getImpl(self):
        quotes = observable.Quote(self.ticker, self.start, self.end) # TODO: should be in definitions
        return Array([
                SingleOrder2(
                    order.factory.Iceberg(
                        const(self.volume),
                        order.factory.FloatingPrice(
                            BreaksAtChanges(ops.constant(sign*self.delta) + quotes),
                            order._limit.Price_Factory(
                                side = const(side),
                                volume = const(self.volume * 1000000)))))\
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
