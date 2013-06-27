import inspect, collections

class property_descriptor(collections.namedtuple("property_descriptor", 
                                                 ["name", 
                                                  "type", 
                                                  "hidden", 
                                                  "collapsed"
                                                  ])):
    
    pass

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

       
        
