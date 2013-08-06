import _base

class Base(_base.Base):
    
    def onOrderMatched(self, order, price, volume):
        self.owner.onOrderMatched(self, price, volume)
        
    def onOrderDisposed(self, order):
        pass
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
        
class HasPriceProxied(object):
    
    @property
    def signedPrice(self):
        """ Returns "signed" price of the order:
        positive if the order is on sell side
        negative if the order is on buy side 
        """
        return self._order.signedPrice

    @property
    def price(self):
        """ Limit price of the order
        """
        return self._order.price
    

    
        
    