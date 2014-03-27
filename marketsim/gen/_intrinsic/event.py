from marketsim import bind, meta, context, types, _

from marketsim.gen._out._intrinsic_base.event import Every_Base, After_Base
            
class Event_Impl(object):
    """ Multicast event

    Keeps a set of callable listeners
    """

    def __init__(self):
        self._listeners = None
        self.fire = bind.Method(self, '_fire_impl')

#    _internals = ['_listeners']

    def __iadd__(self, listener):
        """ Adds 'listener' to the listeners set
        """
        if self._listeners is None:
            self._listeners = set()
        self._listeners.add(listener)
        return self

    def __isub__(self, listener):
        self._listeners.remove(listener)
        return self

    def _fire_impl(self, *args):
        """ Calls all listeners passing *args to them
        """
        if self._listeners:
            for x in list(self._listeners):
                x(*args)

from marketsim.gen._out._ievent import IEvent
class Event(Event_Impl, IEvent):
    """ Multicast event
    
    Keeps a set of callable listeners 
    """

class Conditional_Impl(Event_Impl):
    
    def __init__(self):
        Event_Impl.__init__(self)
        from blist import sorteddict
        self._greater = sorteddict()
        self._less = sorteddict()
    
    def __iadd__(self, listener):
        if '_greaterThan' in dir(listener):
            bound = listener._greaterThan()
            if bound not in self._greater:
                self._greater[bound] = []
            self._greater[bound].append(listener)
            return self
        elif '_lessThan' in dir(listener):
            bound = listener._lessThan()
            if -bound not in self._less:
                self._less[-bound] = []
            self._less[-bound].append(listener)
            return self
        else:
            return Event_Impl.__iadd__(self, listener)
            
    def __isub__(self, listener):
        if '_greaterThan' in dir(listener):
            bound = listener._greaterThan()
            self._greater[bound].remove(listener)
            return self
        elif '_lessThan' in dir(listener):
            bound = listener._lessThan()
            self._less[-bound].remove(listener)
            return self
        else:
            return Event_Impl.__isub__(self, listener)
            
    def _fire_impl(self, *args):
        if len(self._less) or len(self._greater):
            current = self()
            if current is not None:
                for bound, handlers in list(self._greater.iteritems()):
                    if bound < current:
                        for handler in handlers:
                            handler(*args)
                for bound, handlers in list(self._less.iteritems()):
                    if -bound > current:
                        for handler in handlers:
                            handler(*args)
        Event_Impl._fire_impl(self, *args)

class Conditional(Conditional_Impl, IEvent): pass
        
class GreaterThan(object):
    
    def __init__(self, bound, target):
        self.bound = bound
        self.target = target
        
    _internals = ['target']
        
    def _greaterThan(self):
        return self.bound
    
    def __call__(self, *args):
        self.target(*args)
                
class LessThan(object):
    
    def __init__(self, bound, target):
        self.bound = bound
        self.target = target
        
    _internals = ['target']
        
    def _lessThan(self):
        return self.bound
    
    def __call__(self, *args):
        self.target(*args)
                
            

class Array(Event):
    
    def __init__(self, events):
        self._events = []
        self.events = events
        
    _properties = { 'events' : meta.listOf(Event) }
        
    @property
    def events(self):
        return self._events
    
    @events.setter
    def events(self, value):
        for ev in self._events:
            ev -= self.fire
        self._events = value
        for ev in self._events:
            ev += self.fire
            
    def dispose(self):
        for ev in self._events:
            ev -= self.fire
        
        
        
    
            
class Subscription(object):
    
    def __init__(self, event, listener):
        self._event = event 
        self._listener = listener
        self._subscribed = False # in fact it is _bound but its cleaning is not yet supported at dispose
        
    _internals = ['_event']
    
    @property
    def event(self):
        return self._event
    
    @event.setter
    def event(self, value):
        self._event -= self._listener
        self._event = value
        self._event += self._listener
        
    def switchTo(self, newEvent):
        self._event -= self._listener
        self._event = newEvent
        self._event += self._listener
        
    def bind(self, context):
        self._event += self._listener
        self._subscribed = True
        
    def dispose(self):
        if self._subscribed:
            self._event -= self._listener
            self._subscribed = False
                
def dispose(obj):
    if '_subscriptions' in dir(obj):
        for x in obj._subscriptions:
            x.dispose()
    if '_children_to_visit' in dir(obj):
        for child in obj._children_to_visit:
            if 'dispose' in dir(child):
                child.dispose()
            
                
def subscribe(event, listener, target = None, ctx = None):
    
    subscription = Subscription(event, listener)
    
    if target is not None:
        if '_subscriptions' not in dir(target):
            target._subscriptions = []
            
        target._subscriptions.append(subscription)
        
        if 'dispose' not in dir(target):
            target.dispose = bind.Callable(dispose, target)
            
    if ctx is not None:
        context.bind(subscription, ctx)
            
    return subscription

def subscribe_if_observable(source, target):
    if isinstance(source, IEvent):
        subscribe(source, _(target).fire, target)

class Every_Impl(Event_Impl, Every_Base):
    """ Represents a repeating action. 
    
        Parameters:
        
        *intervalFunc*
            intervals of time between moments when subscribed listeners are to be called  
    """

    def __init__(self):
        Event_Impl.__init__(self)
        self._cancelled = False
        
    def bind(self, context):
        self._scheduler = context.world
        self.schedule()

    def schedule(self):
        self._scheduler.scheduleAfter(self.intervalFunc(), _(self)._wakeUp)
        
    def reset(self):
        self.schedule()
        
    def _wakeUp(self):
        if not self._cancelled:
            self.fire(self)
            self.schedule()

    def cancel(self):
        self._cancelled = True
 
class After_Impl(Event_Impl, After_Base):

    def __init__(self):
        Event_Impl.__init__(self)
        self._cancelled = False
        
    def bind(self, context):
        self._scheduler = context.world
        self.schedule()

    def schedule(self):
        self._scheduler.scheduleAfter(self.delay(), _(self)._wakeUp)
        
    def reset(self):
        self.schedule()
        
    def _wakeUp(self):
        if not self._cancelled:
            self.fire(self)

    def cancel(self):
        self._cancelled = True
 
