import random
from marketsim import Event
from marketsim.scheduler import Timer

class RandomWalk(object):
    """ A discrete signal with user-defined increments   
    """

    def __init__(self,
                 initialValue=0,
                 deltaDistr=(lambda: random.normalvariate(0.,1.)),
                 intervalDistr=(lambda: random.expovariate(1.)),
                 label=None):
        """ Initializes a signal
        initialValue - initial value of the signal (default: 0)
        deltaDistr - increment function (default: normal distribution with \mu=0, \sigma=1)
        intervalDistr - defines intervals between signal updates
        """
        self.label = label if label is not None else "#"+str(id(self))
        
        self._initialValue = initialValue
        self.attributes = {"smooth":True}
        self._deltaDistr = deltaDistr
        self._intervalDistr = intervalDistr
        self.on_changed = Event()
        def wakeUp(_):
            self.value += self._deltaDistr()
            self.on_changed.fire(self)
            
        if '_timer' in dir(self):
            self._timer.unadvise(wakeUp)

        self._timer = Timer(self._intervalDistr)
        self._timer.advise(wakeUp)
        
        self.reset()
        
    def reset(self):
        self.value = self._initialValue

    def advise(self, listener):
        """ Subscribes 'listener' to value changed events 
        """
        self.on_changed += listener
