import _meta

class Order_Impl(_meta.OwnsSingleOrder):
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
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._lotSize = lotSize
        
    def With(self, **kwargs):
        return Order_Impl(self._lotSize, self.proto.With(**kwargs))
                
    def onOrderDisposed(self, order):
        if not self.cancelled:
            self._tryToResend()
        _meta.OwnsSingleOrder.onOrderDisposed(self, order)
            
    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        self.send(self.proto.With(volume = min(self._lotSize, self.volumeUnmatched)))

    def startProcessing(self):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self._tryToResend()
