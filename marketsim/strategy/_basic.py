from marketsim import types

class Strategy(types.IStrategy):
    
    def __init__(self, trader):
        self._suspended = False
        self._trader = trader
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, s=True):
        self._suspended = s
        
    def bind(self, context):
        self._trader = context.trader
        self._scheduler = context.world    
        
    @property
    def trader(self):
        return self._trader
   