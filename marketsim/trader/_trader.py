from marketsim import event, _, Side, types, meta, timeserie, context, ops

from marketsim import asset, exchange

from _sa import SingleAsset
from _base import Base

class Trader(SingleAsset):
    def __init__(self, exchange, strategy=None):

        self.book = exchange.books()[0]  # take first book for now
        SingleAsset.__init__(self, self.book, strategy)
        self.exchange = exchange
        self.set_strategy(self._strategy)  # hack

        self.main_account = asset.CashBase("cash")  # default cash account to charge
        self.portfolio = asset.portfolio.PortfolioBase()

        for stock in exchange.assets():
            self.portfolio[stock] = 1
        self.portfolio[self.main_account] = 0

        print self.portfolio

    @property
    def PnL(self):
        return self.portfolio[self.main_account]

    @PnL.setter
    def PnL(self, value):
        self.portfolio[self.main_account] = value

    @property
    def amount(self):
        """ Number of assets traded:
        positive if trader has bought more assets than sold them
        negative otherwise
        """
        # TODO: remove since positions/amounts are managed by the portfolio class
        return -1
        #return self.portfolio[self.asset]

    @amount.setter
    def amount(self, value):
        # TODO: remove since positions/amounts are managed by the portfolio class
        pass
        #self.portfolio[self.asset] = value

    def onOrderMatched(self, order, price, volume):
        """ Called when a trader's 'order' is traded against 'other' order
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade
        """
        print "matched", order.asset, price, volume
        dVolume = volume if order.side == Side.Buy else -volume
        self.portfolio[order.asset] += dVolume
        # print self.portfolio
        super(Trader, self).onOrderMatched(order, price, volume)

    def set_strategy(self, s):
        if s is not None:
            s.parent = self
        self._strategy = s

    def get_strategy(self):
        return self._strategy

    @property
    def orderBooks(self):
        # TODO: convert to assets
        return [self.book]

    def send(self, order, asset=None):
        if not hasattr(order, 'asset'):
            order.asset = self.asset  # for compatibility with previous implementation
        # print "sending", order, "to", self.exchange[order.asset]

        Base.send(self, self.exchange[order.asset], order)

    def review_trade(self, trade, sender, callback):
        # TODO: Trader should derive from Reviewer class and its review_trade method
        print "reviewing trade", trade, "from", sender
        callback(True)

    strategy = property(get_strategy, set_strategy)