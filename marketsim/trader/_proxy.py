from marketsim import types, Event

class SASM_ProxyBase(object):
    
    def __init__(self):
        
        self._impl = None
        
        self.on_order_sent = Event()
        self.on_traded = Event()
        self._alias = ["$(Trader)"]
        
    def _bind(self, impl):
        assert self._impl is  None
        self._impl = impl
        self._impl.on_order_sent += self.on_order_sent.fire
        self._impl.on_traded += self.on_traded.fire

    def _new_property_changed_listener_added(self, propname):
        pass
                
    _properties = {}
    
    _types = [types.ISingleAssetTrader]
    
    @property
    def PnL(self):
        assert self._impl
        return self._impl.PnL
    
    @PnL.setter
    def PnL(self, value):
        assert self._impl
        self._impl.PnL = value
        
    def send(self, order):
        assert self._impl
        self._impl.send(order)
        
    @property
    def label(self):
        assert self._impl
        return self._impl.label
    
    @label.setter
    def label(self, value):
        assert self._impl
        self._impl.label = value

    @property
    def amount(self):
        assert self._impl
        return self._impl.amount
    
    @amount.setter
    def amount(self, value):
        assert self._impl
        self._impl.amount = value
        
    @property 
    def strategies(self):
        assert self._impl
        return self._impl.strategies
    
    @strategies.setter
    def strategies(self, value):
        assert self._impl
        self._impl.strategies = value
        
            
    @property
    def book(self): # obsolete
        assert self._impl
        return self._impl.orderBook
    
    @property
    def orderBook(self):
        return self._impl.orderBook if self._impl else None
    
    @orderBook.setter
    def orderBook(self, newvalue):
        assert self._impl
        self._impl.orderBook = newvalue

class SASM_Proxy(SASM_ProxyBase):

    def bind(self, context):
        self._bind(context.trader)
            
class SASM_ParentProxy(SASM_ProxyBase):
    
    def bind(self, context):
        self._bind(context.parentTrader)