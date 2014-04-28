from marketsim import (event, _)

from marketsim.gen._out._intrinsic_base.observable.breaks_at_changes import BreaksAtChanges_Base

class BreaksAtChanges_Impl(BreaksAtChanges_Base):
    
    def __init__(self):
        self._value = None
        event.subscribe(self.source, _(self)._clean, self)

    def bind_impl(self, ctx):
        if not hasattr(self, '_scheduler'):
            self._scheduler = ctx.world

    def _clean(self, dummy):
        self._setup(None)
        self._scheduler.async(_(self, self.source())._setup)
        
    def _setup(self, x):
        self._value = x
        self.fire(self)
    
    def __call__(self):
        return self._value
