import random
from marketsim import bind, trader, scheduler, orderbook, mathutils, meta, registry, types, event
from marketsim.types import *
from _wrap import wrapper2

class _Canceller_Impl(object):
    """ Randomly cancels created orders in specific moments of time    
    """
    
    def choiceFunc(self, N):
        return random.randint(0, N-1)

    def _wakeUp_impl(self, _):
        # if we have orders to cancel
        while self._elements <> []:
            # choose an order
            N = len(self._elements)
            idx = self.choiceFunc(N)
            e = self._elements[idx]
            # if the order is invalid
            if e.empty or e.cancelled:
                # put the last order instead of it and repeat the procedure
                if e <> self._elements[-1]:
                    self._elements[idx] = self._elements[-1]
                # it converges since every time we pops an element from the queue
                self._elements.pop()
            else:
                # if order is valid, cancel it
                self._book.process(order.Cancel(e))
                return

    def __init__(self):

        # orders created by trader
        self._elements = []
        self.wakeUp = bind.Method(self, '_wakeUp_impl')
        self._eventGen = scheduler.Timer(self.cancellationIntervalDistr)
        myTrader = trader.SASM_Proxy()
        # start listening its orders sent
        myTrader.on_order_sent += bind.Method(self, 'process')
        self._book = orderbook.OfTrader(myTrader)
        event.subscribe(self._eventGen, self.wakeUp, self)
        
    def dispose(self):
        self._eventGen -= self.wakeUp
        
    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)

exec wrapper2("Canceller",
             "",
             [('cancellationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])
