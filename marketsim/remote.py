import random
from marketsim import scheduler, meta, mathutils

class Link(object):
    """ Ensures that sending packets via a link preserves their order
    """
    
    def __init__(self, latency=mathutils.constant(0.001), sched = None):
        """ Initializes the link with a latency function
        """
        self._scheduler = sched if sched else scheduler.current() 
        self.latency = latency
        self.reset()
        
    _properties = { "latency" : meta.function(args=(), rv=float) }
        
    def reset(self):
        self._lastT = 0
        
    def send(self, func):
        """ "Sends" data via link.
        After latency() moments of time 'func' will be called
        If there is another function that is scheduled for later time 
        we adjust action time of 'func' in order to preserve their order 
        """
        t = self._scheduler.currentTime + self.latency()
        if t < self._lastT:
            t = self._lastT
        self._lastT = t 
        self._scheduler.schedule(t, func)

class TwoWayLink(object):
    
    def __init__(self, 
                 up = Link(), 
                 down = Link()):
        
        self.up = up
        self.down = down
        
    _properties = { "up" : Link, "down" : Link }
