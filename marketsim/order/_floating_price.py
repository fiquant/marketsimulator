from marketsim import request, _, event, Event, types
from marketsim.types import *

from _limit import Limit

import _meta

class FloatingPrice(_meta.Base):
    """ Meta order controlling price of the underlying order
        When price changes it cancels underlying order and resends it with changed price
        For the moment we work only on limit orders but this mecanism might be extented to any persistent order
    """
    
    def __init__(self, side, price, volume):
        _meta.Base.__init__(self, side, volume)
        self._order = None
        self._price = price

    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self._price += _(self)._update
        self._create(self._side, self._volume)
        if self._order is not None:
            self.orderBook.process(self._order)
        
    def _dispose(self):
        if self._order is not None:
            self._volume = self.volume
            self.orderBook.process(request.Cancel(self._order))
            self._order = None
            
    def _create(self, side, volume):
        price = self._price()
        #print price, self._volume
        if price is not None and self._volume > 0:
            self._order = Limit(self._side, price, self._volume)
            self._order.owner = self
        
    def _update(self, dummy):
        self._dispose() # we should resend the order only when the previous is cancelled
        self._create(self.side, self.volume)
        #print 'new price'
        if self._order is not None:
            self.orderBook.process(self._order)

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
    

    def cancel(self):
        """ Marks order as cancelled. Notifies the order book about it
        """
        self._price -= _(self)._update
        self._cancelled = True
        if self._order is None:
            self._onOrderCancelled(None)
        else:
            self._dispose()

    def _onOrderCancelled(self, order):
        if self._cancelled:
            self.owner._onOrderCancelled(self)
    
    def __hash__(self):
        return id(self)
