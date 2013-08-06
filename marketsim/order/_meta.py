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
        self.owner.onOrderMatched(self, price, volume)
        
    def onOrderDisposed(self, order):
        pass
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
            

    
        
    