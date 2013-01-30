import weakref
import inspect
import marketsim
from functools import reduce


## {{{ http://code.activestate.com/recipes/578272/ (r1)
def toposort2(data):
    """Dependencies are expressed as a dictionary whose keys are items
and whose values are a set of dependent items. Output is a list of
sets in topological order. The first set consists of items with no
dependences, each subsequent set consists of items that depend upon
items in the preceeding sets.

>>> print '\\n'.join(repr(sorted(x)) for x in toposort2({
...     2: set([11]),
...     9: set([11,8]),
...     10: set([11,3]),
...     11: set([7,5]),
...     8: set([7,3]),
...     }) )
[3, 5, 7]
[8, 11]
[2, 9, 10]

"""

    # Ignore self dependencies.
    for k, v in data.items():
        v.discard(k)
    # Find all items that don't depend on anything.
    extra_items_in_deps = reduce(set.union, data.itervalues()) - set(data.iterkeys())
    # Add empty dependences where needed
    data.update({item:set() for item in extra_items_in_deps})
    while True:
        ordered = set(item for item, dep in data.iteritems() if not dep)
        if not ordered:
            break
        yield ordered
        data = {item: (dep - ordered)
                for item, dep in data.iteritems()
                    if item not in ordered}
    assert not data, "Cyclic dependencies exist among these items:\n%s" % '\n'.join(repr(x) for x in data.iteritems())
## end of http://code.activestate.com/recipes/578272/ }}}


def meta(frame):
    _, _, _, values = inspect.getargvalues(frame)
    module = inspect.getmodule(frame).__name__
    function = inspect.getframeinfo(frame).function
    constructAs = module + "." + function
    return (dict(values), constructAs)

def properties_t(cls):
    bases = inspect.getmro(cls)
    rv = {}
    
    for base in reversed(bases):
        if '_properties' in dir(base):
            for k,v in base._properties.iteritems():
                rv[k] = v
                
    return rv            


def properties(obj):
    cls = type(obj)
    rv = properties_t(cls)
    
    if '_properties' in dir(obj):
        if obj._properties:
            for k,v in obj._properties.iteritems():
                rv[k] = v 
        else:
            rv = None
    else:
        print "object " + str(obj) + " doesn't have field _properties."
    
    return rv            
                
def getCtor(obj): 
    if '_constructAs' in dir(obj):
        ctor = obj._constructAs
    else:
        cls = obj.__class__
        ctor = cls.__module__ + "." + cls.__name__
    return ctor

def getObjRef(value):
    if type(value) == str and len(value) > 1:
        if value[0] == '#' and value[1] != "#":
            return int(value[1:])
    return -1
            

class Registry(object):
    
    def __init__(self):
        self._id2obj = dict() #weakref.WeakValueDictionary()
        self._initial = dict()
        self._counter = 0
        
    def _insertNew(self, Id, obj):
        if id in self._id2obj:
            old = self._id2obj[id]
            del old._id
            del old._referencedBy
        obj._id = Id
        obj._referencedBy = weakref.WeakSet()
        self._id2obj[Id] = obj
        self._initial[Id] = self.dump(Id)
        return obj._id
    
    def _toposort(self, objects):
        """
        object - list of pairs (id, meta) of objects to create
                 where meta is pair (ctor, properties)
                     where ctor is a type name to instantiate (should be in marketsim module)
                     properties is a dictionary property_name -> property_value_representation
                     property_value_representation may be either a reference to an object of form #id
                     or a number or a string
        """
        children = {}
        for id, meta in objects:
            if len(meta) == 2: # it is a createable object
                ctor, props = meta
                children[id] = set()
                for (_, (_, value)) in props.iteritems():
                    child = getObjRef(value)
                    if child != -1:
                        children[id].add(child)
                    if type(value) == list:
                        for v in value:
                            child = getObjRef(v)
                            if child != -1:
                                children[id].add(child)
                                
        return toposort2(children)
                
    
    def reset(self):
        ordered = self._toposort(list(self._initial.iteritems()))
        for outer in ordered:
            for id in outer:
                meta = self._initial[id]
                if len(meta) == 2:
                    ctor, props = self._initial[id]
                    props = dict([(name, value) for (name, (_, value)) in props.iteritems()])
                    self.createFromMeta(id, (ctor, props))               
    
    def get(self, id):
        return self._id2obj[id]
        
    def insert(self, obj):
        if '_id' in dir(obj):
            # the object is supposed to be in the dictionary
            # so we just check this
            Id = obj._id
            assert Id in self._id2obj
            assert self._id2obj[Id] == obj
            return Id 
        else:
            return self._insertNew(self.getUniqueId(), obj)

    def getUniqueId(self):
        while self._counter in self._id2obj:
            self._counter += 1  # looking for a next free id
        return self._counter
        
    def setAttr(self, Id, propname, value):
        obj = self._id2obj[Id]
        props = properties(obj)
        # try:
        value = self._convert(props, propname, value)
        # except: 
        
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
        
    def _convert(self, dst_properties, k, v):
        id = getObjRef(v)
        if id != -1:
            v = self._id2obj[id]
            
        if type(v) == list:
            for i in range(len(v)):
                id = getObjRef(v[i])
                if id != -1:
                    v[i] = self._id2obj[id]
                
        typeinfo = dst_properties[k]
        
        if '_casts_to' in dir(v):
            if not v._casts_to(typeinfo):
                a = 1
            assert v._casts_to(typeinfo)
            return v
        
       
        if inspect.isclass(typeinfo) and issubclass(type(v), typeinfo):
            # we just checked that our object is a subclass for the constraint
            return v# so we may leave it
        
        if typeinfo is not None: # consider it as a converter
            return typeinfo(v)
        
        return v
        
        
    def createFromMeta(self, Id, meta):
        """ Creates a new object from meta information 
        Id should be a unique number
        meta - an array of length 2 containing constructor name and parameters dictionary
        """
        assert len(meta) == 2
        ctorname, props = meta
        qualified_name = ctorname.split('.')
        assert qualified_name[0] == 'marketsim', "We may create only marketsim types"
        ctor = globals()['marketsim']
        for k in qualified_name[1:]:
            ctor = getattr(ctor, k)
        dst_properties = properties_t(ctor)
        converted = dict()
        for k,v in props.iteritems():
            converted[k] = self._convert(dst_properties, k, v)
        obj = ctor(**converted)
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

    def ofType(self, prefix):
        return [k for (k,v) in self._id2obj.iteritems() if getCtor(v).startswith(prefix)]
    
    @property
    def traders(self):
        return self.ofType("marketsim.trader.")
    
    @property
    def books(self):
        return self.ofType("marketsim.orderbook.")
    
    @property
    def graphs(self):
        return self.ofType("marketsim.js.Graph")
    
    def tojson(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None
        if '_constructAs' in dir(obj):
            ctor = obj._constructAs
        else:
            cls = obj.__class__
            ctor = cls.__module__ + "." + cls.__name__
            
        label = obj.jsLabel if 'jsLabel' in dir(obj) else\
                obj.label if 'label' in dir(obj) else\
                repr(obj)            
            
        propnames = properties(obj)
        props     = dict([(k, self._dumpPropertyValue(getattr(obj, k), obj)) \
                                           for k,v in propnames.iteritems()])\
                     if propnames is not None else None
        
        return [ctor, props, label] if props is not None else [ctor, {}, label]
    
    def tojsonall(self):
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
                dumped = self.tojson(k_id)    # getting dump representation
                rv[k_id] = dumped           # storing it in the dictionary
                for p in dumped[1].itervalues():        # iterating its fields
                    visit_if_ref(p)
                    if type(p) is list:                 # if a field is list (other sequences are to be processed in future)
                        for e in p:                     # for each its element
                            visit_if_ref(e)
                                
        for k_id in list(self._id2obj.iterkeys()): # getting initial set of the dictionary keys
            visit(k_id)
            
        return rv
        
        
    def dump(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None

        ctor = getCtor(obj)
            
        propnames = properties(obj)
        props     = dict([(k, (v, self._dumpPropertyValue(getattr(obj, k), obj))) \
                                                for k,v in propnames.iteritems()])\
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
                    for _,p in dumped[1].itervalues():        # iterating its fields
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
        
def new(name, fields):
    return instance.createFromMeta(instance.getUniqueId(), 
                                            [name, fields])
    
def setAttr(obj, name, value):
    instance.setAttr(instance.insert(obj), name, value)
    
def insert(obj):
    instance.insert(obj)
    
def dump(objId):
    return instance.dump(objId)
    
def dumpall():
    return instance.dumpall()


# Naming service

uniqueNames = dict()

def uniqueName(s):
    base, _, suffix = s.rpartition("#")
    if base == "":
        base = suffix
        suffix = ""
    sbase = base.strip()
    if sbase not in uniqueNames:
        uniqueNames[sbase] = set()
        return s
    ssuffix = suffix.strip()
    usednames = uniqueNames[sbase]
    if ssuffix in usednames or ssuffix == "":
        suffix = ssuffix = str(len(usednames))
    usednames.add(ssuffix)
    return base + "#" + suffix