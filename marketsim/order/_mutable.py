from marketsim import request, _, event, Event, types
from marketsim.types import *

from _limit import Limit

class Base(types.IOrder):
    """ Meta order with mutable parameters
        User should provide an observable that generates new parameters for the order
    """
    
    def __init__(self, source):
        self._order = None
        self.source = source
        
    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self.source += _(self)._update
        self._update(None)
        
    def onOrderMatched(self, order, price, volume):
        self.owner.onOrderMatched(self, price, volume)
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
    
    def onOrderCharged(self, price):
        self.owner.onOrderCharged(price)    
        
    def _dispose(self):
        if self._order is not None:
            self.orderBook.process(request.Cancel(self._order))
        
    def _update(self, dummy):
        self._dispose()
        params = self.source()
        if params is not None:
            self._order = Limit(*params)
            self._order.owner = self
            self.orderBook.process(self._order)
            
    @property
    def side(self):
        return self._order.side
        
    def __str__(self):
        if self._order is not None:
            return "%s_%s[%d/%d]" % (type(self).__name__, self._side, self._volumeUnmatched, self.volumeTotal)
        else:
            return "MutableOrder"

    def __repr__(self):
        return self.__str__()

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
    
    @property
    def volumeTotal(self):
        return self.volumeFilled + self.volumeUnmatched

    @property
    def volumeFilled(self):
        return self._order.volumeFilled

    @property
    def volumeUnmatched(self):
        """ Volume to trade
        """
        return self._order.volumeUnmatched

    @property
    def signedVolumeUnmatched(self):
        return self._order.signedVolumeUnmatched
    
    @property
    def empty(self):
        """ Volume is empty iff its volume is 0
        """
        return self._order.empty

    @property
    def cancelled(self):
        """ Is order cancelled
        """
        return self._order.cancelled
    

    def cancel(self):
        """ Marks order as cancelled. Notifies the order book about it
        """
        self._dispose()
        self.source -= _(self)._update

    def __hash__(self):
        return id(self)
    
Impl = types.Factory("Impl", """(Base):
    _properties = { 
        'source' : IObservable[%(T)s],
    }
""", globals())
    
def Mutable(source):
    
    return Impl[source.T](source)