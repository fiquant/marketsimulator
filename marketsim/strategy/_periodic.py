from marketsim import (registry, meta, _, types, Side, mathutils, order, 
                       Event, event, ops, scheduler)
from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper2

class _Periodic_Impl(Strategy):    
    
    def __init__(self):                
        """ Runs generic periodic two side strategy 
        trader - single asset single market trader
        params.eventGen -- event that initiates strategy work
        params.sideFunc -- function '() -> Side option' that calculates side of order to create
        params.volumeFunc -- function '() -> Volume' calculating volume of order to create
        params.orderFactory -- function 'Side -> Volume -> IOrder' instantiating orders
        """        
        Strategy.__init__(self)
        event.subscribe(self.eventGen, _(self)._wakeUp, self)
        
    def __repr__(self):
        return ("Periodic(\n\t" + repr(self.orderFactory) + ",\n\t"
                                + repr(self.eventGen) + ",\n\t"
                                + repr(self.volumeFunc) + ",\n\t"
                                + repr(self.sideFunc) + ")" )
        
    def _wakeUp(self, _):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        side = self.sideFunc()
        if side <> None:
            volume = int(self.volumeFunc())
            if volume > 0:
                # create order given side and parameters
                order = self.orderFactory(side)(volume)
                # send order to the order book
                self._trader.send(order)

exec  wrapper2("Periodic", 
             """ Generic periodic strategy that wakes up on events given by *eventGen*, 
                 chooses side of order to create using *sideFunc* and its volume by *volumeFunc*,
                 creates an order via *orderFactory* and sends the order to the market using its trader
             
                 Parameters:
                 
                     |orderFactory|
                         order factory function (default: order.Limit.T)
                         
                     |eventGen|
                         Event source making the strategy to wake up
                         
                     |volumeFunc|
                         defines volumes of orders to create 
                         (default: exponential distribution with |lambda| = 1)
                         
                     |sideFunc|
                         function choosing side of order to create (default: randomSide)
                         
             """,
              [('orderFactory',         'order.MarketFactory',                  'Side -> Volume -> IOrder'),
               ('eventGen',             'None',                                 'Event'),
               ('volumeFunc',           'mathutils.rnd.expovariate(1.)',        '() -> Volume'),
               ('sideFunc',             'ops.constant(Side.Sell)',              '() -> Side')], register=False)

class _Periodic2_Impl(Strategy):    
     
    def __init__(self):                
        Strategy.__init__(self)
        event.subscribe(self.eventGen, _(self)._wakeUp, self)
         
    def __repr__(self):
        return "Periodic(%s, %s)" % (self.eventGen, self.orderFactory)
         
    def _wakeUp(self, _):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        order = self.orderFactory()
        # send order to the order book
        if order is not None:
            self._trader.send(order)
 
exec  wrapper2("Periodic2", 
             """ Generic periodic strategy that wakes up on events given by *eventGen*, 
                 creates an order via *orderFactory* and sends the order to the market using its trader
              
                 Parameters:
                  
                     |orderFactory|
                         order factory function (default: order.Limit.T)
                          
                     |eventGen|
                         Event source making the strategy to wake up
                          
             """,
              [('orderFactory',         'order.factory.Market',                 'types.IOrderFactory'),
               ('eventGen',             'scheduler.Timer(ops.constant(1.))',    'Event')], register=False)
