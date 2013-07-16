from marketsim import ops, types

class Base(object):

    def __init__(self):
        self.reset()
        
    def reset(self):
        self._definitions = self.getDefinitions()
        self.impl = self.getImpl()
        
    _properties = {'impl' : types.IFunction[float] }
        
    def __call__(self):
        return self.impl()
        
tmpl = """
%(reg)s
class %(name)s_Generated(_wrap.Base, %(name)s):
    \"\"\" %(docstring)s
    \"\"\"    
    
    def __init__(self, %(args)s):
        %(ctor)s
        _wrap.Base.__init__(self)
        %(name)s_Impl.__init__(self)

    _properties = { %(props)s }
"""

prop = """
    @property
    def %(name)s(self):
        return self._%(name)s
        
    @%(name)s.setter
    def %(name)s(self, value):
        self._%(name)s = value
        self.reset()
        
"""

trailer = """    
%(name)s_Impl = %(name)s
%(name)s = %(name)s_Generated
"""
 
def generate(cls, alias, docstring, fields, ctx):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % locals() for (name, ini, typ) in fields])
    
    args = process("%(name)s = None")
    ctor = process("self._%(name)s = %(name)s if %(name)s is not None else %(ini)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    pdefs = "".join([prop % locals() for (name, _,_) in fields])
    reg = "@registry.expose("+str(alias)+")"# if register else ""
    name = cls.__name__
    #print (tmpl + pdefs + trailer) % locals()
    exec (tmpl + pdefs + trailer) % locals() in ctx
