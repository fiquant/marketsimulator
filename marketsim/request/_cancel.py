from marketsim import types, _

class Cancel(object):
    """ Cancels another order that can be for example a limit or an iceberg order
    """
    def __init__(self, orderToBeCancelled, callback = None):
        self._toCancel = orderToBeCancelled
        self.callback = callback if callback is not None else _(self)._empty
        
    def _empty(self): pass
        
    def charge(self, price):
        self.on_charge.fire(price)
        
    def processIn(self, orderBook):
        orderBook.cancelOrder(self._toCancel)
        self.callback()

