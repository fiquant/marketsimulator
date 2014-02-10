from marketsim import types,  event

class Base(object):
    
    def bind(self, context):
        self._trader = context.trader
        self._scheduler = context.world
        
    @property
    def trader(self):
        return self._trader

class Strategy(Base, types.ISingleAssetStrategy):
    
    def __init__(self):
        Base.__init__(self)
        self.on_order_created = event.Event()

    def _send(self, order, unused = None):
        self.on_order_created.fire(order, self)

    @property
    def orderBook(self):
        return self.trader.orderBook
        
        

class MultiAssetStrategy(Base, types.IMultiAssetStrategy):
    
    def __init__(self):
        Base.__init__(self)
        self.on_order_created = event.Event()

class _Empty_Impl(Strategy):
    pass