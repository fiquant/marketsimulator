import random
from marketsim import _, Event, meta, types, mathutils, registry, scheduler, event

@registry.expose(['Random walk'])
class RandomWalk(types.Observable):
    """ A discrete signal with user-defined increments.
    
        Parameters:
        
        **initialValue** 
            initial value of the signal (default: 0)
            
        **deltaDistr**
            increment function (default: normal distribution with |mu| = 0, |sigma| = 1)
        
        **intervalDistr**
            defines intervals between signal updates
            (default: exponential distribution with |lambda| = 1)
    """
    _properties = { 'initialValue' : float, 
                    'deltaDistr'   : types.IFloatFunction, 
                    'intervalDistr': types.IFloatFunction }
        

    def _wakeUp(self, _):
        self.value += self.deltaDistr()
        self.fire(self)

    def __init__(self,
                 initialValue=0,
                 deltaDistr=mathutils.rnd.normalvariate(0.,1.),
                 intervalDistr=mathutils.rnd.expovariate(1.),
                 label=None):
        super(RandomWalk, self).__init__()
        self.label = label if label is not None else "#"+str(id(self))
        
        self.initialValue = initialValue
        self.attributes = {"smooth":True}
        self.deltaDistr = deltaDistr
        self.intervalDistr = intervalDistr
            
        self._timer = scheduler.Timer(self.intervalDistr)
        event.subscribe(self._timer, _(self)._wakeUp, self)
        
        self.reset()
        
    _internals = ['_timer']
        
    def reset(self):
        self.value = self.initialValue
        
    def schedule(self):
        self._timer.schedule()

    def __call__(self):
        return self.value