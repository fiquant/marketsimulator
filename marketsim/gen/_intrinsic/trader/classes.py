from marketsim.gen._out._timeserie import TimeSerie
from marketsim import event, _, types, context
from marketsim.gen._out._side import Side

from marketsim.gen._out._intrinsic_base.trader.classes import SingleAsset_Base, MultiAsset_Base

class Holder_Impl(object):

    def __init__(self):
        if type(self.timeseries) is dict:
            self.timeseries = [TimeSerie(k,v) for k,v in self.timeseries.iteritems()]

    def addTimeSerie(self, source, graph):
        ts = TimeSerie(source, graph)
        self.timeseries.append(ts)

class Base_Impl(Holder_Impl):
    """ Base class for traders.
    Responsible for bookkeeping P&L of the trader and
    maintaining on_order_sent and on_traded events
    """

    def __init__(self):
        Holder_Impl.__init__(self)
        # event to be fired when an order has been sent
        from marketsim.gen._out.event._event import Event
        self.on_order_sent = Event()
        # event to be fired when an order issued by the trader has been matched
        self.on_order_matched = Event()
        # event to be fired when an order issued by the trader has been cancelled
        self.on_order_disposed = Event()
        # event to be fired when a trader's is traded; to be removed
        self.on_traded = Event()
        self.reset()

    def updateContext(self, context):
        context.trader = self
        context.orderProcessor = self

    def updateContext_ex(self, context):
        context.trader = self
        context.orderProcessor = self

    def reset(self):
        self.PnL = 0

    def _charge(self, price):
        self.PnL -= price

    def onOrderMatched(self, order, price, volume):
        """ Called when a trader's 'order' is traded against 'other' order
        at given 'price' and 'volume'
        Trader's P&L is updated and listeners are notified about the trade
        """
        pv = price * volume
        self.PnL += pv if order.side == Side.Sell else -pv

        self.on_order_matched.fire(self, order, price, volume)
        self.on_traded.fire(self)

    def onOrderDisposed(self, order):
        self.on_order_disposed.fire(self, order)

    def _makeSubscribedTo(self, order):
        """ Makes trader subscribed to 'order' on_matched event
        before sending it to the order book
        Returns the order itself
        """
        order.owner = self
        return order

    def send(self, book, order):
        """ Sends 'order' to 'book'
        After having the order sent notifies listeners about it
        """
        from marketsim.gen._out._iorder import IOrder
        order.bind_ex(self._ctx_ex)
        if hasattr(self, '_ctx'):
            context.bind(order, self._ctx)
        if isinstance(order, IOrder):
            order = self._makeSubscribedTo(order)
        book.process(order)
        if isinstance(order, IOrder):
            self.on_order_sent.fire(order)

class SingleAsset_Impl(Base_Impl, SingleAsset_Base):
    """ A trader that trades a single asset on a single market.

        Parameters:

        **orderBook**
            order book for the asset being traded

        **strategies**
            array of strategies run by the trader

        **amount**
            current position of the trader (number of assets that it owns)

        **PnL**
            current trader balance (number of money units that it owns)
    """

    def __init__(self):
        Base_Impl.__init__(self)
        self._alias = [self.label]

    def on_strategy_set(self, value):
        if hasattr(self, '_subscription'):
            self._subscription.switchTo(value.on_order_created)
        else:
            self._subscription = event.subscribe(self.strategy.on_order_created, _(self).send, self)

    def reset(self):
        self.amount = 0
        self.on_strategy_set(self.strategy)

    _internals = ['orderBook'] # hack in order to make it processed first

    def onOrderMatched(self, order, price, volume):
        """ Called when a trader's 'order' is traded against 'other' order
        at given 'price' and 'volume'
        Trader's amount and P&L is updated and listeners are notified about the trade
        """
        dVolume = volume if order.side == Side.Buy else -volume
        self.amount += dVolume
        Base_Impl.onOrderMatched(self, order, price, volume)


    @property
    def orderBooks(self):
        return [self.orderBook]

    @property
    def _digitsToShow(self):
        return self.orderBook._digitsToShow

    def send(self, order, unused = None):
        Base_Impl.send(self, self.orderBook, order)

class MultiAsset_Impl(Base_Impl, MultiAsset_Base):

    def __init__(self):
        Base_Impl.__init__(self)
        self._alias = [self.label]
        for t in self._traders:
            t.on_traded += self.on_traded.fire

    @property
    def traders(self):
        return self._traders

    @traders.setter
    def traders(self, newTraders):
        if hasattr(self, "_traders"):
            for t in self._traders:
                t.on_traded -= self.on_traded.fire
        self._traders = newTraders
        if hasattr(self, "on_traded"):
            for t in self._traders:
                t.on_traded += self.on_traded.fire

    def dispose(self):
        for t in self._traders:
            t.on_traded -= self.on_traded.fire

    @property
    def orderBooks(self):
        return [t.orderBook for t in self._traders]

    @property
    def _digitsToShow(self):
        return max([t._digitsToShow for t in self._traders])

    @property
    def PnL(self):
        return sum([t.PnL for t in self._traders])

    @PnL.setter
    def PnL(self, value):
        assert value == self.PnL, 'cannot change balance of a multi asset trader'