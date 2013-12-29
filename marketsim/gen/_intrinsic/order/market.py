from marketsim import Side
from _base import *

class Order_Impl(Default, HasSide, HasVolume, Cancellable):
    """ Market order of given *side* and *volume*
    """

    def __init__(self, side, volume, owner = None, volumeFilled = 0):
        """ Initializes order with volume to trade
        """
        HasSide.__init__(self, side)
        HasVolume.__init__(self, volume, volumeFilled)
        Cancellable.__init__(self)
        Default.__init__(self, owner)

    def With(self, side = None, volume = None):
        def opt(a,b):
            return a if b is None else b
        return Order_Impl(opt(self.side, side),
                           opt(self.volumeUnmatched, volume))

    def copyTo(self, dst):
        HasSide.copyTo(self, dst)
        HasVolume.copyTo(self, dst)
        Cancellable.copyTo(self, dst)

    def __str__(self):
        return "%s_%s%s" % (type(self).__name__, HasSide.__str__(self), HasVolume.__str__(self))

    def clone(self):
        return Order_Impl(self.side, self.volumeUnmatched, self.owner, self.volumeFilled)

    def processIn(self, orderBook):
        """ Order book calls this method to ask the order
        how it should be processed in the order book (a la Visitor)
        """
        orderBook.processMarketOrder(self)

    def canBeMatched(self, other):
        """ Returns True iff this order can be matched with 'other'
        """
        assert other.side == self.side.opposite
        return True

    @staticmethod
    def Buy(volume): return Order_Impl(Side.Buy, volume)

    @staticmethod
    def Sell(volume): return Order_Impl(Side.Sell, volume)
