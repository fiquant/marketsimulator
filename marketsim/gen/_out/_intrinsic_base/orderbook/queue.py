class BestPrice_Base(object):
    def get_queue(self):
        return self._back_queue
    
    def set_queue(self, value):
        self._back_queue = value
        self.on_queue_set(value)
    
    queue = property(get_queue, set_queue)
    def on_queue_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
