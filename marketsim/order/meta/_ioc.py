from marketsim import request, combine, meta, types, _, registry, bind, Side

from .. import _limit 

import _meta

class ImmediateOrCancel(_meta.OwnsSingleOrder):
    """ This a combination of a limit order and a cancel order sent immediately
    It works as a market order in sense that it is not put into the order queue 
    but can be matched (as a limit order) 
    only if there are orders with suitable price in the queue
    """
    
    def __init__(self, proto):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        _meta.OwnsSingleOrder.__init__(self, proto)
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
        
    def processIn(self, orderBook):
        self.orderBook = orderBook
        self.send(self.proto)
        self.orderBook.process(request.Cancel(self.proto))
    
Order = ImmediateOrCancel

class Factory(types.IOrderGenerator):
    
    def __init__(self, inner = _limit.Factory()):
        self.inner = inner
        
    _properties = {
        'inner'  : types.IOrderGenerator,  
    }

    def __call__(self):
        proto = self.inner()
        return Order(proto) if proto is not None else None 
