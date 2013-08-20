from marketsim import (registry, types, _, ops, event)

from .._basic import Strategy
from .._wrap import wrapper2

from ..side import FundamentalValue


class _Suspendable_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        event.subscribe(self.inner.on_order_created, _(self).send, self)
        
    @property
    def suspended(self):
        return not self.predicate()
    
    def send(self, order, source):
        if self.predicate():
            self._send(order)

exec wrapper2("Suspendable", 
             "",
             [
              ('inner',     'FundamentalValue()', 'types.ISingleAssetStrategy'),
              ('predicate', 'ops.constant(True)', 'types.IFunction[bool]')
             ], register=False)

