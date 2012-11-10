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

        self.on_changed = Event()
        
        self.label = label if label is not None else "#"+str(id(self))
        
        self.value = initialValue
        self.attributes = {"smooth":True}

        def wakeUp(_):
            self.value += deltaDistr()
            self.on_changed.fire(self)

        Timer(intervalDistr).advise(wakeUp)

    def advise(self, listener):
        """ Subscribes 'listener' to value changed events 
        """
        self.on_changed += listener
