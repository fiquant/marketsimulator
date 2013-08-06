from marketsim import request
import _base

class Base(_base.Base):
    
    @property
    def orderBook(self):
        return self._book
        
    @orderBook.setter
    def orderBook(self, book):
        self._book = book
        
    def send(self, order):
        if order is not None:
            order.owner = self
            self._book.process(order)
        return order
    
    def onOrderMatched(self, order, price, volume):
        self.onMatchedWith(price, volume)
        
    def onOrderDisposed(self, order):
        pass
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
            
class OwnsSingleOrder(Base):
    
    def __init__(self, side, volume, owner = None, volumeFilled = 0):
        Base.__init__(self, side, volume, owner, volumeFilled)
        self._order = None
    
    def __str__(self):
        if self._order is not None:
            Base.__str__()
        else:
            return type(self).__class__.__name__

    def __repr__(self):
        return self.__str__()
    
    def send(self, order):
        self._order = Base.send(self, order)
        
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
    
    
        
    