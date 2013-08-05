import _base

class Base(_base.Base):
    
    def _onOrderMatched(self, order, other, (price, volume)):
        self.owner._onOrderMatched(self, other, (price, volume))
        
    def _onOrderCancelled(self, order):
        pass
    
    def _onOrderCharged(self, price):
        self.owner._onOrderCharged(price)    
        
    