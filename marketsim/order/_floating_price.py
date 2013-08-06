from marketsim import request, _, event, Event, types
from marketsim.types import *

from _limit import Limit

import _meta
import _base

class FloatingPrice(_meta.Base, _base.HasPrice): 
    """ Meta order controlling price of the underlying order
        When price changes it cancels underlying order and resends it with changed price
        For the moment we work only on limit orders but this mecanism might be extented to any persistent order
    """
    
    def __init__(self, side, price, volume, owner = None):
        _meta.Base.__init__(self, side, volume, owner)
        self.price = None
        self._order = None
        self._priceGenerator = price
        event.subscribe(self._priceGenerator, _(self)._update, self)
        
    _internals = ['_priceGenerator']

    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self._update(None)
        
    def _dispose(self):
        if self._order is not None:
            self.orderBook.process(request.Cancel(self._order))
            self._order = None
            
    def _create(self):
        self.price = self._priceGenerator()
        if self.price is not None:
            #print side, price, volume
            self._order = self.send(Limit(self.side, self.price, self.volumeUnmatched))
        
    def _update(self, dummy):
        self._dispose() 
        self._create()

    def __str__(self):
        if self._order is not None:
            Base.__str__()
        else:
            return "FloatingPrice"

    def __repr__(self):
        return self.__str__()

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
            
    def onOrderMatched(self, order, price, volume):
        self.onMatchedWith(price, volume)