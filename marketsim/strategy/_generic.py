from marketsim import (registry, meta, _, types, Side, mathutils, order, 
                       Event, event, ops, scheduler)
from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper2

class _Generic_Impl(Strategy):    
     
    def __init__(self):                
        Strategy.__init__(self)
        event.subscribe(self.eventGen, _(self)._wakeUp, self)
         
    def __repr__(self):
        return "Generic(%s, %s)" % (self.eventGen, self.orderFactory)
         
    def _wakeUp(self, _):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        order = self.orderFactory()
        # send order to the order book
        if order is not None:
            self._send(order)
 
exec  wrapper2("Generic", 
             """ Generic strategy that wakes up on events given by *eventGen*, 
                 creates an order via *orderFactory* and sends the order to the market using its trader
              
                 Parameters:
                  
                     |orderFactory|
                         order factory function (default: order.Limit.T)
                          
                     |eventGen|
                         Event source making the strategy to wake up
                          
             """,
              [('orderFactory',         'order.factory.Market()',               'types.IOrderGenerator'),
               ('eventGen',             'scheduler.Timer(ops.constant(1.))',    'Event')])
