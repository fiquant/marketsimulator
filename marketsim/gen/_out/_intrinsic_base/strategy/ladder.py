class OneSide_Base(object):
    def get_orderFactory(self):
        return self._back_orderFactory
    
    def set_orderFactory(self, value):
        self._back_orderFactory = value
        self.on_orderFactory_set(value)
    
    orderFactory = property(get_orderFactory, set_orderFactory)
    def on_orderFactory_set(self, value):
        pass
    
    def get_initialSize(self):
        return self._back_initialSize
    
    def set_initialSize(self, value):
        self._back_initialSize = value
        self.on_initialSize_set(value)
    
    initialSize = property(get_initialSize, set_initialSize)
    def on_initialSize_set(self, value):
        pass
    
    def get_side(self):
        return self._back_side
    
    def set_side(self, value):
        self._back_side = value
        self.on_side_set(value)
    
    side = property(get_side, set_side)
    def on_side_set(self, value):
        pass
    
