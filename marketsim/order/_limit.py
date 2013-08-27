from _base import *
from marketsim import combine, registry, bind, ops, meta, types
from marketsim.types import *

class Limit(Default, HasSide, HasPrice, HasVolume, Cancellable):
    """ Limit order of the given *side*, *price* and *volume*
    """

    def __init__(self, side, price, volume, owner = None, volumeFilled = 0):
        """ Initializes order with price and volume
        price is a limit price on which order can be traded
        if there are no suitable orders, the limit order remains in the order book
        """
        HasSide.__init__(self, side)
        HasVolume.__init__(self, volume, volumeFilled)
        Cancellable.__init__(self)
        Default.__init__(self, owner)
        HasPrice.__init__(self, price)
        
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
        return Limit(opt(self.side, side),
                     opt(self.price, price),
                     opt(self.volumeUnmatched, volume))
        
    def clone(self):
        return Limit(self.side, self.price, self.volumeUnmatched, self.owner, self.volumeFilled)
        
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
    def Buy(price, volume): return Limit(Side.Buy, price, volume)
     
    @staticmethod
    def Sell(price, volume): return Limit(Side.Sell, price, volume)
    
Order = Limit

class Factory(types.IPersistentOrderGenerator, combine.SidePriceVolume):
    
    def __call__(self):
        params = combine.SidePriceVolume.__call__(self)
        return Limit(*params) if params is not None else None
    
@sig((IFunction[Side],IFunction[float]), IOrderGenerator)
class SidePrice_Factory(combine.Volume):
    
    def __call__(self, side, price):
        return Factory(side, price, self.volume)
    
class Price_Factory(IFunction[IOrderGenerator, float]):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell), 
                 volume = ops.constant(1.)):
        self.side = side
        self.volume = volume
        
    _properties = { 
        'side'   : types.IFunction[Side],
        'volume' : types.IFunction[float],
     }
    
    def create(self, price):
        return Limit(self.side(), price, self.volume())
    
    def __call__(self, price):
        return Factory(self.side, price, self.volume)
    
class Side_Factory(IFunction[IOrderGenerator, Side]):
    
    def __init__(self, price = ops.constant(100.), volume = ops.constant(1.)):
        self.price = price
        self.volume = volume
        
    _properties = { 
        'price'  : types.IFunction[float],
        'volume' : types.IFunction[float] 
    }
    
    def __call__(self, side):
        return Factory(side, self.price, self.volume)

class PriceVolume_Factory(IFunction[IOrderGenerator, PriceVolume]):
    
    def __init__(self, side = ops.constant(Side.Sell)):
        self.side = side
        
    _properties = { 
        'side'   : types.IFunction[Side]
     }
    
    def __call__(self, price, volume):
        return Factory(self.side, price, volume)

class Volume_Factory(IFunction[IOrderGenerator, PriceVolume]):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell),
                 price = ops.constant(100.)):
        self.side = side
        self.price = price
        
    _properties = { 
        'side'   : types.IFunction[Side],
        'price'  : types.IFunction[float],
     }
    
    def __call__(self, volume):
        return Factory(self.side, self.price, volume)

    
class LimitOrderFactory(types.IFunction[types.IOrder, types.SidePriceVolume]):
    
    def __call__(self, side, price, volume):
        return Limit(side, price, volume) 
    
@registry.expose(alias=['Limit'])
@sig(args=(Side,), rv=function((Price, Volume,), IOrder))
def LimitFactory(side):
    return bind.Construct(Limit, side)

LimitFactory.__doc__ = Limit.__doc__ 

class AdaptLimit_SidePriceBound(object):
    
    def __init__(self, orderFactory, side, price):
        self.orderFactory = orderFactory
        self.side = side
        self.price = price
        
    def __call__(self, volume):
        return self.orderFactory(self.side)(self.price, volume)

@registry.expose(alias=['Adapt limit order'])
class AdaptLimit(object):
    """ Adapts limit-like orders for usage where market-like orders are expected.
    User should provide *priceFunc* calculating price of order to create
    """
    
    def __init__(self, orderFactory = LimitFactory, priceFunc = ops.constant(100)):
        self.orderFactory = orderFactory
        self.priceFunc = priceFunc
        
    _properties = { 'orderFactory' : meta.function(args=(Side,), rv=function((Price, Volume,), IOrder)),
                    'priceFunc'    : meta.function((), Price)}
    
    _types = [meta.function(args=(Side,), rv=function((Volume,), IOrder))]
    
    def __repr__(self):
        return 'AdaptLimit(' + repr(self.orderFactory) + ', ' + repr(self.priceFunc) + ')'
        
    def __call__(self, side):
        price = self.priceFunc()
        price = self.priceFunc()
        return AdaptLimit_SidePriceBound(self.orderFactory, side, price)
