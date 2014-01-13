from marketsim import (event, _, types, ops, registry)

class _BreaksAtChanges_Impl(ops.Observable[float]):
    
    def __init__(self):
        ops.Observable[float].__init__(self)
        self._value = None
        event.subscribe(self.source, _(self)._clean, self)
        
    def bind(self, ctx):
        self._scheduler = ctx.world
    
    def _clean(self, dummy):
        self._setup(None)
        self._scheduler.async(_(self, self.source())._setup)
        
    def _setup(self, x):
        self._value = x
        self.fire(self)
    
    def __call__(self):
        return self._value
