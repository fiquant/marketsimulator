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
