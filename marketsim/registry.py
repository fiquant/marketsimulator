import weakref
import inspect

def meta(frame):
    _, _, _, values = inspect.getargvalues(frame)
    module = inspect.getmodule(frame).__name__
    function = inspect.getframeinfo(frame).function
    constructAs = module + "." + function
    return (dict(values), constructAs)

def expose(f):
    f._properties = None
    f._constructAs = f.__module__ + "." + f.__name__
    return f


class Registry(object):
    
    def __init__(self):
        self._id2obj = weakref.WeakValueDictionary()
        self._counter = 0
        
    def insert(self, obj):
        if '__id' in dir(obj):
            # the object is supposed to be in the dictionary
            # so we just check this
            Id = obj.__id
            assert Id in self._id2obj
            assert self._id2obj[Id] == obj
            return Id 
        else:
            obj.__id = self._counter
            self._id2obj[self._counter] = obj
            self._counter += 1
            return obj.__id
        
    def _tojson(self, value):
        typ = type(value)
        if typ is int or typ is float or typ is bool or typ is str:
            return value
        if typ is list:
            return [self._tojson(x) for x in value]
        # other sequences we'll consider later
        # so value is a class instance
        return "#" + str(self.insert(value))  
        
    def dump(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None
        
        if '_constructAs' in dir(obj):
            ctor = obj._constructAs
        else:
            cls = obj.__class__
            ctor = cls.__module__ + "." + cls.__name__            
            
        properties = {}
        
        if '_properties' in dir(obj):
            if obj._properties:
                for k in obj._properties: 
                    properties[k] = self._tojson(getattr(obj, k))
            else:
                properties = None
        else:
            print "object " + str(obj) + " doesn't have field _properties."
        
        
        return [ctor, properties] if properties is not None else [ctor]
                
    def dumpall(self):
        rv = {}
        
        def visit_if_ref(p):
            if type(p) is str and p[0] == "#":  # if a field is class instance
                p_id = int(p[1:])               # getting id of its value
                visit(p_id)                     # and recursively visit it

        def visit(k_id):
            """ Processes an object with id = k_id
            """
            if k_id not in rv: # check that it hasn't been yet processed
                dumped = self.dump(k_id)    # getting dump representation
                rv[k_id] = dumped           # storing it in the dictionary
                if len(dumped) > 1:         # if it has properties
                    for p in dumped[1].itervalues():        # iterating its fields
                        visit_if_ref(p)
                        if type(p) is list:                 # if a field is list (other sequences are to be processed in future)
                            for e in p:                     # for each its element
                                visit_if_ref(e)
                                
        for k_id in list(self._id2obj.iterkeys()): # getting initial set of the dictionary keys
            visit(k_id)
            
        return rv
                        
instance = Registry()                
         
        
        
    