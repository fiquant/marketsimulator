from marketsim import meta, types, registry

from _basic import Strategy
from _wrap import wrapper2
from _lp_side import LiquidityProviderSide

class _StrategyArray_Impl(Strategy):
    
    def dispose(self):
        for s in self.strategies:
            s.dispose()

    def suspend(self, flag):
        Strategy.suspend(self, flag)
        for s in self.strategies:
            s.suspend(flag)

    @property
    def suspended(self):
        for s in self.strategies:
            assert s.suspended == self._suspended
        return Strategy.suspended(self)
    
exec wrapper2('StrategyArray', "", [('strategies', '[LiquidityProviderSide()]', 'meta.listOf(types.IStrategy)')])
