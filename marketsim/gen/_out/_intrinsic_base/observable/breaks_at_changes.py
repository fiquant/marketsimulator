class BreaksAtChanges_Base(object):
    def get_source(self):
        return self._back_source
    
    def set_source(self, value):
        self._back_source = value
        self.on_source_set(value)
    
    source = property(get_source, set_source)
    def on_source_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
