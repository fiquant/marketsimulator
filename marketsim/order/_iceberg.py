from _limit import LimitFactory
import _meta
from marketsim import request, meta, types, registry, bind, event, _, combine

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

class Iceberg(_meta.Base):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, orderFactory, *args):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        self._args = unpack(args)
        # we pretend that we are an order initially having given volume
        _meta.Base.__init__(self, None, self._args._volume)
        self._lotSize = lotSize
        self._orderFactory = orderFactory
        self._current = None
        self._subscription = None
        self._side = None
        
    def onOrderMatched(self, order, price, volume):
        self.onMatchedWith(price, volume)
        if self._current.empty:
            self._tryToResend()

    def onOrderDisposed(self, order):
        if self._cancelled:
            self.owner.onOrderDisposed(self)

    def cancel(self):
        """ If we are asked to be cancelled, we mark ourselves as cancelled 
        and the make the real order also cancelled 
        """
        self._cancelled = True
        if self._current is not None:
            self._book.process(request.Cancel(self._current))
        else:
            self.onOrderDisposed(None)

    def _tryToResend(self):
        """ Tries to send a real order to the order bookCaC
        """
        # if we have something to trade
        if self._volumeUnmatched > 0: 
            # define volume to trade
            v = min(self._lotSize, self._volumeUnmatched)
            self._args._volume = v
            # create a real order
            self._current = self._orderFactory(*self._args.packed)
            self._current.owner = self
            self._side = self._current.side
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
        
class FactoryLimit(types.IPersistentOrderGenerator, combine.SidePriceVolumeLotSize):
    
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        params = combine.SidePriceVolumeLotSize.__call__(self)
        if params is not None:
            (side, price, volume, lotsize) = params
            order = Iceberg(lotsize, LimitFactory(side), price, volume)
            return order
        return None


def iceberg(lotSize, orderFactory):
    """ Returns a function to create iceberg orders with 
    given lotSize and orderFactory to create real orders
    """
    def inner(*args):
        return Iceberg(lotSize, orderFactory, *args)
    return inner

LimitOrderFactorySignature = meta.function((types.Side,), meta.function((types.Price, types.Volume), types.IOrder))

@registry.expose(['Iceberg'])
class IcebergFactory(object):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """
    
    def __init__(self, lotSize = 10, orderFactory = LimitFactory):
        self.lotSize = lotSize
        self.orderFactory = orderFactory
        
    _types = [LimitOrderFactorySignature]
        
    _properties = {'lotSize'  : int,
                   'orderFactory' : LimitOrderFactorySignature}
    
    def __call__(self, side):
        return bind.Construct(Iceberg, self.lotSize, self.orderFactory(side))