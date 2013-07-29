from marketsim import combine, ops, registry, meta, types, bind
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

class Factory_Base(types.IOrderGenerator):
    
    def __call__(self):
        params = self.get()
        return Market(*params) if params is not None else None

class Factory(Factory_Base, combine.SideVolume):
    
    def get(self):
        return combine.SideVolume.__call__(self)
    
class FactorySigned(Factory_Base, combine.SignedVolume):
    
    def get(self):
        return combine.SignedVolume.__call__(self)
        
@registry.expose(alias=['Market'])
@sig(args=(Side,), rv=function((Volume,), IOrder))
def MarketFactory(side):
    return bind.Construct(Market, side)
    
MarketFactory.__doc__ = Market.__doc__