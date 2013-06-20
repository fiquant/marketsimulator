from event import Event

class Alias(object):
    
    @property
    def _alias(self):
        return self.__alias if '__alias' in dir(self) else self._initialAlias
    
    @_alias.setter
    def _alias(self, value):
        self.__alias = value 
    
    

class flags(object):
    
    @staticmethod
    def hidden(d):
        d['hidden'] = True
        
    @staticmethod
    def collapsed(d):
        d["collapsed"] = True

def getLabel(x):
    """ Returns a printable label for *x*
    We try to access *'label'* field of the object 
    """
    return x.label

class Reference(object):

    def __init__(self, name):
        self._impl = None
        self.name = name
        
    def bind(self, ctx):
        assert self._impl is  None
        self._impl = getattr(ctx, self.name)
        
    def __getattr__(self, name):
        if name[0:2] != "__" and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
        
    def __iadd__(self, other):
        self._impl += other
        return self
    
    def __isub__(self, other):
        self._impl -= other
        return self
    
    def __call__(self, *args, **kwargs):
        return self._impl(*args, **kwargs)
    
    _properties = { 'name' : str }

def defs(obj, vs):
    if '_definitions' not in dir(obj):
        obj._definitions = {}
    obj._definitions.update(vs)
    return obj

class RefFactory(object):
    
    def __getattr__(self, name):
        if name[0:2] != "__":
            return Reference(name)
        else:
            raise AttributeError
    
_ =  RefFactory()
                        
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
