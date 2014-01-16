from marketsim import _,  meta, types, ops, mathutils, registry, event

class _RandomWalk_Impl(ops.Observable[float]):
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
    def _wakeUp(self, _):
        self.value += self.deltaDistr()
        self.fire(self)

    def __init__(self):
        ops.Observable[float].__init__(self)

        self.attributes = {"smooth":True}

        self._timer = event.Every(self.intervalDistr)
        event.subscribe(self._timer, _(self)._wakeUp, self)
        
        self.reset()
        
    _internals = ['_timer']
        
    def reset(self):
        self.value = self.initialValue
        
    def schedule(self):
        self._timer.schedule()

    def __call__(self):
        return self.value