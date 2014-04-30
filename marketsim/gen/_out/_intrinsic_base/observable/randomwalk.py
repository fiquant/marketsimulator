class RandomWalk_Base(object):
    def get_initialValue(self):
        return self._back_initialValue
    
    def set_initialValue(self, value):
        self._back_initialValue = value
        self.on_initialValue_set(value)
    
    initialValue = property(get_initialValue, set_initialValue)
    def on_initialValue_set(self, value):
        pass
    
    def get_deltaDistr(self):
        return self._back_deltaDistr
    
    def set_deltaDistr(self, value):
        self._back_deltaDistr = value
        self.on_deltaDistr_set(value)
    
    deltaDistr = property(get_deltaDistr, set_deltaDistr)
    def on_deltaDistr_set(self, value):
        pass
    
    def get_intervalDistr(self):
        return self._back_intervalDistr
    
    def set_intervalDistr(self, value):
        self._back_intervalDistr = value
        self.on_intervalDistr_set(value)
    
    intervalDistr = property(get_intervalDistr, set_intervalDistr)
    def on_intervalDistr_set(self, value):
        pass
    
    def get_name(self):
        return self._back_name
    
    def set_name(self, value):
        self._back_name = value
        self.on_name_set(value)
    
    name = property(get_name, set_name)
    def on_name_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
