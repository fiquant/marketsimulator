from marketsim import (observable, combine, event, _, Side, order, types, mathutils, 
                       scheduler, ops, Event, registry, request)
from marketsim.types import *
from .._basic import Strategy
from _wrap import wrapper2

from marketsim.trader import TraderHistory, SingleProxy

import marketsim.historical.market as data

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
            self._trader.send(request.Cancel(position))

        quote = self.quotes[self._scheduler.currentTime]
        buyOrder = order.LimitFactory(Side.Buy)(quote - 5, self.volume)
        sellOrder = order.LimitFactory(Side.Sell)(quote + 5, self.volume)
        self._send(buyOrder)
        self._send(sellOrder)

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
