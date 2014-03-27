class TwoWayLink_Base(object):
    @property
    def up(self):
        return self.__up
    
    @up.setter
    def up(self, value):
        self.__up = value
    
    @property
    def down(self):
        return self.__down
    
    @down.setter
    def down(self, value):
        self.__down = value
    
class Link_Base(object):
    @property
    def latency(self):
        return self.__latency
    
    @latency.setter
    def latency(self, value):
        self.__latency = value
    
