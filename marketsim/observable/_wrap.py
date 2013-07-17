from marketsim import ops, types, event, _, flags

class Base(object):

    def __init__(self):
        if 'getDefinitions' in dir(self):
            self._definitions = self.getDefinitions()
        self.impl = self.getImpl()
                
    def __call__(self):
        return self.impl()

class FunctionBase(Base):

    _properties = {'impl' : (types.IFunction[float], flags.collapsed) }

class ObservableBase(Base):

    def __init__(self):
        Base.__init__(self)
        event.subscribe(self.impl, _(self).fire, self)
        
    _properties = {'impl' : (types.IObservable[float], flags.collapsed) }
        
tmpl = """
%(reg)s
class %(name)s_Generated(_wrap.%(kind)sBase, %(name)s):
    \"\"\" %(docstring)s
    \"\"\"    
    
    def __init__(self, %(args)s):
        %(ctor)s
        _wrap.%(kind)sBase.__init__(self)
        %(name)s_Impl.__init__(self)
        
    def updateContext(self, ctx):
        %(binds)s
        pass
        
    @property
    def attributes(self):
        return {}

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

def _generate(kind, cls, alias, docstring, fields, ctx):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % locals() for (name, ini, typ) in fields])
    
    args = process("%(name)s = None")
    ctor = process("self._%(name)s = %(name)s if %(name)s is not None else %(ini)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    binds = process("ctx.%(name)s = self._%(name)s", "; ")
    pdefs = "".join([prop % locals() for (name, _,_) in fields])
    reg = "@registry.expose("+str(alias)+")"# if register else ""
    name = cls.__name__
    #print (tmpl + pdefs + trailer) % locals()
    exec (tmpl + pdefs + trailer) % locals() in ctx
 
def function(cls, alias, docstring, fields, ctx):
    _generate("Function", cls, alias, docstring, fields, ctx)
    
def observable(cls, alias, docstring, fields, ctx):
    _generate("Observable", cls, alias, docstring, fields, ctx)
