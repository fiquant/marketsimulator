import gen, collections

from gen import cached_property

from bind import Method
from reference import Reference

from meta import listOf, function

float = float

Volume = float
Price = float
bool = bool
str = str
int = int

def call(target, *args):
    r = target(*args)
    if hasattr(r, "dereference"):
        r = getattr(r, "dereference")
    return r


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


def defs(obj, vs):
    if '_definitions' not in dir(obj):
        obj._definitions = {}
    obj._definitions.update(vs)
    return obj

class Binder(object):
    
    def __init__(self, target, args):
        self.target = target
        self.args = args
        
    def __getattr__(self, name):
        if name[0:2] != "__":
            return bind.Method(self.target, name, *self.args)
        else:
            raise AttributeError
    

class Underscore(object):
    
    def __getattr__(self, name):
        if name[0:2] != "__":
            return Reference(name)
        else:
            raise AttributeError
        
    def __call__(self, target, *args):
        return Binder(target, args)
    
_ =  Underscore()
                        
