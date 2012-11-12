from _queue import Queue
from _base import BookBase
from marketsim import Side

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
    """ Order book for a single asset in a market
    Maintains two order queues for orders of different sides
    """
    def __init__(self, tickSize=1, label=""):
        """ Initializes empty order book with given tick size
        """
        BookBase.__init__(self, 
                          Bids(tickSize, self), 
                          Asks(tickSize, self), 
                          tickSize, 
                          label)
