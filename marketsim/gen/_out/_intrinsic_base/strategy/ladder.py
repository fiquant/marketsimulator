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
    
class StopLoss_Base(object):
    def get_inner(self):
        return self._back_inner
    
    def set_inner(self, value):
        self._back_inner = value
        self.on_inner_set(value)
    
    inner = property(get_inner, set_inner)
    def on_inner_set(self, value):
        pass
    
    def get_lossFactor(self):
        return self._back_lossFactor
    
    def set_lossFactor(self, value):
        self._back_lossFactor = value
        self.on_lossFactor_set(value)
    
    lossFactor = property(get_lossFactor, set_lossFactor)
    def on_lossFactor_set(self, value):
        pass
    
class Balancer_Base(object):
    def get_inner(self):
        return self._back_inner
    
    def set_inner(self, value):
        self._back_inner = value
        self.on_inner_set(value)
    
    inner = property(get_inner, set_inner)
    def on_inner_set(self, value):
        pass
    
    def get_maximalSize(self):
        return self._back_maximalSize
    
    def set_maximalSize(self, value):
        self._back_maximalSize = value
        self.on_maximalSize_set(value)
    
    maximalSize = property(get_maximalSize, set_maximalSize)
    def on_maximalSize_set(self, value):
        pass
    
class MarketMaker_Base(object):
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
    
