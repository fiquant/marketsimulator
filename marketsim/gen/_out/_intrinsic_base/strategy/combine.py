class Array_Base(object):
    def get_strategies(self):
        return self._back_strategies
    
    def set_strategies(self, value):
        self._back_strategies = value
        self.on_strategies_set(value)
    
    strategies = property(get_strategies, set_strategies)
    def on_strategies_set(self, value):
        pass
    
class Combine_Base(object):
    def get_A(self):
        return self._back_A
    
    def set_A(self, value):
        self._back_A = value
        self.on_A_set(value)
    
    A = property(get_A, set_A)
    def on_A_set(self, value):
        pass
    
    def get_B(self):
        return self._back_B
    
    def set_B(self, value):
        self._back_B = value
        self.on_B_set(value)
    
    B = property(get_B, set_B)
    def on_B_set(self, value):
        pass
    
