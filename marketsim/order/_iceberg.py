from _limit import Factory, Volume_Factory
from _base import HasPrice
from _meta import OwnsSingleOrder
from marketsim import ops, request, meta, types, registry, bind, event, _, combine

class Iceberg(OwnsSingleOrder, HasPrice):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, factory, volume):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        HasPrice.__init__(self, factory.price())
        # we pretend that we are an order initially having given volume
        OwnsSingleOrder.__init__(self, factory.side(), volume, None)
        self._lotSize = lotSize
        self._subscription = None
        self._orderGenerator = factory(_(self).getVolumeToTrade)
                
    def onOrderMatched(self, order, price, volume):
        OwnsSingleOrder.onOrderMatched(self, order, price, volume)
        if order.empty:
            self._tryToResend()
            
    def getVolumeToTrade(self):
        return min(self._lotSize, self.volumeUnmatched) 

    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        self.send(self._orderGenerator())

    def processIn(self, book):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self.orderBook = book
        self._tryToResend()
        
class FactoryLimit(types.IPersistentOrderGenerator, combine.SidePriceVolumeLotSize):
    
    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        params = combine.SidePriceVolumeLotSize.__call__(self)
        if params is not None:
            (side, price, volume, lotsize) = params
            factory = Volume_Factory(ops.constant(side), 
                                     ops.constant(price))            
            order = Iceberg(lotsize, factory, volume)
            return order
        return None
