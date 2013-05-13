from event import Event

""" Appends *callback* into collections of listeners for 
    a change of property named *propname* of object *obj*
"""
def OnPropertyChanged(obj, propname, callback):
    if '_on_property_changed' not in dir(obj):
        obj._on_property_changed = {}
        
    if propname not in obj._on_property_changed:
        obj._on_property_changed[propname] = Event()
        
        if '_new_property_changed_listener_added' in dir(obj):
            obj._new_property_changed_listener_added(propname)
        
    obj._on_property_changed[propname] += callback
    
def NotifyPropertyChanged(obj, propname, value):
    if '_on_property_changed' in dir(obj):
        if propname in obj._on_property_changed or '*' in obj._on_property_changed:
            obj._on_property_changed[propname](propname, value)

def SetAttr(obj, propname, value):
    setattr(obj, propname, value)
    NotifyPropertyChanged(obj, propname, value)

class Bind(object):
    
    def __init__(self, callable, *args):
        self.callable = callable
        self.args = args
        
    def __call__(self, *args):
        return self.callable(*(self.args + args))


class Method(object):
    
    def __init__(self, obj, methodname, *args):
        self.obj = obj
        self.methodname = methodname 
        self.args = args
        
    def __call__(self, *args):
        return getattr(self.obj, self.methodname)(*(self.args + args))


class Construct(object):
    
    def __init__(self, class_, *args):
        self.class_ = class_
        self.args = args
        
    def __call__(self, *args):
        return self.class_(*(self.args + args))

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
