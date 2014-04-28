from marketsim import types, request, context
from .. import _base

class Base(_base.Base):
    
    def processIn(self, orderBook):
        self.orderBook = orderBook
        self.startProcessing()
    
    @property
    def orderBook(self):
        return self._book
        
    @orderBook.setter
    def orderBook(self, book):
        self._book = book

    @property
    def world(self):
        return self._ctx_ex.world
        
    @property
    def active(self):
        return hasattr(self, '_book') and not self.cancelled
        
    def send(self, order):
        from marketsim.gen._out._iorder import IOrder
        if order is not None:
            if isinstance(order, IOrder):
                order.owner = self
            order.bind_ex(self._ctx_ex)
            self._book.process(order)
        return order
    
    def onOrderMatched(self, order, price, volume):
        self.onMatchedWith(price, volume)
        
    def onOrderDisposed(self, order):
        pass
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
            
class OwnsSingleOrder(Base):
    
    def __init__(self, proto):
        Base.__init__(self, proto.volumeUnmatched)
        self._order = None
        self._proto = proto
        
    @property
    def side(self):
        return self._proto.side
    
    @property
    def price(self): # NB! defined only if proto order has price
        return self._proto.price 
        
    @property
    def proto(self):
        return self._proto
    
    def __repr__(self):
        return self.__str__()
    
    def send(self, order):
        self._order = Base.send(self, order)
        
    def __str__(self):
        return Base.__str__(self) + '(' + str(self._proto) + ')'
        
    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, value):
        self._order = value

    def _dispose(self):
        if self._order is not None:
            self.orderBook.process(request.Cancel(self._order))
            self._order = None
            
    def cancel(self):
        """ Marks order as cancelled. Notifies the order book about it
        """
        self._cancelled = True
        if self._order is None:
            self.onOrderDisposed(None)
        else:
            self._dispose()

    def onOrderDisposed(self, order):
        if self._cancelled:
            self.owner.onOrderDisposed(self)
    
    
        
    