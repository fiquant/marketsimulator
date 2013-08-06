from marketsim import request, _, event, Event, types
from marketsim.types import *

from _limit import Limit

import _meta
import _base

class FloatingPrice(_meta.OwnsSingleOrder, _base.HasPrice): 
    """ Meta order controlling price of the underlying order
        When price changes it cancels underlying order and resends it with changed price
        For the moment we work only on limit orders but this mecanism might be extented to any persistent order
    """
    
    def __init__(self, side, price, volume, owner = None):
        _meta.OwnsSingleOrder.__init__(self, side, volume, owner)
        self.price = None
        self._priceGenerator = price
        event.subscribe(self._priceGenerator, _(self)._update, self)
        
    _internals = ['_priceGenerator']

    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self._update(None)
        
    def _create(self):
        self.price = self._priceGenerator()
        if self.price is not None:
            self.send(Limit(self.side, self.price, self.volumeUnmatched))
        
    def _update(self, dummy):
        self._dispose() 
        self._create()

