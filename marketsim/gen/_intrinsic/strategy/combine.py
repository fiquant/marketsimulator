from marketsim import event, _

from basic import Strategy

from marketsim.gen._out._intrinsic_base.strategy.combine import Combine_Base, Array_Base

class Combine_Impl(Strategy, Combine_Base):
    
    def __init__(self):
        Strategy.__init__(self)
        for s in [self.A, self.B]:
            event.subscribe(s.on_order_created, _(self)._send, self)

    def dispose(self):
        for s in [self.A, self.B]:
            s.dispose()

class Array_Impl(Strategy, Array_Base):

    def __init__(self):
        Strategy.__init__(self)
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self)._send, self)

    def dispose(self):
        for s in self.strategies:
            s.dispose()
