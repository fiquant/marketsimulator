import weakref
import inspect
import marketsim

def meta(frame):
    _, _, _, values = inspect.getargvalues(frame)
    module = inspect.getmodule(frame).__name__
    function = inspect.getframeinfo(frame).function
    constructAs = module + "." + function
    return (dict(values), constructAs)

def properties(obj):
    cls = type(obj)
    bases = inspect.getmro(cls)
    rv = []
    
    for base in reversed(bases):
        if '_properties' in dir(base):
            for k in base._properties:
                rv.append(k)
                
    if '_properties' in dir(obj):
        if obj._properties:
            for k in obj._properties:
                rv.append(k) 
        else:
            rv = None
    else:
        print "object " + str(obj) + " doesn't have field _properties."
    
    return rv            
                

class Registry(object):
    
    def __init__(self):
        self._id2obj = weakref.WeakValueDictionary()
        self._counter = 0
        
    def _insertNew(self, Id, obj):
        obj._id = Id
        self._id2obj[Id] = obj
        obj._referencedBy = weakref.WeakSet()
        return obj._id
        
    def insert(self, obj):
        if '_id' in dir(obj):
            # the object is supposed to be in the dictionary
            # so we just check this
            Id = obj._id
            assert Id in self._id2obj
            assert self._id2obj[Id] == obj
            return Id 
        else:
            while self._counter in self._id2obj:
                self._counter += 1  # looking for a next free id
            return self._insertNew(self._counter, obj)
        
    def setAttr(self, Id, propname, value):
        obj = self._id2obj[Id]
        setattr(obj, propname, value)
        
        #notifing all referencees that the object has changed
        visited = set()
        def notify(o):
            for r in o._referencedBy:
                if r not in visited:
                    if '_on_property_changed' in dir(r):
                        r._on_property_changed()
                    notify(r)
        
        notify(obj)
        
    def createFromMeta(self, Id, meta):
        """ Creates a new object from meta information 
        Id should be a unique number
        meta - an array of length 2 containing constructor name and parameters dictionary
        """
        assert Id not in self._id2obj
        assert len(meta) == 2
        ctor, props = meta
        obj = eval(ctor)(**props)
        self._insertNew(Id, obj)
        return obj
        
    def _dumpPropertyValue(self, value, parent):
        typ = type(value)
        if typ is int or typ is float or typ is bool:
            return value
        if typ is str:
            return "#"+value if len(value) and value[0]=="#" else value
        if typ is list:
            return [self._dumpPropertyValue(x, parent) for x in value]
        # other sequences we'll consider later
        # so value is a class instance

        Id = self.insert(value)
        value._referencedBy.add(parent)
        
        return "#" +  str(Id) 
        
    def dump(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None
        
        if '_constructAs' in dir(obj):
            ctor = obj._constructAs
        else:
            cls = obj.__class__
            ctor = cls.__module__ + "." + cls.__name__            
            
        propnames = properties(obj)
        props     = dict([(k, self._dumpPropertyValue(getattr(obj, k), obj)) for k in propnames])\
                     if propnames is not None else None
        
        return [ctor, props] if props is not None else [ctor]
                
    def dumpall(self):
        rv = {}
        
        def visit_if_ref(p):
            if type(p) is str and p[0] == "#":  # if a field is class instance
                try:
                    p_id = int(p[1:])               # getting id of its value
                    visit(p_id)                     # and recursively visit it
                except ValueError:
                    pass

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
         
        
def expose(f):
    f._properties = None
    f._constructAs = f.__module__ + "." + f.__name__
    instance.insert(f)
    return f
        
    