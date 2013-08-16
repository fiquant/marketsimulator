from marketsim import types, registry

class Base(object):
    
    def __init__(self):
        self._suspended = False
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, s=True):
        self._suspended = s
        
    def bind(self, context):
        self._trader = context.trader
        self._orderProcessor = context.orderProcessor
        self._scheduler = context.world
        
    @property
    def orderProcessor(self):
        return self._orderProcessor
        
    @property
    def trader(self):
        return self._trader

class Strategy(Base, types.ISingleAssetStrategy):
    
    def __init__(self):
        Base.__init__(self)

    def send(self, order):
        self.orderProcessor.send(order)    
        

class MultiAssetStrategy(Base, types.IMultiAssetStrategy):
    
    def __init__(self):
        Base.__init__(self)

@registry.expose(['Empty']) 
class Empty(Strategy):
    pass