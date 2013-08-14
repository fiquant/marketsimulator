import _limit 
from _base import HasPrice
from _meta import OwnsSingleOrder
from marketsim import context, ops, request, meta, types, registry, bind, event, _, combine

class Iceberg(OwnsSingleOrder):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, proto):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        OwnsSingleOrder.__init__(self, proto)
        self._lotSize = lotSize
        
    def With(self, **kwargs):
        return Iceberg(self._lotSize, self.proto.With(**kwargs))
                
    def onOrderDisposed(self, order):
        if not self.cancelled:
            self._tryToResend()
        OwnsSingleOrder.onOrderDisposed(self, order)
            
    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        self.send(self.proto.With(volume = min(self._lotSize, self.volumeUnmatched)))

    def processIn(self, book):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self.orderBook = book
        self._tryToResend()
        
class Factory(types.IOrderGenerator):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : types.IFunction[float],
        'factory' : types.IOrderGenerator
    }
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        lotSize = self.lotSize()
        if lotSize is None:
            return None
        proto = self.factory()
        if proto is None:
            return None
        order = Iceberg(lotSize, proto)
        return order
    
class Price_Factory(types.IFunction[types.IOrderGenerator, float]):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.Price_Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : types.IFunction[float],
        'factory' : types.IFunction[types.IOrderGenerator, float]
    }
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    # it should implement also __call__ but later we will fix it
    
    def create(self, price):
        lotSize = self.lotSize()
        if lotSize is None:
            return None
        proto = self.factory.create(price)
        return Iceberg(lotSize, proto) if proto is not None else None
