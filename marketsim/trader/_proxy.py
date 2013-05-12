from marketsim import types, Event

class SASM_Proxy(object):
    
    def __init__(self):
        
        self._impl = None
        
        self.on_order_sent = Event()
        self.on_traded = Event()
        self._alias = ["$(Trader)"]
        
    def bind(self, impl):
        if not self._impl or not impl:
            if self._impl: 
                self._impl.on_order_sent -= self.on_order_sent
                self._impl.on_traded -= self.on_traded
            self._impl = impl
            if self._impl:
                self._impl.on_order_sent += self.on_order_sent
                self._impl.on_traded += self.on_traded
        else:
            assert self._impl == impl
        
    @property
    def running(self):
        assert self._impl
        return self._impl.running
    
    def run(self):
        assert self._impl
        self._impl.run()
    
    def stop(self):
        assert self._impl
        self._impl.stop()
        
    def reset(self):   
        assert self._impl
        self._impl.reset()
        
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
        assert self._impl
        return self._impl.orderBook
    
    @orderBook.setter
    def orderBook(self, newvalue):
        assert self._impl
        self._impl.orderBook = newvalue
