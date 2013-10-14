from templet import stringfunction
from werkzeug.utils import cached_property
from .. import types, ops
from types import *

from base import *

class Gen(Base):
    
    def __init__(self, cls, category, impl, label):
        Base.__init__(self, cls)
        self.category = category
        self.impl = impl
        self._label = label

    @property
    def implmodule(self):
        return "math"
        
    def makeFieldGeneric(self, n, v, constraint):
        return n, v.defvalue.getName()[1], constraint
    
    def makeFieldPrimitive(self, n, v):
        v = types.IFunction[float](ops.Constant[float](v))
        return self.makeFieldGeneric(n, v, v.constraint)
        
    reprbody_t = """
        ${{}}
                return "${self._label}" % self.__dict__
        """
    
    baseclass = "Observable[float]"

    initbody_t = """
        ${{}}
                Observable[float].__init__(self)
                ${self.expand(Base.initbody_t)}
        """

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

    callbody_t = """
        ${{}}
                ${self.nullablefields}
        ${self.expand(Base.callbody_t)}
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
        exec Meta(cls)() in globals()
        return globals()[cls.__name__]
    
    return inner
