class LastTradeVolume_Base(object):
    def get_queue(self):
        return self.__queue
    
    def set_queue(self, value):
        self.__queue = value
    
    queue = property(get_queue, set_queue)
class LastTradePrice_Base(object):
    def get_queue(self):
        return self.__queue
    
    def set_queue(self, value):
        self.__queue = value
    
    queue = property(get_queue, set_queue)
