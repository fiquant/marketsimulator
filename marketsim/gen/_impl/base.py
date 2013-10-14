from templet import stringfunction
from werkzeug.utils import cached_property


tab = "    "
nl = "\n"
comma = ","
slash = "\\"

dummy_t = """
def dummy(self): 
   \"\"\"%(__body__)s\"\"\"
   pass
"""

def screen_escapes(s):
    return s.replace('\"\"\"', '\\\"\\\"\\\"')

class Base(object):

    def __init__(self, cls):
        self.cls = cls

    def expand(self, template):
        tmpl = screen_escapes(template)
        func = (dummy_t % { '__body__' : tmpl })
        exec func
        try:
            return stringfunction(dummy)(self)
        except AttributeError, exc:
            print "caught: ", exc.message

    def __getattr__(self, name):
        name_t = name + "_t"
        if hasattr(self, name_t):
            return self.expand(getattr(self, name_t))
        else:
            raise AttributeError(name_t)
        
    @cached_property
    def name(self): 
        return self.cls.__name__
        
    @cached_property
    def docstring(self):
        return self.cls.__doc__
    
    def makeFieldGeneric(self, n, v, constraint):
        return n, v.defvalue, constraint
    
    def makeFieldPrimitive(self, n, v):
        return n, v, type(v).__name__
    
    def convertField(self, n):
        v = getattr(self.cls, n)
        constraint = getattr(v, "constraint", None)
        if constraint is not None:
            return self.makeFieldGeneric(n, v, constraint)
        else:
            if type(v) in [float, int]:
                return self.makeFieldPrimitive(n, v)
            else:
                assert False, "unsupported type"
                        
    @cached_property
    def fields(self):
        return [self.convertField(n) for n in dir(self.cls) if n[0:2] != '__']
    
    @property
    def alias(self):
        return self.name

    registration_t = """
        @registry.expose(['${self.category}', '${self.alias}'])"""

    baseclass_t = "object"

    header_t = """
        ${self.registration}
        class ${self.name}(${self.baseclass}):
        """

    doc_t = """
        ${{}}
            \"\"\" ${self.docstring}
            \"\"\"    
        """
        
    @cached_property
    def initfields(self):
        return self.joinfields("%(name)s = %(ini)s")
    
    assignfield = "self.%(name)s = %(name)s"
    
    @cached_property
    def assignfields(self):
        return self.joinfields(self.assignfield, nl + 2*tab)
    
    initbody_t = """
        ${{}}
                ${self.assignfields}
        """
        
    init_t = """
        ${{}}

            def __init__(self, ${self.initfields}):
        ${self.initbody}
        """ 
      
    label_t = """
        ${{}}

            @property
            def label(self):
                return repr(self)
        """
      
        
    @cached_property
    def propfields(self):
        return self.joinfields("\'%(name)s\' : %(typ)s", comma + nl + 2*tab)
        
    properties_t = """
        ${{}}

            _properties = { 
                ${self.propfields}
            }
        """

    @cached_property
    def reprfields(self):
        return self.joinfields("%(name)s = \" + str(self.%(name)s) + \"")
    
    reprbody_t = """
        ${{}}
                return "${self.name}(${self.reprfields})"
        """

    repr_t = """
        ${{}}
        
            def __repr__(self):
        ${self.reprbody}
        """ 
        
    @cached_property
    def callfields(self):
        return self.joinfields("%(name)s")
    
    @property
    def implfunction(self):
        return self.name
    
    callbody_t = """
        ${{}}
                return ${self.implmodule}.${self.implfunction}(${self.callfields})
        """

    call_t = """
        ${{}}

            def __call__(self, *args, **kwargs):
        ${self.callbody}
        """
        
    def joinfields(self, tmpl, sep = ", "):
        return sep.join([tmpl % locals() for (name, ini, typ) in self.fields])

    def __getitem__(self, key):
        return getattr(self, key)
    
    members = """
            header
            doc
            init
            label
            properties
            repr
        """
        
    def __call__(self):
        return "".join(map(lambda name: getattr(self, name), self.members.split()))


class Meta(Base):
    
    registration_t = ""
    
    assignfield = "self.%(name)s = %(typ)s(%(name)s)"
