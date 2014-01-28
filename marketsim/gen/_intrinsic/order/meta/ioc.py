from marketsim import request

import _meta

class Order_Impl(_meta.OwnsSingleOrder):
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
