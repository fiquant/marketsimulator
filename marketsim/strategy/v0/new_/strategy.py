from marketsim import event, ops
from marketsim.observable import LastTradePrice, BufferedSeries, PortfolioValue, OnEveryDt, IndicatorBase

class StrategyBase(object):
    def __init__(self, label="Base"):
        self._running = True
        self._label = label
        self.on_order_created = event.Event()

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


import marketsim
import pandas as pd
import matplotlib.pyplot as plt
class OrderbookStrategy(StrategyBase):
    # TODO: Should a strategy have its own portfolio?
    def __init__(self):
        StrategyBase.__init__(self)

    def _subscribe(self):
        """ We finalize events that depend on bind
        """
        super(OrderbookStrategy, self)._subscribe()
        self._event = event.Every(ops.constant(20.0))
        event.subscribe(self._event, self.handle_data, self)

        book_A = self.parent.exchange.values()[0]
        self.series_A = BufferedSeries(LastTradePrice(book_A))

        book_B = self.parent.exchange.values()[1]
        self.series_B = BufferedSeries(LastTradePrice(book_B))

        portfolio_value = PortfolioValue(self.trader)
        # value = IndicatorBase(self.parent.on_order_matched, portfolio_value)
        value = OnEveryDt(1, portfolio_value)
        self.value_series = BufferedSeries(value)



    def handle_data(self, caller):
        # TODO: unsubscribe from all events except the trade review
        if self.running:
            #d = {'A': self.series_A(), 'B': self.series_B()}
            #frame = pd.DataFrame(d)
            # frame.fillna(inplace=True, method='ffill')
            #frame = frame.resample('1S', fill_method='ffill')
            #frame.plot()
            #plt.subplot(211)
            self.series_A().plot(title="Asset A", linestyle="steps")
            self.series_B().plot(title="Asset B", linestyle="steps")
            #plt.subplot()
            plt.show()


    def set_book(self, book):
        self._book = book

    def get_book(self):
        return self._book

    book = property(get_book, set_book)

    _internals = ['value_series', 'series_A', 'series_B']
