from _base import Base
from marketsim import registry, Construct, mathutils, meta
from marketsim.types import *

class Limit(Base):
    """ Base class for limit orders. 
    Adds to the basic order functionality price handling
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
        return type(self).__name__ + "("+self.side+", Price=" + str(self.price) + ", volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

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
        """ Matches the order with another one
        Returns True iff this order is completely matched
        """
        if other.canBeMatched(self):
            # volume to trade
            v = min(self.volume, other.volume)
            assert v > 0
            # price to trade is my price
            # it means that incoming limit order is considered as a market order
            # and its price is not taken for the trade
            p = self.price
            # notify trade side about the it
            self.onMatchedWith(other, (p,v))
            other.onMatchedWith(self, (p,v))
        return self.empty

    @staticmethod
    def Buy(price, volume): return Limit(Side.Buy, price, volume)
     
    @staticmethod
    def Sell(price, volume): return Limit(Side.Sell, price, volume) 
    
@registry.expose(alias='Limit')
@sig(args=(Side,), rv=function((Price, Volume,), IOrder))
def LimitFactory(side):
    return Construct(Limit, side)

class AdaptLimit_SidePriceBound(object):
    
    def __init__(self, orderFactory, side, price):
        self.orderFactory = orderFactory
        self.side = side
        self.price = price
        
    def __call__(self, volume):
        return self.orderFactory(self.side)(self.price, volume)

@registry.expose(alias='Adapt limit order')
class AdaptLimit(object):
    
    def __init__(self, orderFactory = LimitFactory, priceFunc = mathutils.constant(100)):
        self.orderFactory = orderFactory
        self.priceFunc = priceFunc
        
    _properties = { 'orderFactory' : meta.function(args=(Side,), rv=function((Price, Volume,), IOrder)),
                    'priceFunc'    : meta.function((), Price)}
    
    _types = [meta.function(args=(Side,), rv=function((Volume,), IOrder))]
        
    def __call__(self, side):
        price = self.priceFunc()
        return AdaptLimit_SidePriceBound(self.orderFactory, side, price)
