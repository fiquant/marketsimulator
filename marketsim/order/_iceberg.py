import _limit 
from _base import HasPrice
from _meta import OwnsSingleOrder
from marketsim import ops, request, meta, types, registry, bind, event, _, combine

class Iceberg(OwnsSingleOrder, HasPrice):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, protoorder):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        HasPrice.__init__(self, protoorder.price)
        # we pretend that we are an order initially having given volume
        OwnsSingleOrder.__init__(self, protoorder.side, protoorder.volumeUnmatched, None)
        self._proto = protoorder
        self._lotSize = lotSize
        self._subscription = None
                
    def onOrderMatched(self, order, price, volume):
        OwnsSingleOrder.onOrderMatched(self, order, price, volume)
        if order.empty and not self.empty:
            self._tryToResend()
            
    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        self.send(self._proto.With(volume = min(self._lotSize, self.volumeUnmatched)))

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
    
    def __call__(self):
        lotSize = self.lotSize()
        if lotSize is None:
            return None
        proto = self.factory()
        if proto is None:
            return None
        return Iceberg(lotSize, proto)
