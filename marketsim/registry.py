import weakref
import inspect
import marketsim
from functools import reduce

from marketsim import Side

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
    
    rv = {}
    assert inspect.isclass(cls), "only classes may have properties - functions are considered as literals"
    bases = inspect.getmro(cls)
    
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
    
    return rv            
                
def getCtor(obj): 
    if '_constructAs' in dir(obj):
        ctor = obj._constructAs
    else:
        cls = obj.__class__
        ctor = cls.__module__ + "." + cls.__name__
    return ctor

def getObjRef(value):
    if type(value) in [str, unicode] and len(value) > 1:
        if value[0] == '#' and value[1] != "#":
            return int(value[1:])
    return -1

class ListProxy(object):
    
    def __init__(self, **kwargs):
        if 'elements' in kwargs and  'elementConstraint' in kwargs:
            elements = kwargs['elements']
            elementConstraint = kwargs['elementConstraint']
            self.__dict__['_elements'] = elements
            self.__dict__['_elementConstraint'] = elementConstraint
            self.__dict__['_properties'] = {str(i) : self._elementConstraint for i in range(len(self.__dict__['_elements']))}
        
    def __getattr__(self, s):
        try:
            return self.__dict__['_elements'][int(s)]
        except ValueError:
            return self.__dict__[s]
    
    def __setattr__(self, s, value):
        try:
            self.__dict__['_elements'][int(s)] = value
        except ValueError:
            self.__dict__[s] = value



def _findType(ctorname):    
    qualified_name = ctorname.split('.')
    assert qualified_name[0] == 'marketsim', "We may create only marketsim types"
    ctor = globals()['marketsim']
    for k in qualified_name[1:]:
        ctor = getattr(ctor, k)
    return ctor
    

class Registry(object):
    
    def __init__(self):
        self._id2obj = dict() #weakref.WeakValueDictionary()
        self._counter = 0
        self._id2savedfields = {}
        
    def _findAlias(self, obj):
        t = type(obj)
        if '_alias' in dir(obj):
            return obj._alias
        for x in self._id2obj.itervalues():
            if type(x) == t and '_alias' in dir(x) and x._alias != "":
                return x._alias
        return obj.__class__.__name__
        
    def _insertNew(self, Id, obj):
        if type(Id) != int:
            a = 12
        assert type(Id) == int
        if id in self._id2obj:
            old = self._id2obj[id]
            del old._id
            del old._referencedBy
        obj._id = Id
        obj._referencedBy = weakref.WeakSet()
        obj._alias = self._findAlias(obj)
        self._id2obj[Id] = obj
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
        # it is a dirty hack and later we'll have to 
        # store complete object graph in the registry (not only properties)
        marketsim.scheduler.current()._reset()
        for x in self._id2obj.itervalues():
            if 'reset' in dir(x):
                x.reset()
                
    def save_state_before_changes(self):
        self._id2savedfields = {}
        for k,v in self._id2obj.iteritems():
            fields = {}
            for pname in (properties(v) or []):
                x = getattr(v, pname)
                if type(x) == int or type(x) == float or type(x) == str:
                    # we'd better to check here also that this field is "mutable"
                    fields[pname] = x
            if fields != {}:
                self._id2savedfields[k] = fields
                
    def get_changes(self):
        changes = []
        for k,v in self._id2obj.iteritems():
            if k in self._id2savedfields:
                saved = self._id2savedfields[k]
                for pname in properties(v):
                    x = getattr(v, pname)
                    if type(x) == int or type(x) == float or type(x) == str:
                        # we'd better to check here also that this field is "mutable"
                        if x != saved[pname]:
                            changes.append((k, pname, x))
        return changes
        
    
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
                # we should check that all elements meet the constraint
            return v
                
        typeinfo = dst_properties[k]
        
        if '_casts_to' in dir(v):
            if not v._casts_to(typeinfo):
                a = 1
            assert v._casts_to(typeinfo)
            return v
        
        if '_types' in dir(v) and typeinfo in v._types:
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
        ctor = _findType(ctorname)
        if ctorname == 'marketsim.Side._SellSide':
            obj = Side.Sell
        elif ctorname == 'marketsim.Side._BuySide':
            obj = Side.Buy
        elif inspect.isclass(ctor):
            dst_properties = properties_t(ctor)
            converted = dict()
            for k,v in props.iteritems():
                converted[k] = self._convert(dst_properties, k, v)
            obj = ctor(**converted)
        else:
            assert inspect.isfunction(ctor)
            obj = ctor
        self._insertNew(Id, obj)
        return obj
        
    def _dumpPropertyValue(self, constraint, value, parent):
        typ = type(value)
        if typ is int or typ is float or typ is bool:
            return value
        if typ is str:
            return "#"+value if len(value) and value[0]=="#" else value
        if typ is list:
            elementType = constraint.elementType if type(constraint) == marketsim.meta.listOf else None
            return [self._dumpPropertyValue(elementType, x, parent) for x in value]
            #value = ListProxy(value, elementType)

        # other sequences we'll consider later
        # so value is a class instance

        Id = self.insert(value)
        value._referencedBy.add(parent)
        
        return "#" +  str(Id)

    def assureAllReferencedAreRegistred(self, obj):
        typ = type(obj)
        if typ is int or typ is float or typ is bool or typ is str:
            return 
        
        if typ is list:
            for x in obj:
                self.assureAllReferencedAreRegistred(x)
        else:
            self.insert(obj)
            
            propnames = properties(obj)
            if propnames is None:
                propnames = {}
                
            for propname in propnames.iterkeys():
                self.assureAllReferencedAreRegistred(getattr(obj, propname))        

    def ofType(self, prefix):
        return [k for (k,v) in self._id2obj.iteritems() if getCtor(v).startswith(prefix)]
    
    def valuesOfType(self, prefix):
        return [v for v in self._id2obj.itervalues() if getCtor(v).startswith(prefix)]
    
    @property
    def traders(self):
        return self.ofType("marketsim.trader.")
    
    @property
    def books(self):
        return self.ofType("marketsim.orderbook.")
    
    @property
    def graphs(self):
        return self.ofType("marketsim.js.Graph")
    
    def _dumpPropertyConstraint(self, constraint):
        if constraint == marketsim.Side:
            return "marketsim.Side" # TODO: generic procedure to treat modules 
        if constraint == None or constraint == str:
            return 'identity'
        if constraint == int:
            return "_parseInt"
        if constraint == float:
            return "_parseFloat"
        if 'toJS' in dir(constraint):
            return constraint.toJS()(self._dumpPropertyConstraint)
        if '_constructAs' in dir(constraint):
            ctor = constraint._constructAs
        else:
            ctor = constraint.__module__ + "." + constraint.__name__
        return ctor
    
    def tojson(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None
        if '_constructAs' in dir(obj):
            ctor = obj._constructAs
        else:
            cls = obj.__class__
            ctor = cls.__module__ + "." + cls.__name__
            
        alias = obj._alias
            
        propnames = properties(obj)
        props     = dict([(k, 
                           (self._dumpPropertyValue(v, getattr(obj, k), obj), 
                            self._dumpPropertyConstraint(v))) \
                                           for k,v in propnames.iteritems()])\
                     if propnames is not None else None
                     
        if '_types' in dir(obj):
            assert len(obj._types) == 1
            typ = self._dumpPropertyConstraint(obj._types[0])
        else:
            typ = ctor
            
        if props is None:
            props = {}
        
        return [ctor, props, typ, alias]
    
    def tojsonall(self):
        
        root = list(self._id2obj.itervalues())                        
        for obj in root: # getting initial set of the dictionary keys
            self.assureAllReferencedAreRegistred(obj)
        
        rv = {}
        
        def visit_if_ref(p):
            if type(p) is str and p[0] == "#":  # if a field is class instance
                try:
                    p_id = int(p[1:])               # getting id of its value
                    assert p_id in self._id2obj, 'cannot get here'
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
                    visit_if_ref(p[0])
        
        root = list(self._id2obj.iteritems())                        
        for (k_id, obj) in root: # getting initial set of the dictionary keys
            visit(k_id)
            
        return rv
        
        
    def dump(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None

        ctor = getCtor(obj)
            
        propnames = properties(obj)
        props     = dict([(k, (v, self._dumpPropertyValue(v, getattr(obj, k), obj))) \
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
         
        
def expose(alias, constructor=None):
    def inner(f):
        f._constructAs = constructor if constructor else f.__module__ + "." + f.__name__
        f._alias = alias
        instance.insert(f)
        return f
    return inner
        
def new(name, fields):
    return instance.createFromMeta(instance.getUniqueId(), 
                                            [name, fields])
    
def setAttr(obj, name, value):
    instance.setAttr(instance.insert(obj), name, value)
    
def insert(obj, alias=None):
    if alias is not None:
        obj._alias = alias
    return instance.insert(obj)
    
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
