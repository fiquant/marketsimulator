from marketsim import request, _

import _meta

class Order_Impl(_meta.OwnsSingleOrder):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, proto, delay):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._delay = delay

    def bind_ex(self, ctx):
        self.proto.bind_ex(ctx)
        self._ctx_ex = ctx
        self._bound_ex = True
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
    
    def startProcessing(self):
        self.send(self.proto)
        self.world.scheduleAfter(self._delay, 
                                 _(self.orderBook, 
                                   request.Cancel(self.proto)).process)
