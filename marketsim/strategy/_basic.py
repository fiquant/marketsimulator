from marketsim import types, registry, Event

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
        self._scheduler = context.world
        
    @property
    def trader(self):
        return self._trader

class Strategy(Base, types.ISingleAssetStrategy):
    
    def __init__(self):
        Base.__init__(self)
        self.on_order_created = Event()

    def _send(self, order, unused = None):
        self.on_order_created.fire(order, self)

    @property
    def orderBook(self):
        return self.trader.orderBook
        
        

class MultiAssetStrategy(Base, types.IMultiAssetStrategy):
    
    def __init__(self):
        Base.__init__(self)
        self.on_order_created = Event()

@registry.expose(['Empty']) 
class Empty(Strategy):
    pass