class merge(object):
    def __init__(self, d, **kwargs):
        self.__dict__ = d.__dict__.copy()
        for k in kwargs:
            self.__dict__[k] = kwargs[k]

template = """
%(reg)s
class %(name)s(object):
    \"\"\" %(docstring)s
    \"\"\"    
    
    def __init__(self, %(init)s, label=None):
        self.label = label
        self._constructAs = 'marketsim.strategy.%(name)s'
        %(dict_)s
        self._impl = None
        self._trader = None
        
    _types = [types.IStrategy]
        
    _properties = { %(props)s }

    def reset(self):
        if 'reset' in dir(self._impl):
            self._impl.reset()
            
    def dispose(self):
        if self._impl is not None:
            self._impl.dispose()
            self._impl = None

    def _respawn(self):
        self.dispose()
        self._impl = _%(name)s_Impl(self._trader, self)
        
    def __getattr__(self, item):
        if '_impl' in self.__dict__ and self._impl is not None:
            return getattr(self._impl, item)
        if item == 'suspended':
            return True
        raise AttributeError()
        
    def __setattr__(self, item, value):
        self.__dict__[item] = value
        if item in %(name)s._properties and self._trader:
            self._respawn()
    
    def With(self, %(withini)s):
        
        %(withbody)s
        
        return %(name)s(%(withrv)s)
        
    def bind(self, context):
        self._trader = context.trader
        self.world = context.world
        self._respawn()
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

def wrapper(name, docstring, params, register=True, category="Basic"):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % mapped(locals()) for (name, ini, typ) in params])
    
    init = process("%(name)s = %(ini)s")
    withini = process("%(name)s = None")
    withbody = process("%(name)s = %(name)s if %(name)s is not None else self.%(name)s", "; ")
    withrv = process("%(name)s")
    dict_= process("self.__dict__[\'%(name)s\'] = %(name)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    call = process("self.%(name)s")
    reg = "@registry.expose(['"+category+"', '"+name+"'])" if register else ""
    
    return template % locals()

template2 = """
%(reg)s
class %(name)s(_%(name)s_Impl):
    \"\"\" %(docstring)s
    \"\"\"    
    
    def __init__(self, %(init)s):
        self._constructAs = 'marketsim.strategy.%(name)s'
        %(dict_)s
        _%(name)s_Impl.__init__(self)

    _types = [types.IStrategy]
        
    _properties = { %(props)s }

    def With(self, %(withini)s):
        
        %(withbody)s
        
        return %(name)s(%(withrv)s)
"""

def wrapper2(name, docstring, params, register=True, category="Basic"):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % mapped(locals()) for (name, ini, typ) in params])
    
    init = process("%(name)s = %(ini)s")
    withini = process("%(name)s = None")
    withbody = process("%(name)s = %(name)s if %(name)s is not None else self.%(name)s", "; ")
    withrv = process("%(name)s")
    dict_= process("self.__dict__[\'%(name)s\'] = %(name)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    reg = "@registry.expose(['"+category+"', '"+name+"'])" if register else ""
    
    return template2 % locals()
