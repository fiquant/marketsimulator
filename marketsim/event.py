from marketsim import bind

class Event(object):
    """ Multicast event
    
    Keeps a set of callable listeners 
    """

    def __init__(self):
        self._listeners = set()
        self.fire = bind.Method(self, '_fire_impl')
        
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
        
    def _fire_impl(self, *args):
        """ Calls all listeners passing *args to them
        """
        for x in self._listeners:
            x(*args)
            
Event._types = [Event]

class Subscription(object):
    
    def __init__(self, event, listener):
        self._event = event 
        self._listener = listener
        
    _internals = ['_event']
        
    def bind(self, context):
        self._event += self._listener
        
    def dispose(self):
        self._event -= self._listener
                
def subscribe(event, listener, target = None):
    
    subscription = Subscription(event, listener)
    
    if target is not None:
        if '_subscriptions' not in dir(target):
            target._subscriptions = []
            
        target._subscriptions.append(subscription)
        
