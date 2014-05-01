from marketsim import types,  event

from marketsim.gen._out._intrinsic_base.strategy.basic import Empty_Base

class Base(object):

    def bind_impl(self, context):
        if not hasattr(self, '_trader'):
            self._trader = context.trader

        if not hasattr(self, '_scheduler'):
            self._scheduler = context.world

    def reset(self):
        pass

    @property
    def trader(self):
        return self._trader

class Strategy(Base):
    
    def __init__(self):
        Base.__init__(self)
        self.on_order_created = event.Event()

    def _send(self, order, unused = None):
        self.on_order_created.fire(order, self)

    @property
    def orderBook(self):
        return self.trader.orderBook
        
        

class MultiAssetStrategy(Base):
    
    def __init__(self):
        Base.__init__(self)
        self.on_order_created = event.Event()

class Empty_Impl(Strategy, Empty_Base):
    pass