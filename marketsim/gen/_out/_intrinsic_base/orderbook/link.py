class TwoWayLink_Base(object):
    def get_up(self):
        return self._back_up
    
    def set_up(self, value):
        self._back_up = value
        self.on_up_set(value)
    
    up = property(get_up, set_up)
    def on_up_set(self, value):
        pass
    
    def get_down(self):
        return self._back_down
    
    def set_down(self, value):
        self._back_down = value
        self.on_down_set(value)
    
    down = property(get_down, set_down)
    def on_down_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Link_Base(object):
    def get_latency(self):
        return self._back_latency
    
    def set_latency(self, value):
        self._back_latency = value
        self.on_latency_set(value)
    
    latency = property(get_latency, set_latency)
    def on_latency_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
