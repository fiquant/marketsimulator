from _base import Base
from marketsim import combine, registry, bind, ops, meta, types
from marketsim.types import *

class Limit(Base):
    """ Limit order of the given *side*, *price* and *volume*
    """

    def __init__(self, side, price, volume):
        """ Initializes order with price and volume
        price is a limit price on which order can be traded
        if there are no suitable orders, the limit order remains in the order book
        """
        Base.__init__(self, side, volume)
        self._price = price
        
    def clone(self):
        return Limit(self.side, self.price, self.volume)
        
    def copyTo(self, dst):
        Base.copyTo(self, dst)
        dst._price = self._price

    def __str__(self):
        return type(self).__name__ + "("+str(self.side)+", Price=" + str(self.price) + ", volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

    def processIn(self, orderBook):
        """ Order book calls this method to ask the order 
        how it should be processed in the order book (a la Visitor)
        """
        orderBook.processLimitOrder(self)

    @property
    def signedPrice(self):
        """ Returns "signed" price of the order:
        positive if the order is on sell side
        negative if the order is on buy side 
        """
        return self.side.makePriceSigned(self._price)

    @property
    def price(self):
        """ Limit price of the order
        """
        return self._price
    
    @price.setter
    def price(self, value):
        """ When an order is put into an oredr book, 
        its price might be corrected with respect to order tick size
        this function is used to notify the order about the new corrected price
        """
        self._price = value

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
        v = min(self.volume, other.volume)
        # price to trade is my price
        # it means that incoming limit order is considered as a market order
        # and its price is not taken for the trade
        p = self.price
        pv = (p,v)
        # notify trade side about the it
        self.onMatchedWith(other, pv)
        other.onMatchedWith(self, pv)
        return pv

    @staticmethod
    def Buy(price, volume): return Limit(Side.Buy, price, volume)
     
    @staticmethod
    def Sell(price, volume): return Limit(Side.Sell, price, volume)

class Factory(types.IPersistentOrderGenerator, combine.SidePriceVolume):
    
    def __call__(self):
        params = combine.SidePriceVolume.__call__(self)
        return Limit(*params) if params is not None else None
    
class SidePrice_Factory(IFunction[IOrderGenerator, SidePrice]):
    
    def __init__(self, volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 'volume' : types.IFunction[float] }
    
    def __call__(self, side, price):
        return Factory(side, price, self.volume)
    
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
