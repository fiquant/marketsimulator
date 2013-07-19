from marketsim import event, _, Side, order, types, mathutils, scheduler, ops
from marketsim.types import *
from _basic import Strategy
from _wrap import wrapper2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class _MarketMaker_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        self._eventGen = scheduler.Timer(self.creationIntervalDistr)
        event.subscribe(self._eventGen, _(self)._wakeUp, self)

        def nans(shape, dtype=float):
            a = np.empty(shape, dtype)
            a.fill(np.nan)
            return a

        self.rng = range(1000)
        self.bids = pd.Series(nans(len(self.rng)), index=self.rng)
        self.asks = pd.Series(nans(len(self.rng)), index=self.rng)
        self.pnl = pd.Series(nans(len(self.rng)), index=self.rng)
        self.plotted = False

        import pickle
        quote = pickle.load(open("../marketsim/strategy/^GSPC.p", "rb"))
        self.quotes = quote['Adj Close']

        self.orders = {}

    def currentPrice(self, queue):
        return queue.best.price if not queue.empty else None

    def cancelUnmatched(self):
        for o, e in self.orders.iteritems():
            cancelOrder = order.Cancel(o)
            self._trader.send(cancelOrder)
        self.orders = {}

    def adjustPosition(self):
        # get current bids and asks
        bids = self._trader.book.bids
        asks = self._trader.book.asks

        time = int(np.floor(self._scheduler.currentTime))
        currentBid = self.quotes[time]
        currentAsk = self.quotes[time]



        self.bids[time] = currentBid if currentBid is not None else np.nan
        self.asks[time] = currentAsk if currentAsk is not None else np.nan
        # determine best position
        myBid = currentBid - 0.01
        myAsk = currentAsk + 0.01

        ordersToSend = []

        ordersToSend.append(self.orderFactory(Side.Buy)(myBid, 1000))
        ordersToSend.append(self.orderFactory(Side.Sell)(myAsk, 1000))

        # send orders and subscribe to their events
        for o in ordersToSend:
            self.orders[o] = event.subscribe(o.on_matched, self.onMatched, self, {})
            self._trader.send(o)

        # print self._trader.amount, currentBid, currentAsk

        self.pnl[time] = self._trader.PnL

        # if time > 990 and not self.plotted:
        #     plt.subplot('311')
        #     self.bids.plot()
        #     self.asks.plot()
        #     plt.subplot('312')
        #     bidaskspread = self.asks - self.bids
        #     bidaskspread.plot()
        #     meanbaspread = pd.rolling_mean(bidaskspread, 20)
        #     meanbaspread.plot()
        #
        #     plt.subplot('313')
        #     self.pnl.plot()
        #     self.plotted = True
        #     plt.show()


    def _wakeUp(self, dummy):
        self.cancelUnmatched()
        self.adjustPosition()

    def onMatched(self, matchedOrder, other, (price, volume)):
        # self._position -= matchedOrder.side.makePriceSigned(volume)
        pass

                        
exec  wrapper2("MarketMaker",
             """ Generic Market Maker strategy
                         
             """,
              [('orderFactory',         'order.LimitFactory',                  'Side -> Volume -> IOrder'),
               ('creationIntervalDistr', 'ops.constant(1)',        '() -> TimeInterval')],
               register=False)
