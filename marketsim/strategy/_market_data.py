from marketsim import event, _, Side, order, types, mathutils, scheduler, ops
from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2

from datetime import datetime
from pandas.io.data import DataReader
import pickle
from marketsim.trader import TraderHistory, SingleProxy

class _MarketData_Impl(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = scheduler.Timer(ops.constant(1))
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        start = datetime.strptime(self.start, '%d/%m/%Y')
        end = datetime.strptime(self.end, '%d/%m/%Y')

        self.quotes = self.loadData(self.ticker, start, end)['Adj Close']
        self.log = TraderHistory(SingleProxy())

    _internals = ['log']

    def loadData(self, ticker, start, end):
        try:
            # TODO: check if the start/end dates are covered by the data
            path = "../strategy/"
            market_data = pickle.load(open(path+ticker+".p", "rb"))
        except IOError:
            print "Downloading " + ticker + " data"
            market_data = DataReader(ticker,  "yahoo", start, end)
        return market_data

    def cancelPrevious(self):
        for position in self.log.pending:
            self.trader.send(order.Cancel(position))

    def updatePosition(self, bid, ask):
        buyOrder = order.LimitFactory(Side.Buy)(bid, self.volume)
        sellOrder = order.LimitFactory(Side.Sell)(ask, self.volume)
        self.log(buyOrder)
        self.log(sellOrder)
        self._trader.send(buyOrder)
        self._trader.send(sellOrder)

    @property
    def time(self):
        return self._scheduler.currentTime

    def _wakeUp(self, dummy):
        self.cancelPrevious()
        quote = self.quotes[self.time]
        myBid = quote - 0.1
        myAsk = quote + 0.1
        self.updatePosition(myBid, myAsk)


exec  wrapper2("MarketData",
             """ A Strategy that allows to drive the asset price based on historical market data
             by creating large volume orders for the given price.

             Every time step of 1 in the simulation corresponds to a 1 day in the market data.

             At each time step the previous Limit Buy/Sell orders are cancelled and new ones
             are created based on the next price of the market data.

             |ticker|
                Ticker of the asset

             |start|
                Start date in DD/MM/YYYY format

             |end|
                End date in DD/MM/YYYY format

             |volume|
                Volume of Buy/Sell orders. Should be large compared to the volumes of other traders.
             """,
              [ ('ticker', '"^GSPC"',  'str'),
                ('start', '"1/1/2000"', 'str'),
                ('end', '"1/1/2008"', 'str'),
                  ('volume', '1000', 'Volume')], register=False)
