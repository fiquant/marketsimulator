class merge(object):
    def __init__(self, d, **kwargs):
        self.__dict__ = d.__dict__.copy()
        for k in kwargs:
            self.__dict__[k] = kwargs[k]

template = """
class %(name)s(object):
    
    def __init__(self, %(init)s, label=None):
        from marketsim.registry import uniqueName
        self.label = uniqueName('%(name)s') if label is None else label
        self._constructAs = 'marketsim.strategy.%(name)s'
        %(dict_)s
        self._impl = None
        
    _types = [types.IStrategy]
        
    _properties = { %(props)s }

    def reset(self):
        if 'reset' in dir(self._impl):
            self._impl.reset()
            
    def dispose(self):
        if self._impl is not None:
            self._impl.dispose()

    def _respawn(self):
        self.dispose()
        self._impl = _%(name)s_Impl(self._trader, self)
        
    def __getattr__(self, item):
        if self._impl is not None:
            return getattr(self._impl, item)
        
    def __setattr__(self, item, value):
        self.__dict__[item] = value
        if item in %(name)s._properties and self._trader:
            self._respawn()
    
    def With(self, %(withini)s):
        
        %(withbody)s
        
        return %(name)s(%(withrv)s)
        
    def runAt(self, trader):
        assert self._impl == None, "a strategy can be bound to only one trader"
        self._trader = trader
        self._respawn()
        return self
        
    def stopRunning(self):
        assert self._impl, "a strategy must be running"
        self._impl = None
        self._trader = None
        self.dispose()
    
    
%(reg)s
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

def wrapper(name, params, register=True):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % mapped(locals()) for (name, ini, typ) in params])
    
    init = process("%(name)s = %(ini)s")
    withini = process("%(name)s = None")
    withbody = process("%(name)s = %(name)s if %(name)s is not None else self.%(name)s", "; ")
    withrv = process("%(name)s")
    dict_= process("self.__dict__[\'%(name)s\'] = %(name)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    call = process("self.%(name)s")
    reg = "registry.insert("+name+"(),'"+name+"')" if register else ""
    
    return template % locals()
