from marketsim import (bind, event, Event, getLabel, Side, scheduler, 
                       types, meta, mathutils, registry, trader)

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
    
    _properties = [ ('dataSource'  , meta.function((), float)),
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
    
    return IndicatorBase(scheduler.Timer(mathutils.constant(interval)),
                         source, 
                         {'smooth':True})

    