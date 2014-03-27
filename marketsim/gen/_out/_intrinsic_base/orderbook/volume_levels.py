class VolumeLevels_Base(object):
    @property
    def queue(self):
        return self.__queue
    
    @queue.setter
    def queue(self, value):
        self.__queue = value
    
    @property
    def volumeDelta(self):
        return self.__volumeDelta
    
    @volumeDelta.setter
    def volumeDelta(self, value):
        self.__volumeDelta = value
    
    @property
    def volumeCount(self):
        return self.__volumeCount
    
    @volumeCount.setter
    def volumeCount(self, value):
        self.__volumeCount = value
    
