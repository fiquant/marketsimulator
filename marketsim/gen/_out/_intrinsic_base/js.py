class Graph_Base(object):
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
    
