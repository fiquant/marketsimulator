import random
from marketsim import event, request, _, types

from marketsim.gen._out._intrinsic_base.strategy.canceller import Canceller_Base

class Canceller_Impl(Canceller_Base):
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
        from marketsim.gen._out.trader._singleproxy import SingleProxy
        from marketsim.gen._out.orderbook._oftrader import OfTrader
        self._elements = []
        self._eventGen = event.Every(self.cancellationIntervalDistr)
        self._myTrader = SingleProxy()
        self._book = OfTrader(self._myTrader)
        self.on_order_created = event.Event()
        
    _internals = ['_myTrader']

    def bind(self, ctx):
        event.subscribe(self._myTrader.on_order_sent, _(self).process, self, ctx)
        event.subscribe(self._eventGen, _(self)._wakeUp, self, ctx)
        
    def process(self, order):
        """ Puts 'order' to future cancellation list
        """
        self._elements.append(order)
