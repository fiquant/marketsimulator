from marketsim import (bind, event, Event, getLabel, Side, scheduler, 
                       types, meta, mathutils, ops, registry, trader, _)

class IndicatorBase(types.Observable):
    """ Observable that stores some scalar value and knows how to update it
    
    * **Source of data** -- function that provides data
    * **Events when to act** -- events when to act
    """
    def __init__(self, eventSource, dataSource, attributes = {}):
        """ Initializes indicator
        eventSources -- sequence of events to be subscribed to 
        dataSource -- function to be called in order to obtain the value
        label -- indicator label to be shown, for example, on a graph
        attributes -- a dictionary of attributes to be associated with the indicator
        """
        
        super(IndicatorBase, self).__init__()
        self.attributes = attributes
        self._subscription = event.subscribe(eventSource, self.fire, self)
        self._dataSource = dataSource
        
    @property    
    def label(self):
        return self._dataSource.label
    
    _properties = [ ('dataSource'  , types.IFunction[float]),
                    ('eventSource' , Event) ]
    
    @property
    def eventSource(self):
        return self._subscription.event
    
    @eventSource.setter
    def eventSource(self, value):
        self._subscription.event = value 
        
    @property
    def digits(self):
        return self._dataSource.digits if 'digits' in dir(self._dataSource) else 4
    
    @property
    def dataSource(self):
        return self._dataSource
    
    @dataSource.setter
    def dataSource(self, value):
        self._dataSource = value
    
    def schedule(self):
        self.reset()
                
    def __call__(self):
        """ Returns current value
        """
        return self._dataSource()

class Proxy(types.IObservable):
    
    def __iadd__(self, listener):
        self._impl.__iadd__(listener)
        return self
        
    def __isub__(self, listener):
        self._impl.__isub__(listener)
        return self
    
    def __call__(self):
        return self._impl.__call__()
    
    @property
    def _digitsToShow(self):
        return self._impl._digitsToShow
    
    @property
    def label(self):
        return self._impl.label
    
    @property
    def attributes(self):
        return {}


def OnEveryDt(interval, source):
    """ Creates an indicator that is updated regularly
    interval - constant interval between updates
    source - function to obtain indicator value
    """
    
    return IndicatorBase(scheduler.Timer(ops.constant(interval)),
                         source, 
                         {'smooth':True})

class MultiFold(ops.Function[float]):
    def __init__(self, sources, folder):
        """ Folding function for multiple sources
        """
        self._acc = folder
        self._sources = sources
        self._events = [event.subscribe(source, _(self)._update, self) for source in self._sources]

    def bind(self, context):
        self._scheduler = context.world

    @property
    def label(self):
        l = self._acc.label + '(' + ' '.join([s.label for s in self._sources]) + ')'
        return l

    _properties = { 'source' : types.IObservable,
                    'folder' : types.IUpdatableValue }

    def _update(self, _):
        self._acc.update(self._scheduler.currentTime, [source() for source in self._sources])

    @property
    def folder(self):
        return self._acc

    @folder.setter
    def folder(self, value):
        # TODO: FIX
        self._acc = value

    @property
    def source(self):
        # TODO: FIX
        return self._sources[0]

    @source.setter
    def source(self, value):
        # TODO: FIX
        self._source = value
        self._event.switchTo(self._source)

    def __call__(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self._acc.at(self._scheduler.currentTime)

class UpdatableLookback(types.IUpdatableValue):
    """ Computed value based on one or more sources
    """

    def __init__(self, f, window=1):
        import collections
        self.f = f
        self.history = collections.deque(maxlen=window)
        self.window = window
        # self.f_memory = {}

    def value(self):
        return self.f(self.history) if self.history else None

    @property
    def label(self):
        return self.f.__name__

    def addValue(self, value):
        if self.window > 1:
            self.history.append(value)
        else:
            self.history = value

    def at(self, t):
        return self.value()

    def derivativeAt(self, t):
        return self.value()

    def update(self, time, value):
        if (value is not None and not hasattr(value, "__iter__")) or (len(value) > 1 and None not in value):
            self.addValue(value)


def aggregate(observables, aggregator, window=1):
    """ helper function to aggregate observables
    example: maximum price of the asset over the last 20 days:
            aggregate( observable.Price(book), max, window = 20)
    example: bid-ask spread for a given asset:
            asks, bids = observable.AskPrice(book), observable.BidPrice(book)
            aggregate( [asks, bids], lambda (ask, bid): bid - ask )
    """
    return MultiFold(
            observables,
            UpdatableLookback(aggregator, window))