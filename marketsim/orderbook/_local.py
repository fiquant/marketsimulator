from _queue import Queue
from _base import BookBase
from marketsim import Side, registry

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

class Local(BookBase):
    """ Order book for a single asset in a market.
    Maintains two order queues for orders of different sides
    """
    def __init__(self, tickSize=1, label="",
                 marketOrderFee = None, # optional function (order, book)-> price to calculate fee for a market order
                 limitOrderFee = None,
                 cancelOrderFee = None):
        """ Initializes empty order book with given tick size
        """
        BookBase.__init__(self, 
                          Bids(tickSize, self), 
                          Asks(tickSize, self), 
                          label)
        
        self._tickSize = tickSize
        self._marketOrderFee = marketOrderFee
        self._limitOrderFee = limitOrderFee
        self._cancelOrderFee = cancelOrderFee

    _properties = {'tickSize' : float}

    @property
    def tickSize(self):
        """ Returns the tick side
        """
        return self._tickSize
    
    @tickSize.setter
    def tickSize(self, value):
        self._tickSize = value

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

    def processLimitOrder(self, order):
        """ Processes 'order' as limit order:
        If it is not matched completely, it stays at the order queue
        """
        if self._limitOrderFee:
            order.charge(self._limitOrderFee(order, self))
            
        if not self._queues[order.side.opposite.id].matchWith(order):
            self._queues[order.side.id].push(order)

    def processMarketOrder(self, order):
        """ Processes 'order' as market order:
        Iff it is not matched completely, returns False
        """
        if self._marketOrderFee:
            order.charge(self._marketOrderFee(order, self))
            
        return self._queues[order.side.opposite.id].matchWith(order)
