class VolumeLevels_Base(object):
    def get_queue(self):
        return self.__queue
    
    def set_queue(self, value):
        self.__queue = value
    
    queue = property(get_queue, set_queue)
    def get_volumeDelta(self):
        return self.__volumeDelta
    
    def set_volumeDelta(self, value):
        self.__volumeDelta = value
    
    volumeDelta = property(get_volumeDelta, set_volumeDelta)
    def get_volumeCount(self):
        return self.__volumeCount
    
    def set_volumeCount(self, value):
        self.__volumeCount = value
    
    volumeCount = property(get_volumeCount, set_volumeCount)
