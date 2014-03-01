from marketsim import event, _

import fold


class Min_Impl(fold.Last):
    
    def __init__(self):
        event.subscribe(self.source, _(self)._update, self)
        self.reset()

    @property
    def source(self):
        return self.x.source
        
    def reset(self):
        import blist
        self._levels = blist.sorteddict()
        self._x = None
    
    def at(self, t):
        p = self._levels.keys()[0] if len(self._levels) > 0 else None
        x = self._x
        if p is not None:
            if x is not None:
                return min(p,x)
            return p
        return x
         
    def _remove(self, x):
        self._levels[x] -= 1
        if self._levels[x] == 0:
            del self._levels[x]
        self.fire(self)
    
    def update(self, t, x):
        if x is not None and (self._x is None or x < self._x):
            if x not in self._levels:
                self._levels[x] = 0
            self._levels[x] += 1 
            self._scheduler.scheduleAfter(self.x.timeframe, _(self, x)._remove)
        self._x = x
        self.fire(self)
        
class Max_Impl(fold.Last):
    
    def __init__(self):
        event.subscribe(self.source, _(self)._update, self)
        self.reset()
        
    @property
    def source(self):
        return self.x.source

    def reset(self):
        import blist
        self._levels = blist.sorteddict()
        self._x = None
    
    def at(self, t):
        p = -self._levels.keys()[0] if len(self._levels) > 0 else None
        x = self._x
        if p is not None:
            if x is not None:
                return max(p,x)
            return p
        return x
         
    def _remove(self, x):
        self._levels[-x] -= 1
        if self._levels[-x] == 0:
            del self._levels[-x]
        self.fire(self)
    
    def update(self, t, x):
        if x is not None and (self._x is None or x > self._x):
            if -x not in self._levels:
                self._levels[-x] = 0
            self._levels[-x] += 1 
            self._scheduler.scheduleAfter(self.x.timeframe, _(self, x)._remove)
        self._x = x
        self.fire(self)
        
    
    