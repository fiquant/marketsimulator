from marketsim import registry, meta, types, bind
from marketsim.types import *
from _base import Base

class Market(Base):
    """ Market order of given *side* and *volume*
    """

    def __init__(self, side, volume):
        """ Initializes order with volume to trade
        """
        Base.__init__(self, side, volume)
        
    def clone(self):
        return Market(self.side, self.volume)

    def processIn(self, orderBook):
        """ Order book calls this method to ask the order 
        how it should be processed in the order book (a la Visitor)
        """
        if not orderBook.processMarketOrder(self):
            self.cancel()

    def canBeMatched(self, other):
        """ Returns True iff this order can be matched with 'other'
        """
        if other.side != self.side.opposite:
            a = 12
        assert other.side == self.side.opposite
        return True
    
    @staticmethod
    def Buy(volume): return Market(Side.Buy, volume)
    
    @staticmethod
    def Sell(volume): return Market(Side.Sell, volume)
        
@registry.expose(alias=['Market'])
@sig(args=(Side,), rv=function((Volume,), IOrder))
def MarketFactory(side):
    return bind.Construct(Market, side)
    
MarketFactory.__doc__ = Market.__doc__