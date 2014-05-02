class currentScheduler_Base(object):
    pass
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Scheduler_Base(object):
    def get_currentTime(self):
        return self._back_currentTime
    
    def set_currentTime(self, value):
        self._back_currentTime = value
        self.on_currentTime_set(value)
    
    currentTime = property(get_currentTime, set_currentTime)
    def on_currentTime_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
