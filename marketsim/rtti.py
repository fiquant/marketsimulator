import inspect, collections

class property_descriptor(collections.namedtuple("property_descriptor", 
                                                 ["name", 
                                                  "type", 
                                                  "hidden", 
                                                  "collapsed"
                                                  ])):
    
    @property
    def isHidden(self):
        return self.hidden or self.name[0] == '_'

def usedTypes(T):
    
    ret = [T]
    
    if 'usedTypes' in dir(T):
        ret += T.usedTypes()
        
    return ret

def usedConstraints(T):

    ret = [T]
    
    if 'usedConstraints' in dir(T):
        ret += T.usedConstraints()
        
    return ret

def pack_property(n, t, *args):
    d = { 
            'name' : n, 
            'type' : t, 
            'hidden' : False, 
            'collapsed' : False
        }
    for a in args:
        a(d)
    return property_descriptor(**d)

def _checkPropertiesAreUnique(props, cls):
    
    s = {}
    
    for p in props:   
        if p.name in s and s[p.name] != p.type:
            print p.name, ' is not unique in ', props, ' at ', cls
            assert p.name not in s
        s[p.name] = p.type
        
    return props
            

def properties_t(cls):
    
    rv = []
    assert inspect.isclass(cls), "only classes may have properties - functions are considered as literals"
    bases = inspect.getmro(cls)
    
    for base in reversed(bases):
        if '_properties' in dir(base):
            props = base._properties
            if type(props) is dict:
                for k,v in props.iteritems():
                    args = (k,v) if type(v) != tuple else (k,) + v
                    rv.append(pack_property(*args))
            if type(props) is list:
                rv.extend(map(lambda p: pack_property(*p), props))
                
    return _checkPropertiesAreUnique(rv, cls)            


def properties(obj):
    return properties_t(type(obj))

def children_to_visit(obj):
    return obj._children_to_visit if '_children_to_visit' in dir(obj) else []
                
def internals(obj):
    
    cls = type(obj)
    rv = set()
    assert inspect.isclass(cls), "only classes may have properties - functions are considered as literals"
    bases = inspect.getmro(cls)
    
    for base in reversed(bases):
        if '_internals' in dir(base):
            for x in base._internals:
                rv.add(x)
                
    return rv

def types(obj):

    bases = inspect.getmro(type(obj))
    
    rv = set([] if '_types' not in dir(obj) else obj._types)
    
    for base in reversed(bases):
        if not base is object:
            if '_types' in dir(base):
                for x in base._types:
                    rv.add(x)
            rv.add(base)
            
    return list(rv)


def is_object(obj):      

    typ = type(obj)
    return not (typ is int or typ is float or typ is bool or typ is str)

def children(obj, logger):
    
    for name, value in getattr(obj, '_definitions', {}).iteritems():
        logger('$(' + name + ')')
        yield value
    
    for propname in internals(obj):
        logger(propname)
        yield getattr(obj, propname)
        
    for child in children_to_visit(obj):
        yield child

    for p in properties(obj):
        if p.name[0] != '_':
            logger(p.name)
            yield getattr(obj, p.name)
 
    if '_subscriptions' in dir(obj):
        yield obj._subscriptions

import marketsim 

def typecheck(constraint, obj):
    """ Checks that *obj* meets *constraint* for an object field
    """
    def throw():
        from marketsim import exception
        raise exception.Constraint(constraint, obj)
    
    if type(obj) is marketsim.Reference:
        if obj.pointee:
            typecheck(constraint, obj.pointee)
    elif constraint == marketsim.Side:
         if obj not in [marketsim.Side.Sell, marketsim.Side.Buy]:
             throw()
    elif constraint == None:
             throw()
    elif constraint == str:
         if type(obj) != str:
             throw()
    elif constraint == int:
         if type(obj) != int:
             throw()
    elif constraint == float:
         if type(obj) not in [float, int]:
             throw()
    elif 'check_constraint' in dir(constraint):
        constraint.check_constraint(obj)
    else:
        if constraint not in types(obj):
             throw()

def can_be_casted(obj, constraint):
    from marketsim import exception
    try:
        typecheck(constraint, obj)
        return True
    except exception.Constraint:
        return False

        
def check_fields(obj):
    for p in properties(obj):
        typecheck(p.type, getattr(obj, p.name))
