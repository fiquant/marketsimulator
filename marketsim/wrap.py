class Base(object):

    def __init__(self):
        self.impl = self.getImpl()
        if 'getDefinitions' in dir(self):
            self.impl._definitions = self.getDefinitions()
                
    def __call__(self):
        return self.impl()
    
    @property
    def label(self):
        return self.impl.label

tmpl = """
%(reg)s
class %(name)s_Generated(%(name)s, _wrap.%(kind)sBase[%(name)s.T]):
    \"\"\" %(docstring)s
    \"\"\"    
    
    def __init__(self, %(args)s):
        %(ctor)s
        _wrap.%(kind)sBase[%(name)s.T].__init__(self)
        %(name)s_Impl.__init__(self)
        
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

def demangleIfFunction(s):
    head, sep, tail = s.partition('->')
    if sep == '': return s
    head = head.strip()
    if head[0] != '(' and head[-1] != ')':
        head = '(' + head + ',)'
    rv = demangleIfFunction(tail)
    return 'types.function(%(head)s, %(rv)s)' % locals() 
    
def mapped(locs):
    locs['typ'] = demangleIfFunction(locs['typ'])
    return locs

def generate(kind, cls, alias, docstring, fields, ctx):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % mapped(locals()) for (name, ini, typ) in fields])
    
    args = process("%(name)s = None")
    ctor = process("self._%(name)s = %(name)s if %(name)s is not None else %(ini)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    binds = process("ctx.%(name)s = self._%(name)s", "; ")
    pdefs = "".join([prop % locals() for (name, _,_) in fields])
    reg = "@registry.expose("+str(alias)+")"# if register else ""
    name = cls.__name__
    #print (tmpl + pdefs + trailer) % locals()
    exec (tmpl + pdefs + trailer) % locals() in ctx
