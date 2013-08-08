from marketsim import request, _, event, Event, types, ops
from marketsim.types import *

from _limit import Limit, PriceVolume_Factory

import _meta
import _base

class FloatingPrice(_meta.OwnsSingleOrder, _base.HasPrice): 
    """ Meta order controlling price of the underlying order
        When price changes it cancels underlying order and resends it with changed price
        For the moment we work only on limit orders but this mecanism might be extented to any persistent order
    """
    
    def __init__(self, proto, price):
        _meta.OwnsSingleOrder.__init__(self, proto.side, proto.volumeUnmatched)
        _base.HasPrice.__init__(self, proto.price)
        self._proto = proto
        self._priceFunc = price
        event.subscribe(price, _(self)._update, self)
        
    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self._update(None)
        
    def _update(self, dummy):
        self._dispose() 
        self.send(self._proto.With(price = self._priceFunc(), volume = self.volumeUnmatched))

