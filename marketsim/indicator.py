from marketsim import Event, Side
from marketsim.scheduler import Timer, world
import math

def isIterable(x):
    return '__iter__' in dir(x)

def getLabel(x):
    return x.label if 'label' in dir(x) else "#"+str(id(x))
        

class IndicatorBase(object):
    
    def __init__(self, eventSource, dataSource, label, attributes = {}):
        
        self.on_changed = Event()
        self._label = label
        self.attributes = attributes

        def update(_):
            self._current = dataSource()
            if self._current is not None: # this should be removed into a separate filter
                self.on_changed.fire(self) 
        
        if not isIterable(eventSource):
            eventSource = [eventSource]
        
        for es in eventSource:
            es.advise(update)
            
        update(None)
        
    @property
    def label(self):
        return self._label
        
    def advise(self, listener):
        self.on_changed += listener
        
    @property
    def value(self):
        return self._current
    
def AssetPrice(book):
   
    return IndicatorBase(\
        [book.asks.on_best_changed, book.bids.on_best_changed], 
        lambda: book.price, "Price "+getLabel(book))

def BestPrice(book, side, label):
    
    queue = book.queue(side)

    return IndicatorBase(\
        [queue.on_best_changed], 
        lambda: queue.best.price if not queue.empty else None,
        label+getLabel(book))
    
def BidPrice(book):
    return BestPrice(book, Side.Buy, "BidPrice ")

def AskPrice(book):
    return BestPrice(book, Side.Sell, "AskPrice ")

def OnEveryDt(interval, source):
    
    return IndicatorBase([Timer(lambda: interval).on_timer], 
                         source, 
                         getLabel(source), 
                         {'smooth':True})


class ewma(object):
    
    def __init__(self, alpha):
        self._alpha = alpha
        self._avg = None
        
    @property 
    def value(self):
        return self._avg
        
    def at(self, t):
        return \
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self._alpha)**( t - self._lastTime)) \
            if self._avg is not None else None
    
    def derivativeAt(self, t):
        dt = t - self._lastTime
        return -(self._lastValue - self._avg)*math.log(1 - self._alpha)*(1 - self._alpha)**dt
        
    def update(self, time, value):
        self._avg = self.at(time) if self._avg is not None else value
        self._lastValue = value
        self._lastTime = time

class EWMA(ewma):
    
    def __init__(self, source, alpha = 0.15):
        ewma.__init__(self, alpha)
        source.on_changed += lambda _: self.update(world.currentTime, source.value)
        self.label = r"Avg_{\alpha="+str(alpha)+"}(" + getLabel(source) + ")"
        
        
    def __call__(self):
        return self.at(world.currentTime)
