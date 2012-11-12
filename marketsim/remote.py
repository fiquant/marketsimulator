import random
from marketsim.scheduler import world

class Link(object):
    """ Ensures that sending packets via a link preserves their order
    """
    
    def __init__(self, latency):
        """ Initializes the link with a latency function
        """
        self._latency = latency
        self._lastT = 0
        
    def send(self, func):
        """ "Sends" data via link.
        After latency() moments of time 'func' will be called
        If there is another function that is scheduled for later time 
        we adjust action time of 'func' in order to preserve their order 
        """
        t = world.currentTime + self._latency()
        if t < self._lastT:
            t = self._lastT
        self._lastT = t 
        world.schedule(t, func)

class TwoWayLink(object):
    
    def __init__(self, 
                 latencyUp = lambda: 0.001 * random.lognormvariate(0.,1.), 
                 latencyDown = lambda: 0.001 * random.lognormvariate(0.,1.)):
        
        self.up = Link(latencyUp)
        self.down = Link(latencyDown)
