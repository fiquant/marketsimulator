import collections

from marketsim import types, _, event, scheduler, ops, context

class CandleStick(collections.namedtuple("CandleStick", [
                                                     "open", "close",
                                                     "min", "max",
                                                     "mean", "stddev" 
                                     ])):
    
    pass

from _cma import CMA
from _stddev import StdDev

class CandleSticks(types.Observable[float]):
    
    def __init__(self, source, timeframe = 1.):
        types.Observable[float].__init__(self)
        self._source = source
        self._event = event.subscribe(source, _(self)._update, self)
        event.subscribe(scheduler.Timer(ops.constant(timeframe)), _(self)._flush, self)
        self.timeframe = timeframe
        self.reset()
        self._mean = CMA(source)
        self._stddev = StdDev(source)
        
    @property
    def source(self):
        return self._source
        
    @source.setter
    def source(self, value):
        self._source = value
        self._event.switchTo(value)
    
        
    @property
    def attributes(self):
        return {}
        
    _internals = ["_mean", '_stddev']
    _properties = { "source"    : types.IObservable[float], 
                    "timeframe" : float }
    
    def reset(self):
        self._last = None
        self._open = None
        self._min = None
        self._max = None
        self._close = None
    
    @property
    def label(self):
        return 'Candles(' + self.source.label + ')'   
    
    def _flush(self, _):
        last = CandleStick(self._open, self._close, 
                           self._min, self._max, 
                           self._mean(), self._stddev()) \
                if self._open is not None else None
        self.reset()
        self._last = last
        self.fire(self)                
    
    def _update(self, _):        
        x = self.source()
        if x is not None:
            if self._open is None:
                self._open = x
                self._max = x
                self._min = x
                context.reset(self._mean)
                context.reset(self._stddev)
            if self._min > x: self._min = x
            if self._max < x: self._max = x
            self._close = x

    def __call__(self):
        return self._last