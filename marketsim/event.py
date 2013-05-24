class Event(object):
    """ Multicast event
    
    Keeps a set of callable listeners 
    """

    def __init__(self):
        self._listeners = set()
        
    def reset(self):
        pass
    
#    _internals = ['_listeners']
        
    def __iadd__(self, listener):
        """ Adds 'listener' to the listeners set
        """
        self._listeners.add(listener)
        return self
    
    def __isub__(self, listener):
        self._listeners.remove(listener)
        return self
        
    def advise(self, listener):
        """ Adds *listener* to the listeners set
        """
        self += listener

    def unadvise(self, listener):
        """ Removes *listener* from the listeners set
        """
        self -= listener
        
    def __call__(self, *args):
        """ Calls all listeners passing *args to them
        """
        for x in self._listeners:
            x(*args)
    
    @property    
    def fire(self):
        return self
            
Event._types = [Event]

class Subscription(object):
    
    def __init__(self, field, listener):
        self._field = field 
        self._listener = listener
        
    _internals = ['_field']
        
    def bind(self, context):
        self._field += self._listener
        
    def dispose(self):
        self._field -= self._listener
        
    def reset(self):
        self._field.reset()
        
def subscribe(target, fieldname, eventsource, listener):
    
    setattr(target, fieldname, eventsource)
    
    subscription = Subscription(getattr(target, fieldname), listener)
    
    if '_subscriptions' not in dir(target):
        target._subscriptions = []
        
    target._subscriptions.append(subscription)
        
