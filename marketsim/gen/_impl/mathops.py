from templet import stringfunction
from werkzeug.utils import cached_property
from .. import types
from types import *

from base import *

class Gen(Base):
    
    def __init__(self, cls, category, impl, label):
        Base.__init__(self, cls)
        self.category = category
        self.impl = impl
        self._label = label
        
    def makeFieldGeneric(self, n, v, constraint):
        return n, v.defvalue.getName()[1], constraint
        
    @stringfunction
    def reprbody(self):
        """
        ${{}}
                return "${self._label}" % self.__dict__
        """
    
    baseclass = "Observable[float]"

    def initbody(self):
        return 2*tab + "Observable[float].__init__(self)" + Base.initbody(self)
    
    assignfield = """
        self.%(name)s = %(name)s
        if isinstance(%(name)s, types.IEvent):
            event.subscribe(self.%(name)s, self.fire, self)"""
            
    implmodule = "math"
    
    @property
    def implfunction(self):
        return self.impl

    @cached_property
    def nullablefields(self):
        return self.joinfields("%(name)s = self.%(name)s()\n        if %(name)s is None: return None", nl + 2*tab)
    
    @stringfunction
    def callbody(self):
        """
        ${{}}
                ${self.nullablefields}
        ${Base.callbody(self)}
        """
            
    members = Base.members + """
            call
        """ 

defs = ["from marketsim import registry, types, event", 
        "import math", 
        "from _all import Observable, Constant"]

def imported(category, impl, label):
    
    def inner(cls):
        defs.append(Gen(cls, category, impl, label)())
        #exec Meta(cls)() in globals()
        #return globals()[cls.__name__]
    
    return inner
