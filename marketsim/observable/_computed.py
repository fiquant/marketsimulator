from marketsim import (bind, event, Event, getLabel, Side, scheduler, ops,
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

class Proxy(types.IObservable, ops.Function[float]):
    
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
        # TODO: include possibility of multiple aggregating functions?
        self._acc = folder
        if type(sources) is not list:
            sources = [sources]

        self._sources = sources
        for k in range(len(sources)):
            if type(sources[k]) == type(self):
                sources[k] = OnEveryDt(1, sources[k])
        self._events = [event.subscribe(source, _(self)._update, self) for source in self._sources]

    def bind(self, context):
        self._scheduler = context.world

    @property
    def label(self):
        l = '(' + ' '.join([s.label for s in self._sources]) + ')'
        if hasattr(self._acc, "label"):
            l = self._acc.label + l
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

    def __init__(self, f=(lambda x: x), window=1, name=None):
        import collections
        self.f = f
        self.history = collections.deque(maxlen=window)
        self.window = window
        # self.f_memory = {}

        if name is None:
            if hasattr(f, "__name__"):
                self.name = f.__name__
            else:
                self.name = f.__class__
        else:
            self.name = name

    def value(self):
        # quick fix, slices don't work with deque and are necessary for moving averages, etc.
        # TODO: clean this up
        if self.window > 1:
            return self.f(list(self.history)) if self.history else None
        elif hasattr(self.history, "__iter__"):
            return self.f((self.history)) if self.history else None
        else:
            return self.f(self.history) if self.history else None


    @property
    def label(self):
        return self.name

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
        # TODO: history needs to take into account the time the value has been added
        if (value is not None and not hasattr(value, "__iter__")) or (len(value) > 1 and None not in value):
            self.addValue(value)
        if hasattr(value, "__iter__") and len(value) == 1 and value != [None]:
            self.addValue(value[0])


def aggregate(observables, aggregator, window=1, name=None):
    """ helper function to aggregate observables
    example: maximum price of the asset over the last 20 days:
            aggregate( observable.Price(book), max, window = 20)
    example: bid-ask spread for a given asset:
            asks, bids = observable.AskPrice(book), observable.BidPrice(book)
            aggregate( [asks, bids], lambda (ask, bid): bid - ask )
    """
    return MultiFold(
            observables,
            UpdatableLookback(aggregator, window, name))