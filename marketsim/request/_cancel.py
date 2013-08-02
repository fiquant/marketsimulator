from marketsim import types

class Cancel(types.IRequest):
    """ Cancels another order that can be for example a limit or an iceberg order
    """
    def __init__(self, orderToBeCancelled):
        self._toCancel = orderToBeCancelled
        
    def charge(self, price):
        self.on_charge.fire(price)
        
    def processIn(self, orderBook):
        orderBook.cancelOrder(self._toCancel)

