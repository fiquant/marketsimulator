class merge(object):
    def __init__(self, d, **kwargs):
        self.__dict__ = d.__dict__.copy()
        for k in kwargs:
            self.__dict__[k] = kwargs[k]

template = """
class %(name)s(object):
    
    def __init__(self, %(init)s):
        
        %(dict_)s 
        
    _properties = { %(props)s }
    
    def With(self, %(withini)s):
        
        %(withbody)s
        
        return %(name)s(%(withrv)s)
        
    def runAt(self, trader):
        return %(name)s_Running(trader, %(call)s)    
    
class %(name)s_Running(%(name)s):
    
    def __init__(self, trader, %(init)s):
    
        %(name)s.__init__(self, %(withrv)s)
        self._trader = trader
        self._impl = None
        self._respawn()

    def _respawn(self):
        if self._impl is not None:
            self._impl.dispose()
        self._impl = _%(name)s_Impl(self._trader, self)
        
    def __getattr__(self, item):
        if self._impl is not None:
            return getattr(self._impl, item)
        
    def __setattr__(self, item, value):
        self.__dict__[item] = value
        if item in %(name)s_Running._properties:
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

def wrapper(name, params):
    def process(tmpl, sep=", "):
        return sep.join([tmpl % mapped(locals()) for (name, ini, typ) in params])
    
    init = process("%(name)s = %(ini)s")
    withini = process("%(name)s = None")
    withbody = process("%(name)s = %(name)s if %(name)s is not None else self.%(name)s", "; ")
    withrv = process("%(name)s")
    dict_= process("self.__dict__[\'%(name)s\'] = %(name)s", "; ")
    props= process("\'%(name)s\' : %(typ)s")
    call = process("self.%(name)s")
    
    return template % locals()
