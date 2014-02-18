from queue import Queue
from base import BookBase
from marketsim.gen._out._side import Side

class Bids(Queue):
    """ Queue of limit orders buy
    """

    def __init__(self, *args):
        Queue.__init__(self, *args)

    @property
    def label(self):
        return self.book.label + "_{Bids}"

    side = Side.Buy


class Asks(Queue):
    """ Queue of limit orders buy
    """

    def __init__(self, *args):
        Queue.__init__(self, *args)

    @property
    def label(self):
        return self.book.label + "^{Asks}"

    side = Side.Sell

class _Local_Impl(BookBase):
    """ Order book for a single asset in a market.
    Maintains two order queues for orders of different sides
    """
    def __init__(self):
        """ Initializes empty order book with given tick size
        """
        BookBase.__init__(self,
                          Bids(self.tickSize, self),
                          Asks(self.tickSize, self))

        self._asks._digitsToShow = self._digitsToShow
        self._bids._digitsToShow = self._digitsToShow

        self._marketOrderFee = None #marketOrderFee
        self._limitOrderFee =  None #limitOrderFee
        self._cancelOrderFee =  None #cancelOrderFee

    def cancelOrder(self, order):
        """ To be called when 'order' is cancelled
        """
        if self._cancelOrderFee:
            order.charge(self._cancelOrderFee(order, self))

        self.queue(order.side).cancelOrder(order)

    def evaluateOrderPrice(self, side, volume):
        """ Evaluates price at which a market order of given 'side'
            and having given 'volume' would be executed
        """
        return self._queues[side.opposite.id].evaluateOrderPrice(volume)

    def evaluateOrderPriceAsync(self, side, volume, callback):
        callback(self.evaluateOrderPrice(side, volume))

    def evaluateVolumesForBudget(self, side, budget, callback):
        res = list(self._queues[side.opposite.id].pvsForFixedBudget(budget))
        callback(res)


    def processLimitOrder(self, order):
        """ Processes 'order' as limit order:
        If it is not matched completely, it stays at the order queue
        """
        assert order.owner is not None

        if self._limitOrderFee:
            order.charge(self._limitOrderFee(order, self))

        if not self._queues[order.side.opposite.id].matchWith(order):
            self._queues[order.side.id].push(order)

    def processMarketOrder(self, order):
        """ Processes 'order' as market order:
        Iff it is not matched completely, returns False
        """
        assert order.owner is not None

        if self._marketOrderFee:
            order.charge(self._marketOrderFee(order, self))

        return self._queues[order.side.opposite.id].matchWith(order)
