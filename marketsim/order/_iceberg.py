from _base import Base
from _cancel import Cancel
from _limit import LimitFactory

from marketsim import meta, types, registry

class Volume(object):
    """ Auxiliary class to hold market order initialization parameters 
    """
    def __init__(self, v):
        self._volume = v

    hasPrice = False

    @property
    def packed(self):
        """ Returns a tuple (volume)"""
        return self._volume,

class PriceVolume(object):
    """ Auxiliary class to hold limit order initialization parameters 
    """

    def __init__(self, p, v):
        self._price = p
        self._volume = v

    hasPrice = True

    @property
    def packed(self):
        """ Returns a tuple (price, volume)"""
        return self._price, self._volume

def unpack(args):
    """ Unpacks from args volume (and possibly) price of order to create 
    """
    return PriceVolume(*args) if len(args) == 2 else Volume(*args)

class Iceberg(Base):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, volumeLimit, orderFactory, *args):
        """ Initializes iceberg order
        volumeLimit -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        self._args = unpack(args)
        # we pretend that we are an order initially having given volume
        Base.__init__(self, None, self._args._volume)
        self._volumeLimit = volumeLimit
        self._orderFactory = orderFactory
        self._current = None
        
    @property
    def side(self):
        return self._current.side if self._current else None

    @property
    def price(self):  # NB! defined only for limit orders
        assert self._args.hasPrice
        return self._args._price

    def _onMatchedWith(self, myOrder, other, pv):
        """ Called when real order has been matched
        We notify our listeners about the trade
        and if it is matched completely try to resend a new order
        """
        self.on_matched.fire(self, other, pv)
        if self._current.empty:
            self._PnL += self._current.PnL
            self._tryToResend()

    def cancel(self):
        """ If we are asked to be cancelled, we mark ourselves as cancelled 
        and the make the real order also cancelled 
        """
        Base.cancel(self)
        if self._current:
            self._book.process(Cancel(self._current))

    @property
    def PnL(self):
        """ Returns P&L. It sum of P&L of traded orders and P&L of the order being traded
        """
        return self._PnL + (self._current.PnL if self._current else 0)

    @property
    def volume(self):
        """ Returns volume left to trade. 
        """
        return self._volume + (self._current.volume if self._current else 0)

    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        # if we have something to trade
        if self._volume > 0: 
            # define volume to trade
            v = min(self._volumeLimit, self._volume)
            self._args._volume = v
            # diminish our volume to trade
            self._volume -= v
            # create a real order
            self._current = self._orderFactory(*self._args.packed)
            # start listening events about order matching
            self._current.on_matched += self._onMatchedWith
            # and send the order to the order book    
            self._book.process(self._current)
        else:
            # now we have nothing to trade
            self._current = None

    def processIn(self, book):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self._book = book
        self._tryToResend()

def iceberg(volumeLimit, orderFactory):
    """ Returns a function to create iceberg orders with 
    given volumeLimit and orderFactory to create real orders
    """
    def inner(*args):
        return Iceberg(volumeLimit, orderFactory, *args)
    return inner

LimitOrderFactorySignature = meta.function((types.Side,), meta.function((types.Price, types.Volume), types.IOrder))

@registry.expose('Iceberg')
class IcebergFactory(object):
    
    def __init__(self, volumeLimit = 10, orderFactory = LimitFactory):
        self.volumeLimit = volumeLimit
        self.orderFactory = orderFactory
        
    _types = [LimitOrderFactorySignature]
        
    _properties = {'volumeLimit'  : int,
                   'orderFactory' : LimitOrderFactorySignature}
        
    def __call__(self, side):
        def inner(price, volume):
            return Iceberg(self.volumeLimit, self.orderFactory(side), price, volume)
        return inner
