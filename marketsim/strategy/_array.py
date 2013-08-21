from marketsim import event, meta, types, registry, _

from _basic import Strategy, Empty
from _wrap import wrapper2

class _Array_Impl(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        for s in self.strategies:
            event.subscribe(s.on_order_created, _(self)._send, self)
    
    def dispose(self):
        for s in self.strategies:
            s.dispose()

exec wrapper2('Array', "", [('strategies', '[Empty()]', 'meta.listOf(types.ISingleAssetStrategy)')])
