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
    
    def __init__(self, pricevolume_factory, price, volume, owner = None):
        _meta.OwnsSingleOrder.__init__(self, pricevolume_factory.side(), volume, owner)
        self.price = None
        self._orderGenerator = pricevolume_factory(price, _(self)._volumeToTrade)
        event.subscribe(price, _(self)._update, self)
        
    def _volumeToTrade(self):
        return self.volumeUnmatched
 
    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self._update(None)
        
    def _create(self):
        self.send(self._orderGenerator())
        
    def _update(self, dummy):
        self._dispose() 
        self._create()

