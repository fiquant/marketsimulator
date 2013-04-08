import random
from marketsim import Method, Event, meta, types, mathutils
from marketsim.scheduler import Timer

class RandomWalk(types.IObservable):
    """ A discrete signal with user-defined increments   
    """
    def _wakeUp_impl(self, _):
        self.value += self.deltaDistr()
        self.on_changed.fire(self)

    def __init__(self,
                 initialValue=0,
                 deltaDistr=mathutils.rnd.normalvariate(0.,1.),
                 intervalDistr=mathutils.rnd.expovariate(1.),
                 label=None):
        """ Initializes a signal
        initialValue - initial value of the signal (default: 0)
        deltaDistr - increment function (default: normal distribution with \mu=0, \sigma=1)
        intervalDistr - defines intervals between signal updates
        """
        self.label = label if label is not None else "#"+str(id(self))
        
        self.initialValue = initialValue
        self.attributes = {"smooth":True}
        self.deltaDistr = deltaDistr
        self.intervalDistr = intervalDistr
        self.on_changed = Event()
        wakeUp = Method(self, '_wakeUp_impl')
            
        if '_timer' in dir(self):
            self._timer.unadvise(wakeUp)

        self._timer = Timer(self.intervalDistr)
        self._timer.advise(wakeUp)
        
        self.reset()
        
    _properties = { 'initialValue' : float, 
                    'deltaDistr'   : meta.function((), float), 
                    'intervalDistr': meta.function((), float)}
        
    def reset(self):
        self.value = self.initialValue
        
    def schedule(self):
        self._timer.schedule()

    def advise(self, listener):
        """ Subscribes 'listener' to value changed events 
        """
        self.on_changed += listener
        
    def unadvise(self, listener):
        self.on_changed -= listener
