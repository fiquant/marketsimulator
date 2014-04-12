from _base import *
from marketsim.types import *

class Order_Impl(Default, HasSide, HasPrice, HasVolume, Cancellable):
    """ Limit order of the given *side*, *price* and *volume*
    """

    def __init__(self, side, price, volume, owner = None, volumeFilled = 0):
        """ Initializes order with price and volume
        price is a limit price on which order can be traded
        if there are no suitable orders, the limit order remains in the order book
        """
        self._ticks = None
        HasSide.__init__(self, side)
        HasVolume.__init__(self, volume, volumeFilled)
        Cancellable.__init__(self)
        Default.__init__(self, owner)
        HasPrice.__init__(self, price)

    @property
    def ticks(self):
        return self._ticks

    @ticks.setter
    def ticks(self, value):
        self._ticks = value
        
    def copyTo(self, dst):
        HasSide.copyTo(self, dst)
        HasVolume.copyTo(self, dst)
        Cancellable.copyTo(self, dst)
        HasPrice.copyTo(self, dst)
        
    def __str__(self):
        return "%s_%s%s@%s" % (type(self).__name__, 
                               HasSide.__str__(self), 
                               HasVolume.__str__(self), 
                               HasPrice.__str__(self))
        
    def With(self, side = None, price = None, volume = None):
        def opt(a,b):
            return a if b is None else b
        return Order_Impl(opt(self.side, side),
                          opt(self.price, price),
                          opt(self.volumeUnmatched, volume))
        
    def clone(self):
        return Order_Impl(self.side, self.price, self.volumeUnmatched, self.owner, self.volumeFilled)
        
    def processIn(self, orderBook):
        """ Order book calls this method to ask the order 
        how it should be processed in the order book (a la Visitor)
        """
        orderBook.processLimitOrder(self)

    def canBeMatched(self, other):
        """ Returns True iff this order can matched with 'other'
        """
        assert other.side == self.side.opposite
        return not self.side.better(other.price, self.price)

    def matchWith(self, other):
        """ Matches the order with another one provided that it can be matched
        returns (price, volume) of the trade done
        """
        # volume to trade
        v = min(self.volumeUnmatched, other.volumeUnmatched)
        # price to trade is my price
        # it means that incoming limit order is considered as a market order
        # and its price is not taken for the trade
        p = self.price
        pv = (p,v)
        # notify trade side about the it
        self.onMatchedWith(p,v)
        other.onMatchedWith(p,v)
        return pv

    @staticmethod
    def Buy(price, volume): return Order_Impl(Side.Buy, price, volume)
     
    @staticmethod
    def Sell(price, volume): return Order_Impl(Side.Sell, price, volume)
