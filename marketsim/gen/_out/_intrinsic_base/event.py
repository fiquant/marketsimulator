class After_Base(object):
    def get_delay(self):
        return self._back_delay
    
    def set_delay(self, value):
        self._back_delay = value
        self.on_delay_set(value)
    
    delay = property(get_delay, set_delay)
    def on_delay_set(self, value):
        pass
    
class Every_Base(object):
    def get_intervalFunc(self):
        return self._back_intervalFunc
    
    def set_intervalFunc(self, value):
        self._back_intervalFunc = value
        self.on_intervalFunc_set(value)
    
    intervalFunc = property(get_intervalFunc, set_intervalFunc)
    def on_intervalFunc_set(self, value):
        pass
    
