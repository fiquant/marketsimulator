class MinEpsilon_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_epsilon(self):
        return self._back_epsilon
    
    def set_epsilon(self, value):
        self._back_epsilon = value
        self.on_epsilon_set(value)
    
    epsilon = property(get_epsilon, set_epsilon)
    def on_epsilon_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
class MaxEpsilon_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_epsilon(self):
        return self._back_epsilon
    
    def set_epsilon(self, value):
        self._back_epsilon = value
        self.on_epsilon_set(value)
    
    epsilon = property(get_epsilon, set_epsilon)
    def on_epsilon_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
