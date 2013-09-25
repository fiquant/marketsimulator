from templet import stringfunction
from werkzeug.utils import cached_property


tab = "    "
nl = "\n"
comma = ","
slash = "\\"

class Base(object):

    def __init__(self, cls):
        self.cls = cls 
        
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

    @stringfunction
    def registration(self):
        """
        @registry.expose(['${self.category}', '${self.alias}'])"""

    @property
    def baseclass(self):
        return "object"

    @stringfunction
    def header(self):
        """
        ${self.registration()}
        class ${self.name}(${self.baseclass}):
        """

    @stringfunction
    def doc(self):
        """
        ${{}}
            \"\"\" ${self.docstring}
            \"\"\"    
        """
        
    @cached_property
    def initfields(self):
        return self.joinfields("%(name)s = %(ini)s")
    
    @property
    def assignfield(self):
        return "self.%(name)s = %(name)s"
    
    @cached_property
    def assignfields(self):
        return self.joinfields(self.assignfield, nl + 2*tab)
    
    @stringfunction
    def initbody(self):
        """
        ${{}}
                ${self.assignfields}
        """
        
    @stringfunction
    def init(self):
        """
        ${{}}

            def __init__(self, ${self.initfields}):
        ${self.initbody()}
        """ 
      
    @stringfunction
    def label(self):
        """
        ${{}}

            @property
            def label(self):
                return repr(self)
        """
      
        
    @cached_property
    def propfields(self):
        return self.joinfields("\'%(name)s\' : %(typ)s", comma + nl + 2*tab)
        
    @stringfunction
    def properties(self):
        """
        ${{}}

            _properties = { 
                ${self.propfields}
            }
        """

    @cached_property
    def reprfields(self):
        return self.joinfields("%(name)s = \" + str(self.%(name)s) + \"")

    @stringfunction
    def repr(self):
        """
        ${{}}
        
            def __repr__(self):
                return "${self.name}(${self.reprfields})"
        """
        
    def joinfields(self, tmpl, sep = ", "):
        return sep.join([tmpl % locals() for (name, ini, typ) in self.fields])

    def __getitem__(self, key):
        return getattr(self, key)
    
    def members(self):
        return """
            header
            doc
            init
            label
            properties
            repr
        """
        
    def __call__(self):
        return "".join(map(lambda name: getattr(self, name)(), 
                           self.members().split()))


class Meta(Base):
    
    def registration(self):
        return ""
    
    @property
    def assignfield(self):
        return "self.%(name)s = %(typ)s(%(name)s)"
