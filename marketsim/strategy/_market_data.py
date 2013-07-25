from marketsim import event, _, Side, order, types, mathutils, scheduler, ops, Event, registry
from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2

import marketsim.historical.market as data

from marketsim.trader import TraderHistory, SingleProxy
from marketsim.order import Cancel

class Quote(ops.Observable[float]):
    
    def __init__(self, ticker, start, end):
        ops.Observable[float].__init__(self)
        self.ticker = ticker
        self.start = start
        self.end = end
        self._quotes = data.load(self.ticker, self.start, self.end)['Adj Close']
        self._current = None
        event.subscribe(scheduler.Timer(ops.constant(1)), _(self)._wakeUp, self)
        
    _properties = {
        'ticker': str,
        'start' : str,
        'end'   : str,
    }
        
    def bind(self, ctx):
        self._scheduler = ctx.world

    def _wakeUp(self, dummy):
        self._current = self._quotes[self._scheduler.currentTime]
        self.fire(self)
        
    def __call__(self):
        return self._current

class Combine_SidePriceVolume(ops.Observable[types.SidePriceVolume]): 
    
    def __init__(self, side, price, volume):
        ops.Observable[types.SidePriceVolume].__init__(self)
        self.side = side 
        self.price = price 
        self.volume = volume
        if isinstance(side, Event):
            event.subscribe(side, _(self).fire, self)
        if isinstance(price, Event):
            event.subscribe(price, _(self).fire, self)
        if isinstance(volume, Event):
            event.subscribe(volume, _(self).fire, self)
            
    def __call__(self):
        side = self.side()
        if side is None:
            return None
        price = self.price()
        if price is None:
            return None
        volume = self.volume()
        if volume is None:
            return None
        
        return (side, price, volume)
                    
    _properties = {
        'side' : types.IFunction[Side],
        'price': types.IFunction[float],
        'volume':types.IFunction[float],
    }

class _SingleOrder_Impl(Strategy):

    def bind(self, ctx):
        self._scheduler.async(_(self)._wakeUp)

    def _wakeUp(self):
        self._trader.send(self.order)
        
exec wrapper2("SingleOrder", 
              """
              """, 
              [
                ('order', 'None', 'object')
              ], register = False)

from _array import Array
import _wrap

class MarketData2(types.ISingleAssetStrategy):
    
    def getImpl(self):
        quotes = Quote(self.ticker, self.start, self.end) # TODO: should be in definitions
        return Array([
                SingleOrder(
                    order.Mutable(
                        Combine_SidePriceVolume(
                            ops.constant(side), 
                            ops.constant(sign*self.delta) + quotes, 
                            ops.constant(self.volume))))\
                    for side, sign in {Side.Buy : -1, Side.Sell : 1}.iteritems()
            ])
            
_wrap.strategy(MarketData2, ['Market data'],
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
    

class _MarketData_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = scheduler.Timer(ops.constant(1))
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        self.quotes = data.load(self.ticker, self.start, self.end)['Adj Close']

        self.log = TraderHistory(SingleProxy())
        self.waitingForCancel = False

    _internals = ['log']

    def _wakeUp(self, dummy):
        for position in self.log.pending:
            self._trader.send(Cancel(position))

        quote = self.quotes[self._scheduler.currentTime]
        buyOrder = order.LimitFactory(Side.Buy)(quote - 5, self.volume)
        sellOrder = order.LimitFactory(Side.Sell)(quote + 5, self.volume)
        self._trader.send(buyOrder)
        self._trader.send(sellOrder)







exec  wrapper2("MarketData",
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

             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('ticker', '"^GSPC"',  'str'),
                ('start', '"2001-1-1"', 'str'),
                ('end', '"2010-1-1"', 'str'),
                  ('volume', '1000', 'Volume')], register=False)
