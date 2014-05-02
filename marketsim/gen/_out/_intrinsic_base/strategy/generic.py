class Generic_Base(object):
    def get_orderFactory(self):
        return self._back_orderFactory
    
    def set_orderFactory(self, value):
        self._back_orderFactory = value
        self.on_orderFactory_set(value)
    
    orderFactory = property(get_orderFactory, set_orderFactory)
    def on_orderFactory_set(self, value):
        pass
    
    def get_eventGen(self):
        return self._back_eventGen
    
    def set_eventGen(self, value):
        self._back_eventGen = value
        self.on_eventGen_set(value)
    
    eventGen = property(get_eventGen, set_eventGen)
    def on_eventGen_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
