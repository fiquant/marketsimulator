class Canceller_Base(object):
    @property
    def cancellationIntervalDistr(self):
        return self.__cancellationIntervalDistr
    
    @cancellationIntervalDistr.setter
    def cancellationIntervalDistr(self, value):
        self.__cancellationIntervalDistr = value
    
