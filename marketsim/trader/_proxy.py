from marketsim import types, Event

# TODO: inheritance like:
#        Proxy -> ITraderOpt
#        SingleAsset -> ITrader -> ITraderOpt

class Base(object):

    def __init__(self):
        
        self._impl = None
        
        self.on_order_sent = Event()
        self.on_traded = Event()
        
    def _bind(self, impl):
        assert self._impl is  None
        self._impl = impl
        self._impl.on_order_sent += self.on_order_sent.fire
        self._impl.on_traded += self.on_traded.fire

    def _new_property_changed_listener_added(self, propname):
        pass
                
    _properties = {}
    
    @property
    def PnL(self):
        assert self._impl
        return self._impl.PnL
    
    @PnL.setter
    def PnL(self, value):
        assert self._impl
        self._impl.PnL = value
        
    @property
    def label(self):
        assert self._impl
        return self._impl.label
    
    @label.setter
    def label(self, value):
        assert self._impl
        self._impl.label = value

    @property 
    def strategy(self):
        assert self._impl
        return self._impl.strategy
    
    @strategy.setter
    def strategy(self, value):
        assert self._impl
        self._impl.strategy = value
        
class SASM_ProxyBase(Base, types.ISingleAssetTrader):
    
    def __init__(self):
        Base.__init__(self)
        self._alias = ["$(Trader)"]

    @property
    def amount(self):
        assert self._impl
        return self._impl.amount
    
    @amount.setter
    def amount(self, value):
        assert self._impl
        self._impl.amount = value
                    
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
        
class MultiProxy(Base, types.ITrader):
    
    def __init__(self):
        Base.__init__(self)
        self._alias = ['$(MultiTrader)']
        
    def bind(self, context):
        self._bind(context.trader)

    @property
    def traders(self):
        assert self._impl
        return self._impl.traders
    
    @traders.setter
    def traders(self, value):
        assert self._impl
        self.traders = value

class SASM_Proxy(SASM_ProxyBase):

    def bind(self, context):
        self._bind(context.trader)
            
class SASM_ParentProxy(SASM_ProxyBase):
    
    def bind(self, context):
        self._bind(context.parentTrader)