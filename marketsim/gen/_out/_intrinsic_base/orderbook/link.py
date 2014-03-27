class TwoWayLink_Base(object):
    def get_up(self):
        return self.__up
    
    def set_up(self, value):
        self.__up = value
    
    up = property(get_up, set_up)
    def get_down(self):
        return self.__down
    
    def set_down(self, value):
        self.__down = value
    
    down = property(get_down, set_down)
class Link_Base(object):
    def get_latency(self):
        return self.__latency
    
    def set_latency(self, value):
        self.__latency = value
    
    latency = property(get_latency, set_latency)
