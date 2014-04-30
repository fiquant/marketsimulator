class Canceller_Base(object):
    def get_cancellationIntervalDistr(self):
        return self._back_cancellationIntervalDistr
    
    def set_cancellationIntervalDistr(self, value):
        self._back_cancellationIntervalDistr = value
        self.on_cancellationIntervalDistr_set(value)
    
    cancellationIntervalDistr = property(get_cancellationIntervalDistr, set_cancellationIntervalDistr)
    def on_cancellationIntervalDistr_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
