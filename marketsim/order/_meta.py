import _base

class Base(_base.Base):
    
    def onOrderMatched(self, order, price, volume):
        self.owner.onOrderMatched(self, price, volume)
        
    def onOrderDisposed(self, order):
        pass
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
            

    
        
    