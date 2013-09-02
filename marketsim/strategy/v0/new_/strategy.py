from marketsim import event, ops
from marketsim.observable import LastTradePrice, BufferedSeries, PortfolioValue, OnEveryDt, IndicatorBase

import matplotlib.pyplot as plt

from marketsim.order import Market, Side

class StrategyBase(object):
    def __init__(self, label="Base"):
        self._running = True
        self._label = label
        self.on_order_created = event.Event()
        self.data = {}

    def store(self, observed, label=None, freq=None):
        if freq:
            observed = OnEveryDt(freq, observed)
        label = observed.label if label is None else label
        setattr(self, label, BufferedSeries(observed))
        self._internals.append(label)

    def bind(self, context):
        # this is actually not necessary in this implementation
        print "binding strategy"
        self._trader = context.trader
        self._scheduler = context.world

    def set_state(self, state):
        self._running = state

    def get_state(self):
        return self._running

    running = property(get_state, set_state)

    def send(self, trade, executor=None):
        """ sends the trade for review and waits for review before continuing
        """
        # TODO: add a way to notify the executor that the trade can be modified
        #       within certain limits

        assert self.running
        executor = self.parent if executor is None else executor
        self.running = False
        executor.review_trade(trade, sender=self, callback=self.trade_review)

    def trade_review(self, review):
        # for the moment review is only a boolean which is true if
        # the trade sent for review was accepted
        # TODO: Allow for reviews to go through a chain of reviewers
        # print "received trade review", review
        self.running = True
        print self.running

    @property
    def trader(self):
        return self._parent

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent
        self._subscribe()

    def _subscribe(self):
        pass

    @property
    def orderBook(self):
        return self.trader.book

    parent = property(get_parent, set_parent)
    _internals = []

from marketsim.orderbook._queue import AskLevels, BidLevels
from marketsim.observable import OLS

from itertools import izip_longest

import statsmodels.api as sm
import numpy as np

class OrderbookStrategy(StrategyBase):
    # TODO: Should a strategy have its own portfolio?
    def __init__(self):
        StrategyBase.__init__(self)

    def _subscribe(self):
        """ We finalize events that depend on bind
        """
        print "subscribing"
        super(OrderbookStrategy, self)._subscribe()

        self._event = event.Every(ops.constant(1.0))
        event.subscribe(self._event, self.handle_data, self)

        book_A, book_B = self.parent.exchange.books()
        self.asset_A, self.asset_B = self.parent.exchange.assets()

        self.store(LastTradePrice(book_A), label="series_A", freq=1)
        self.store(LastTradePrice(book_B), label="series_B", freq=1)
        self.store(PortfolioValue(self.trader), label="portfolio_value", freq=1)

        self.ask_levels = AskLevels(book_A, depth=5)
        self.bid_levels = BidLevels(book_A, depth=5)
        self._internals.append('ask_levels')
        self._internals.append('bid_levels')

        # event.subscribe(book_A.asks.changed, self.qchange, self)

    def handle_data(self, caller):
        if self.running:
            print OLS(self.series_A(), window=20)

    def qchange(self, caller):
        #print "orderbook"

        # print self._scheduler.currentTime

        levels = izip_longest(self.bid_levels(), self.ask_levels(), fillvalue=(0, 0))

        print "orderbook"
        for bid, ask in levels:
            print "{0[0]:6.2f}{0[1]:6d}\t{1[0]:6.2f}{1[1]:6d}".format(bid, ask)



