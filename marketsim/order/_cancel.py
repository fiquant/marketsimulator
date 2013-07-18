from marketsim import Event, scheduler, registry, ops, types, meta, bind, Side, _, event
from _base import Base
from _limit import LimitFactory

class Cancel(object):
    """ Cancels another order that can be for example a limit or an iceberg order
    """
    def __init__(self, orderToBeCancelled):
        self._toCancel = orderToBeCancelled
        self.on_matched = Event() # just dummy event. never called
        self.on_charged = Event()
        self.on_cancelled = Event()
        
    def charge(self, price):
        self.on_charge.fire(price)
        
    def processIn(self, orderBook):
        orderBook.cancelOrder(self._toCancel)
        
    def clone(self):
        return Cancel(self._toCancel)
    
    def copyTo(self, dest):
        assert dest._toCancel == self._toCancel

