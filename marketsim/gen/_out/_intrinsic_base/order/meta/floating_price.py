class Factory_Base(object):
    def get_proto(self):
        return self._back_proto
    
    def set_proto(self, value):
        self._back_proto = value
        self.on_proto_set(value)
    
    proto = property(get_proto, set_proto)
    def on_proto_set(self, value):
        pass
    
    def get_floatingPrice(self):
        return self._back_floatingPrice
    
    def set_floatingPrice(self, value):
        self._back_floatingPrice = value
        self.on_floatingPrice_set(value)
    
    floatingPrice = property(get_floatingPrice, set_floatingPrice)
    def on_floatingPrice_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
