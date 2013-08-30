from marketsim import event, _, Side, types, meta, timeserie, context, ops

from marketsim import asset, exchange

from _sa import SingleAsset

class Trader(SingleAsset):
    def __init__(self, exchange, strategy=None):

        self.asset, self.book = exchange.items()[0]  # take first book for now
        SingleAsset.__init__(self, self.book, strategy)
        self.exchange = exchange
        self.set_strategy(self._strategy)  # hack

        self._cash = asset.CashBase("cash")  # Main cash asset
        self.main_account = self._cash  # default cash account to charge
        self.portfolio = asset.portfolio.Portfolio()
        self.portfolio[self.asset] = 1
        self.portfolio[self._cash] = 0 # TODO: change to take into account more complex positions
        self.assetB = exchange.keys()[1]
        self.portfolio[self.assetB] = 1

        print self.portfolio

    @property
    def PnL(self):
        return self.portfolio[self.main_account]

    @PnL.setter
    def PnL(self, value):
        print self.portfolio
        self.portfolio[self.main_account] = value

    @property
    def amount(self):
        """ Number of assets traded:
        positive if trader has bought more assets than sold them
        negative otherwise
        """
        return self.portfolio[self.asset]

    @amount.setter
    def amount(self, value):
        self.portfolio[self.asset] = value

    def onOrderMatched(self, order, price, volume):
        """ Called when a trader's 'order' is traded against 'other' order
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade
        """
        dVolume = volume if order.side == Side.Buy else -volume
        self.portfolio[order.asset] += dVolume
        super(Trader, self).onOrderMatched(order, price, volume)

    def set_strategy(self, s):
        if s is not None:
            s.parent = self
        self._strategy = s

    def get_strategy(self):
        return self._strategy

    @property
    def orderBooks(self):
        print "called books"
        return [self.book]

    def send(self, order, _):
        # TODO: include asset in order so that the exchange knows which orderbook to process in
        print "sending", order
        order.asset = self.asset
        SingleAsset.send(self, order)

    def review_trade(self, trade, sender, callback):
        # TODO: Trader should derive from Reviewer class and its review_trade method
        print "reviewing trade", trade, "from", sender
        callback(True)

    strategy = property(get_strategy, set_strategy)