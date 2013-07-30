class merge(object):
    def __init__(self, d, **kwargs):
        self.__dict__ = d.__dict__.copy()
        for k in kwargs:
            self.__dict__[k] = kwargs[k]


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

template2 = """
%(reg)s
class %(name)s(_%(name)s_Impl):
    \"\"\" %(docstring)s
    \"\"\"    
    
    def __init__(self, %(init)s):
        self._constructAs = 'marketsim.strategy.%(name)s'
        %(dict_)s
        _%(name)s_Impl.__init__(self)

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