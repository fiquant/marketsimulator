from templet import stringfunction
from werkzeug.utils import cached_property
from .. import types
from types import *

from base import *

class Gen(Base):
    
    def __init__(self, cls, category, impl):
        Base.__init__(self, cls)
        self.category = category
        self.impl = impl
    
    @stringfunction
    def header(self):
        """
        @registry.expose(['${self.category}', '${self.name}'])
        class ${self.name}(ops.Observable[float]):
        """

        
    @cached_property
    def callfields(self):
        return self.joinfields("%(name)s")
    
    @cached_property
    def nullablefields(self):
        return self.joinfields("%(name)s = self.%(name)s()\n        if %(name)s is None: return None", nl + 2*tab)
    
    @stringfunction
    def call(self):
        """
        ${{}}

            def __call__(self, *args, **kwargs):
                ${self.nullablefields}
                return math.${self.impl}(${self.callfields})
        """
            
    def members(self):
        return Base.members(self) + """
            call
        """ 

defs = ["from marketsim import registry, types, ops", "import math"]

def imported(category, impl):
    
    def inner(cls):
        defs.append(Gen(cls, category, impl)())
        #exec Meta(cls)() in globals()
        #return globals()[cls.__name__]
    
    return inner
