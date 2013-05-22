from marketsim import registry, meta, bind, types, Side, mathutils, order, Event
from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper2

@registry.expose(alias = ['Random side'])
@meta.sig(args=(), rv=Side)
def randomSide():
    return types.Side.byId(mathutils.rnd.randint(0,1)())

class _Generic_Impl(Strategy):    
    
    def __init__(self):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        params.eventGen -- event that initiates strategy work
        params.sideFunc -- function '() -> Side option' that calculates side of order to create
        params.volumeFunc -- function '() -> Volume' calculating volume of order to create
        params.orderFactory -- function 'Side -> Volume -> IOrder' instantiating orders
        """        
        Strategy.__init__(self, None)
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        # start listening calls from eventGen
        self._eventGen.advise(self._wakeUp)
        
    @property
    def _eventGen(self):
        return self.eventGen
    
    @property
    def _sideFunc(self):
        return self.sideFunc
    
    @property
    def _volumeFunc(self):
        return self.volumeFunc
    
    @property
    def _orderFactory(self):
        return self.orderFactory
        
    def reset(self):
        self._eventGen.schedule()
        
    def dispose(self):
        self._eventGen.unadvise(self._wakeUp)

    def _wakeUp_impl(self, _):
        if self._suspended:
            return
        # determine side and parameters of an order to create
        side = self._sideFunc()
        if side <> None:
            volume = int(self._volumeFunc())
            if volume > 0:
                # create order given side and parameters
                order = self._orderFactory(side)(volume)
                # send order to the order book
                self._trader.send(order)

exec  wrapper2("Generic", 
             """ Generic strategy that wakes up on events given by *eventGen*, 
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
               ('sideFunc',             'randomSide',                           '() -> Side')], register=False)
