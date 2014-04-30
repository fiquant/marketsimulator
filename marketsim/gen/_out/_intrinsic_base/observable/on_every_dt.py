class OnEveryDt_Base(object):
    def get_x(self):
        return self._back_x
    
    def set_x(self, value):
        self._back_x = value
        self.on_x_set(value)
    
    x = property(get_x, set_x)
    def on_x_set(self, value):
        pass
    
    def get_dt(self):
        return self._back_dt
    
    def set_dt(self, value):
        self._back_dt = value
        self.on_dt_set(value)
    
    dt = property(get_dt, set_dt)
    def on_dt_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
