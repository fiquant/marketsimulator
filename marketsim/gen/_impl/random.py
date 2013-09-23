from templet import stringfunction
from werkzeug.utils import cached_property

class Base(object):

    def __init__(self, cls, alias, rvtype=float):
 
        self.alias = alias
        self.rvtype = rvtype.__name__
        self.name = cls.__name__
        self.docstring = cls.__doc__
        self.fields = []
        
        for n in dir(cls):
            if n[0:2] != '__':
                v = getattr(cls, n)
                constraint = getattr(v, "constraint", None)
                if constraint is not None:
                    self.fields.append((n, v.defvalue, constraint))
                else:
                    if type(v) in [float, int]:
                        self.fields.append((n, v, type(v).__name__))
                    else:
                        assert False, "unsupported type"

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
    
    @cached_property
    def assignfields(self):
        return self.joinfields("self.%(name)s = %(name)s", nl + 2*tab)
        
    @stringfunction
    def init(self):
        """
        ${{}}

            def __init__(self, ${self.initfields}):
                ${self.assignfields}
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

class RandomImpl(Base):
    
    @stringfunction
    def header(self):
        """
        @registry.expose(['Random', '${self.alias}'])
        class ${self.name}(ops.Function[${self.rvtype}]):
        """

    @stringfunction
    def casts_to(self):
        """
        ${{}}

            def _casts_to(self, dst):
                return ${self.name}._types[0]._casts_to(dst)
        """

        
    @cached_property
    def callfields(self):
        return self.joinfields("self.%(name)s")
    
    @stringfunction
    def call(self):
        """
        ${{}}

            def __call__(self, *args, **kwargs):
                return random.${self.name}(${self.callfields})
        """
            
    def members(self):
        return Base.members(self) + """
            call
            casts_to
        """ 

tab = "    "
nl = "\n"
comma = ","
slash = "\\"

class RandomMeta(Base):
    
    @cached_property
    def assignfields(self):
        return self.joinfields("self.%(name)s = %(typ)s(%(name)s)", nl + 2*tab)

    @stringfunction
    def header(self):
        """
        class ${self.name}(object):
        """
