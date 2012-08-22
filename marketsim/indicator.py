from marketsim import Event, Side
from marketsim.scheduler import Timer

def isIterable(x):
    return '__iter__' in dir(x)

def getLabel(x):
    return x.label if 'label' in dir(x) else "#"+str(id(x))
        

class IndicatorBase(object):
    
    def __init__(self, eventSource, dataSource, label):
        
        self.on_changed = Event()
        self._label = label

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

def OnEveryDt(interval, source, label):
    
    return IndicatorBase([Timer(lambda: interval).on_timer], source, label)