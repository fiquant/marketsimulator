from marketsim import event, _

from basic import Strategy

class _Combine_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        for s in [self.A, self.B]:
            event.subscribe(s.on_order_created, _(self)._send, self)

    def dispose(self):
        for s in [self.A, self.B]:
            s.dispose()
