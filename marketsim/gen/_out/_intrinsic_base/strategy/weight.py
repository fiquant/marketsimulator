class Identity_Base(object):
    def get_array(self):
        return self._back_array
    
    def set_array(self, value):
        self._back_array = value
        self.on_array_set(value)
    
    array = property(get_array, set_array)
    def on_array_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Score_Base(object):
    def get_trader(self):
        return self._back_trader
    
    def set_trader(self, value):
        self._back_trader = value
        self.on_trader_set(value)
    
    trader = property(get_trader, set_trader)
    def on_trader_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class ChooseTheBest_Base(object):
    def get_array(self):
        return self._back_array
    
    def set_array(self, value):
        self._back_array = value
        self.on_array_set(value)
    
    array = property(get_array, set_array)
    def on_array_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
