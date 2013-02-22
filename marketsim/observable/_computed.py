from marketsim import Event, getLabel, Side, scheduler

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
        
        
        self._label = label
        self.attributes = attributes
        self._eventSources = eventSources
        self._dataSource = dataSource
        self.on_changed = Event()

        # this event is called when currentValue updates        
        def update(_):
            # calculate current value
            self._current = self._dataSource()
            if self._current is not None: # this should be removed into a separate filter
                self.on_changed.fire(self) 
        
        for es in self._eventSources:
            es.advise(update)
            
        update(None)
        
    _properties = {}
        
    def reset(self):
        self._current = None
        if 'reset' in dir(self._dataSource):
            self._dataSource.reset()
        for es in self._eventSources:
            es.reset()
            
    def schedule(self):
        self.reset()
                
    @property
    def label(self):
        """ Returns indicator label
        """
        return self._label
        
    def advise(self, listener):
        """ Subscribes 'listener' to value change event
        """
        self.on_changed += listener
        
    def unadvise(self, listener):
        self.on_changed -= listener
        
    @property
    def value(self):
        """ Returns current value
        """
        return self._current
    
def InstEfficiency(trader):
    
    return IndicatorBase([trader.on_traded], 
                         lambda: trader.PnL + trader.amount*trader.book.price if trader.book.price else 0,
                         "InstEfficiency_{" + getLabel(trader) + "}")
    
def PnL(trader):
    
    return IndicatorBase([trader.on_traded], lambda: trader.PnL, "P&L_{"+getLabel(trader)+"}")
    
def Price(book):
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
    
    return IndicatorBase([scheduler.Timer(lambda: interval)],
                         source, 
                         getLabel(source), 
                         {'smooth':True})
