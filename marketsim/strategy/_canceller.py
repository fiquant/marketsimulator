import random
from marketsim import request, order, _, trader, scheduler, orderbook, mathutils, meta, registry, types, event
from marketsim.types import *
from _wrap import wrapper2

class _Canceller_Impl(types.ISingleAssetStrategy):
    """ Randomly cancels created orders in specific moments of time    
    """
    
    def choiceFunc(self, N):
        return random.randint(0, N-1)

    def _wakeUp(self, _):
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
                self._book.process(request.Cancel(e))
                return

    def __init__(self):

        # orders created by trader
        self._elements = []
        self._eventGen = scheduler.Timer(self.cancellationIntervalDistr)
        self._myTrader = trader.SingleProxy()
        self._book = orderbook.OfTrader(self._myTrader)
        
    _internals = ['_myTrader']

    def bind(self, ctx):
        event.subscribe(self._myTrader.on_order_sent, _(self).process, self, ctx)
        event.subscribe(self._eventGen, _(self)._wakeUp, self, ctx)
        
    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)

exec wrapper2("Canceller",
             "",
             [('cancellationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')])
