from marketsim import combine, ops, registry, meta, types, bind
from marketsim.types import *
from _base import *

class Market(Default, HasSide, HasVolume, Cancellable):
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
        return Market(opt(self.side, side),
                      opt(self.volumeUnmatched, volume))

    def copyTo(self, dst):
        HasSide.copyTo(self, dst)
        HasVolume.copyTo(self, dst)
        Cancellable.copyTo(self, dst)
        
    def __str__(self):
        return "%s_%s%s" % (type(self).__name__, HasSide.__str__(self), HasVolume.__str__(self))
        
    def clone(self):
        return Market(self.side, self.volumeUnmatched, self.owner, self.volumeFilled)

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
    def Buy(volume): return Market(Side.Buy, volume)
    
    @staticmethod
    def Sell(volume): return Market(Side.Sell, volume)
    
Order = Market

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
    
@sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(combine.Volume):
    
    def __call__(self, side):
        return Factory(side, self.volume)
        
@registry.expose(alias=['Market'])
@sig(args=(Side,), rv=function((Volume,), IOrder))
def MarketFactory(side):
    return bind.Construct(Market, side)
    
MarketFactory.__doc__ = Market.__doc__