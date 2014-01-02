from marketsim import request, _

import _meta

class WithExpiry_Impl(_meta.OwnsSingleOrder):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, delay, proto):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._delay = delay
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
    
    def startProcessing(self):
        self.send(self.proto)
        self.world.scheduleAfter(self._delay, 
                                 _(self.orderBook, 
                                   request.Cancel(self.proto)).process)
