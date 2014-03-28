class Suspendable_Base(object):
    def get_inner(self):
        return self._back_inner
    
    def set_inner(self, value):
        self._back_inner = value
        self.on_inner_set(value)
    
    inner = property(get_inner, set_inner)
    def on_inner_set(self, value):
        pass
    
    def get_predicate(self):
        return self._back_predicate
    
    def set_predicate(self, value):
        self._back_predicate = value
        self.on_predicate_set(value)
    
    predicate = property(get_predicate, set_predicate)
    def on_predicate_set(self, value):
        pass
    
