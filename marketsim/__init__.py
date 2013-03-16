class Event(object):
    """ Multicast event
    
    Keeps a set of callable listeners 
    """

    def __init__(self):
        self._listeners = set()
        
    def reset(self):
        pass
        
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
        
    def fire(self, *args):
        """ Calls all listeners passing *args to them
        """
        for x in self._listeners:
            x(*args)
            
Event._types = [Event]

def getLabel(x):
    """ Returns a printable label for *x*
    We try to access *'label'* field of the object 
    If it doesn't exists, we return the object id string
    """
    return x.label if 'label' in dir(x) else "#"+str(id(x))
                    
## {{{ http://code.activestate.com/recipes/576563/ (r1)
def cached_property(f):
    """returns a cached property that is calculated by function f"""
    def get(self):
        try:
            return self._property_cache[f]
        except AttributeError:
            self._property_cache = {}
            x = self._property_cache[f] = f(self)
            return x
        except KeyError:
            x = self._property_cache[f] = f(self)
            return x
        
    return property(get)
