from marketsim import Side, Event

class OrderBase(object):
    """ Base class for market and limit orders.
    Responsible for:
    - tracking order's volume
    - tracking order's P&L
    - keeping order cancellation flag (does it needed for market orders???)
    - notifying order listeners about order matching
    TBD: split into Cancelable, HavingVolume base classes
    """

    def __init__(self, volume):
        """ Initializes order by volume to trade
        """
        self._volume = volume
        self._cancelled = False
        self._PnL = 0
        self.on_matched = Event()

    def __str__(self):
        return type(self).__name__ + "(volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

    def __repr__(self):
        return self.__str__()

    @property
    def volume(self):
        """ Volume to trade
        """
        return self._volume
    
    @property 
    def PnL(self):
        """ P&L of the order. 
        positive, if it is a sell side order
        negative, if it is a buy side order
        """
        return self.makePriceSigned(self._PnL)

    @property
    def empty(self):
        """ Volume is empty iff its volume is 0
        """
        return self.volume == 0

    @property
    def cancelled(self):
        """ Is order cancelled
        """
        return self._cancelled
    

    def cancel(self, book=None):
        """ Marks order as cancelled. Notifies the order book about it
        """
        self._cancelled = True
        if book:
            book.onOrderCancelled(self)

    def onMatchedWith(self, other, (price,volume)):
        """ Called when the order is matched with another order
        other - other order
        price - price at which the match was done
        volume - volume of the match.
        In this method we correct order volume and P&L 
        and notify order listener about the match
        """
        self._volume -= volume
        self._PnL += volume * price
        #print "OrderMatched:", self, other, (price, volume)
        self.on_matched.fire(self, other, (price, volume))
        
class CancelOrder(object):
    """ Cancels another order that can be for example a limit or an iceberg order
    """
    def __init__(self, orderToBeCancelled):
        self._toCancel = orderToBeCancelled
        self.on_matched = Event() # just dummy event. never called
        
    def processIn(self, orderBook):
        self._toCancel.cancel(book = orderBook)


class LimitOrderBase(OrderBase):
    """ Base class for limit orders. 
    Adds to the basic order functionality price handling
    """

    def __init__(self, price, volume):
        """ Initializes order with price and volume
        price is a limit price on which order can be traded
        if there are no suitable orders, the limit order remains in the order book
        """
        OrderBase.__init__(self, volume)
        self._price = price

    def __str__(self):
        return type(self).__name__ + "(Price=" + str(self.price) + ", volume=" + str(self.volume) + ", P&L="+str(self.PnL)+")"

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
        return self.makePriceSigned(self._price)

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
        assert other.side == Side.opposite(self.side)
        return not self.better(other.price, self.price)

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

class BuySideOrderBase(object):
    """ Base class for buy side orders
    TBD: this logic can be moved into future BuySide and SellSide classes
    """

    @property
    def PnL(self):
        """ Returns P&L for the order
        negative for buy orders
        """
        return -self._PnL
    
    @staticmethod
    def better(x, y):
        """ Returns True iff signed price 'x' is more attractive than signed price 'y'
        """
        return x > y
    
    @staticmethod
    def makePriceSigned(price):
        """ Makes price of something on buy side negative
        """
        return -price
    
    side = Side.Buy

class SellSideOrderBase(object):
    """ Base class for sell side orders
    TBD: this logic can be moved into future BuySide and SellSide classes
    """

    @property
    def PnL(self):
        """ Returns P&L for the order
        positive for sell orders
        """
        return +self._PnL

    @staticmethod
    def makePriceSigned(price):
        """ Leaves price of something on sell side positive
        """
        return +price

    @staticmethod
    def better(x, y):
        """ Returns True iff signed price 'x' is more attractive than signed price 'y'
        """
        return x < y

    side = Side.Sell

class MarketOrderBase(OrderBase):
    """ Base class for market orders
    """

    def __init__(self, volume):
        """ Initializes order with volume to trade
        """
        OrderBase.__init__(self, volume)

    def processIn(self, orderBook):
        """ Order book calls this method to ask the order 
        how it should be processed in the order book (a la Visitor)
        """
        orderBook.processMarketOrder(self)

    def canBeMatched(self, other):
        """ Returns True iff this order can be matched with 'other'
        """
        assert other.side == Side.opposite(self.side)
        return True

class MarketOrderBuy(MarketOrderBase, BuySideOrderBase):
    """ Market order buy side
    """

    def __init__(self, volume):
        MarketOrderBase.__init__(self, volume)

class MarketOrderSell(MarketOrderBase, SellSideOrderBase):
    """ Market order sell side
    """

    def __init__(self, volume):
        MarketOrderBase.__init__(self, volume)

def MarketOrderT(side):
    """ Returns a factory to create market orders buy if 'side' is Side.Buy
    and a factory to create market orders sell if 'side' is Side.Sell
    """
    return MarketOrderSell if side==Side.Sell else MarketOrderBuy

class LimitOrderBuy(LimitOrderBase, BuySideOrderBase):
    """ Limit order buy side
    """

    def __init__(self, price, volume):
        """ Initializes order with volume and a limit price 
        (trades cannot be done done on price higher than this one)
        """
        LimitOrderBase.__init__(self, price, volume)

class LimitOrderSell(LimitOrderBase, SellSideOrderBase):
    """ Limit order sell side
    """

    def __init__(self, price, volume):
        """ Initializes order with volume and a limit price 
        (trades cannot be done done on price lower than this one)
        """
        LimitOrderBase.__init__(self, price, volume)

def LimitOrderT(side):
    """ Returns a factory to create limit orders buy if 'side' is Side.Buy
    and a factory to create limit orders sell if 'side' is Side.Sell
    """
    return LimitOrderSell if side==Side.Sell else LimitOrderBuy

class LimitMarketOrder(OrderBase):
    """ This a combination of a limit order and a cancel order sent immediately
    It works as a market order in sense that it is not put into the order queue 
    but can be matched (as a limit order) 
    only if there are orders with suitable price in the queue 
    """
    
    def __init__(self, price, volume, limitOrderFactory):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        OrderBase.__init__(self, volume)
        # we create a limit order
        self._order = limitOrderFactory(price, volume)
        # translate its events to our listeners
        self._order.on_matched += self.on_matched.fire
        self.side = limitOrderFactory.side
        
    def processIn(self, orderBook):
        orderBook.process(self._order)
        orderBook.process(CancelOrder(self._order))
        
    @property 
    def volume(self):
        return self._order.volume 
    
    @property
    def PnL(self):
        return self._order.PnL
    
class LimitMarketOrderBuy(LimitMarketOrder):
    
    def __init__(self, price, volume):
        LimitMarketOrder.__init__(self, price, volume, LimitOrderBuy)
        
class LimitMarketOrderSell(LimitMarketOrder):
    
    def __init__(self, price, volume):
        LimitMarketOrder.__init__(self, price, volume, LimitOrderSell)
        
def LimitMarketOrderT(side):
    return LimitMarketOrderBuy if side == Side.Buy else LimitMarketOrderSell
    
