class Canceller_Base(object):
    def get_cancellationIntervalDistr(self):
        return self.__cancellationIntervalDistr
    
    def set_cancellationIntervalDistr(self, value):
        self.__cancellationIntervalDistr = value
    
    cancellationIntervalDistr = property(get_cancellationIntervalDistr, set_cancellationIntervalDistr)
