from marketsim import Event, Side
from marketsim.scheduler import Timer, world
import math

def getLabel(x):
    """ Returns a printable label for x
    We try to access 'label' field of the object 
    If it doesn't exists, we return the object id string
    TBD: add label field to all classes  
    """
    return x.label if 'label' in dir(x) else "#"+str(id(x))

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

class TraderEfficiency(object):
    
    def __init__(self, eventSources, trader):
        
        self.on_changed = Event()
        self._current = None
        self._trader = trader
        self.attributes = {}
        
        def update(_):
            def callback(sign): 
                def inner((price, volume_unmatched)):
                    if volume_unmatched == 0: 
                        self._current = trader.PnL - sign*price
                        self.on_changed.fire(self)
                    else: # don't know what to do for the moment
                        self._current = None
                return inner
        
            side = Side.Buy if trader.amount < 0 else Side.Sell 
            trader.book.evaluateOrderPriceAsync(side, abs(trader.amount), callback(-sign(trader.amount)))
        
        for es in eventSources:
            es.advise(update)
            
        update(None)

    @property
    def label(self):
        """ Returns indicator label
        """
        return "Efficiency_{"+getLabel(self._trader)+"}"
        
    def advise(self, listener):
        """ Subscribes 'listener' to value change event
        """
        self.on_changed += listener
        
    @property
    def value(self):
        """ Returns current value
        """
        return self._current

class IndicatorBase(object):
    """ Indicator that stores some scalar value and knows how to update it
    """
    def __init__(self, eventSources, dataSource, label, attributes = {}):
        """ Initializes indicator
        eventSources -- sequence of events to be subscribed to 
        dataSource -- function to be called in order to obtain the value
        label -- indicator label to be shown, for example, on a graph
        attributes -- a dictionary of attributes to be associated with the indicator
        """
        
        # this event is called when currentValue updates        
        self.on_changed = Event()
        
        self._label = label
        self.attributes = attributes

        def update(_):
            # calculate current value
            self._current = dataSource()
            if self._current is not None: # this should be removed into a separate filter
                self.on_changed.fire(self) 
        
        for es in eventSources:
            es.advise(update)
            
        update(None)
        
    @property
    def label(self):
        """ Returns indicator label
        """
        return self._label
        
    def advise(self, listener):
        """ Subscribes 'listener' to value change event
        """
        self.on_changed += listener
        
    @property
    def value(self):
        """ Returns current value
        """
        return self._current
    
def PnL(trader):
    
    return IndicatorBase([trader.on_traded], lambda: trader.PnL, "P&L_{"+getLabel(trader)+"}")
    
def AssetPrice(book):
    """ Creates an indicator bound to the middle price of an asset
    """   
    return IndicatorBase(\
        [book.asks.on_best_changed, book.bids.on_best_changed], 
        lambda: book.price, "Price_{"+getLabel(book)+"}")
    
def CrossSpread(book_A, book_B):
    asks = book_A.asks
    bids = book_B.bids
    return IndicatorBase(\
        [asks.on_best_changed, bids.on_best_changed], 
        lambda: asks.best.price - bids.best.price if not asks.empty and not bids.empty else None, 
        "Price("+asks.label+") - Price("+bids.label+")")
    
def VolumeTraded(trader):
    return IndicatorBase(\
        [trader.on_traded], 
        lambda: trader.amount, 
        "Amount_{"+getLabel(trader)+"}")
    

def BestPrice(book, side, label):
    """ Creates an indicator bound to the price of the best order in a queue
    book - asset order book
    side - side of the queue
    label - label prefix
    """
    
    queue = book.queue(side)

    return IndicatorBase(\
        [queue.on_best_changed], 
        lambda: queue.best.price if not queue.empty else None,
        "Price("+queue.label+")")
    
def BidPrice(book):
    """ Creates an indicator bound to the bid price of the asset
    book - asset order book
    """
    return BestPrice(book, Side.Buy, "BidPrice ")

def AskPrice(book):
    """ Creates an indicator bound to the ask price of the asset
    book - asset order book
    """
    return BestPrice(book, Side.Sell, "AskPrice ")

def OnEveryDt(interval, source):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    
    return IndicatorBase([Timer(lambda: interval).on_timer], 
                         source, 
                         getLabel(source), 
                         {'smooth':True})


class ewma(object):
    """ Exponentially weighted moving average
    """
    
    def __init__(self, alpha):
        """ Initializes EWMA with \alpha = alpha
        """
        self._alpha = alpha
        self._avg = None
        self.label = r"Avg_{\alpha="+str(alpha)+"}"
        
    @property 
    def value(self):
        """ Returns average value at the last update point 
        """
        return self._avg
        
    def at(self, t):
        """ Returns value of the average at some time point t >= last update time
        Returns None if no data has come
        """
        return \
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self._alpha)**( t - self._lastTime)) \
            if self._avg is not None else None
    
    def derivativeAt(self, t):
        """ Returns derivative of the average at some time point t >= last update time
        Returns None if no data has come
        """
        if self._avg is None:
            return None
        dt = t - self._lastTime
        return -(self._lastValue - self._avg)*math.log(1 - self._alpha)*(1 - self._alpha)**dt
        
    def update(self, time, value):
        """ Adds point (time, value) to calculate the average
        """
        self._avg = self.at(time) if self._avg is not None else value
        self._lastValue = value
        self._lastTime = time
        
class derivative(object):
    
    def __init__(self, src):
        self._src = src
        self.update = self._src.update
        self.at = self._src.derivativeAt
        
class Fold(object):
    """ Folds values from some source using a time-dependent accumulator....
    """
    
    def __init__(self, source, acc):
        """ Initializes folder with source of values and accumulator object        
        """
        self._acc = acc
        source.on_changed += lambda _: acc.update(world.currentTime, source.value)
        self.label = getLabel(acc) + "(" + getLabel(source) + ")"
        
    @property
    def value(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self._acc.at(world.currentTime)
    
    def __call__(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self.value
    
def EWMA(source, alpha=0.15):
    """ Creates a folder with exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return Fold(source, ewma(alpha))

def dEWMA(source, alpha=0.15):
    """ Creates a folder with derivative of exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return Fold(source, derivative(ewma(alpha)))