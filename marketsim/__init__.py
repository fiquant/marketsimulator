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

def deref_opt(x):
    return getattr(x, "dereference") if hasattr(x, "dereference") else x


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
                        
