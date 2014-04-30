class VolumeLevels_Base(object):
    def get_queue(self):
        return self._back_queue
    
    def set_queue(self, value):
        self._back_queue = value
        self.on_queue_set(value)
    
    queue = property(get_queue, set_queue)
    def on_queue_set(self, value):
        pass
    
    def get_volumeDelta(self):
        return self._back_volumeDelta
    
    def set_volumeDelta(self, value):
        self._back_volumeDelta = value
        self.on_volumeDelta_set(value)
    
    volumeDelta = property(get_volumeDelta, set_volumeDelta)
    def on_volumeDelta_set(self, value):
        pass
    
    def get_volumeCount(self):
        return self._back_volumeCount
    
    def set_volumeCount(self, value):
        self._back_volumeCount = value
        self.on_volumeCount_set(value)
    
    volumeCount = property(get_volumeCount, set_volumeCount)
    def on_volumeCount_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
