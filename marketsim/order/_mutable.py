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
        
    def _onOrderMatched(self, order, other, (price, volume)):
        self.owner._onOrderMatched(order, other, (price, volume))
        
    def _onOrderDisposed(self, order):
        self.owner._onOrderDisposed(order)
    
    def _onOrderCharged(self, price):
        self.owner._onOrderCharged(price)    
        
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
            return type(self).__name__ + "("+str(self.side)+", volume=" + str(self.volume) \
                    + ", P&L="+str(self.PnL)+")"
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
    def volume(self):
        """ Volume to trade
        """
        return self._order.volume

    @property
    def signedVolume(self):
        return self._order.signedVolume
    
    @property 
    def PnL(self):
        """ P&L of the order. 
        positive, if it is a sell side order
        negative, if it is a buy side order
        """
        return self._order.PnL

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