from _limit import Factory
from _base import HasPrice
from _meta import OwnsSingleOrder
from marketsim import ops, request, meta, types, registry, bind, event, _, combine

class Iceberg(OwnsSingleOrder, HasPrice):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, side, price, volume):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        HasPrice.__init__(self, price)
        # we pretend that we are an order initially having given volume
        OwnsSingleOrder.__init__(self, side, volume, None)
        self._lotSize = lotSize
        self._subscription = None
                
    def onOrderMatched(self, order, price, volume):
        OwnsSingleOrder.onOrderMatched(self, order, price, volume)
        if order.empty:
            self._tryToResend()

    def _tryToResend(self):
        """ Tries to send a real order to the order bookCaC
        """
        # if we have something to trade
        if self.volumeUnmatched > 0: 
            # define volume to trade
            v = min(self._lotSize, self.volumeUnmatched)
            # create a real order
            self.send(Factory(ops.constant(self.side), 
                              ops.constant(self.price), 
                              ops.constant(v))())
        else:
            # now we have nothing to trade
            self.order = None

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
            order = Iceberg(lotsize, side, price, volume)
            return order
        return None
