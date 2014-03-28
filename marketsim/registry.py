import weakref, inspect, sys

from marketsim import (constraints, exception, rtti, scheduler,
                       meta, utils, context)

from marketsim.gen._out._side import Side

startup = []

def isProxy(s):
    s.find('Proxy') != -1 or s.find("OfTrader") != -1

def union(*dicts):
    return dict(sum(map(lambda dct: list(dct.items()), dicts), []))

def getCtorT(cls):
    return getattr(cls, 
                   '_constructAs', 
                   cls.__module__ + "." + cls.__name__) 

def getCtor(obj): 
    if inspect.isfunction(obj):
        return getCtorT(obj)
    return getCtorT(obj.__class__) 

def getObjRef(value):
    if type(value) in [str, unicode] and len(value) > 1:
        if value[0] == '#' and value[1] != "#":
            return int(value[1:])
    return -1

def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

class ListProxy(object):
    
    def __init__(self, **kwargs):
        if 'elements' in kwargs and  'elementConstraint' in kwargs:
            elements = kwargs['elements']
            elementConstraint = kwargs['elementConstraint']
            self.__dict__['_elements'] = elements
            self.__dict__['_elementConstraint'] = elementConstraint
            self.__dict__['_properties'] = dict([(str(i), self._elementConstraint) \
                                                 for i in range(len(self.__dict__['_elements']))])
        
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


import marketsim

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
        for s in startup:
            s(self)
        self.pushAllReferences()
                
    def _findAlias(self, obj):
        t = type(obj)
        if '_alias' in dir(obj):
            return obj._alias
        for x in self._id2obj.itervalues():
            if type(x) == t and '_alias' in dir(x) and x._alias != []:
                return x._alias
        return [obj.__class__.__name__]
        
    def _insertNew(self, Id, obj):
        if type(Id) != int:
            a = 12
        assert type(Id) == int
        if Id in self._id2obj:
            old = self._id2obj[Id]
            del old._id
            del old._referencedBy
        obj._id = Id
        obj._referencedBy = set()
        self._id2obj[Id] = obj
        return obj._id
    
    def reset(self):
        # it is a dirty hack and later we'll have to 
        # store complete object graph in the registry (not only properties)
        scheduler.current()._reset()
        for x in self._id2obj.itervalues():
            if 'reset' in dir(x):
                x.reset()
                
    def save_state_before_changes(self):
        self._id2savedfields = {}
        for k,v in self._id2obj.iteritems():
            fields = {}
            for p in rtti.properties(v):
                x = getattr(v, p.name)
                if context.primitive(type(x)):
                    # we'd better to check here also that this field is "mutable"
                    fields[p.name] = x
            if fields != {}:
                self._id2savedfields[k] = fields
                
    def get_changes(self):
        changes = []
        for k,v in self._id2obj.iteritems():
            if k in self._id2savedfields:
                saved = self._id2savedfields[k]
                for p in rtti.properties(v):
                    x = getattr(v, p.name)
                    if context.primitive(type(x)):
                        # we'd better to check here also that this field is "mutable"
                        if x != saved[p.name]:
                            changes.append((k, p.name, x))
        return changes
        
    
    def get(self, id):
        return self._id2obj[id]
        
    def insert(self, obj):
        if '_id' in dir(obj):
            # the object is supposed to be in the dictionary
            # so we just check this
            Id = obj._id
            if Id not in self._id2obj:
                self._insertNew(Id, obj)
            else:
                if self._id2obj[Id] is not obj:
                    if self._id2obj[Id]._id != obj._id:
                        a = 12
                    else:
                        self._id2obj[Id] = obj
            return Id 
        else:
            return self._insertNew(self.getUniqueId(), obj)

    def getUniqueId(self):
        while self._counter in self._id2obj:
            self._counter += 1  # looking for a next free id
        return self._counter
        
    def setAttr(self, Id, propname, value):
        obj = self._id2obj[Id]
        
        if propname == '_alias':
            obj._alias = value
            return
        
        props = rtti.properties(obj)
        # try:
        value = self._convert(props, propname, value)
        # except: 

        setattr(obj, propname, value)

    def _convert(self, dst_properties, k, v):
        
        def lookup(id):
            if '_metaToCreate' in dir(self):
                self.createFromMetaEx(id)                    
            return self._id2obj[id]
        
        id = getObjRef(v)
        if id != -1:
            v = lookup(id)
            
        if type(v) == list:
            for i in range(len(v)):
                id = getObjRef(v[i])
                if id != -1:
                    v[i] = lookup(id)
                # we should check that all elements meet the constraint
            return v
        
        for p in dst_properties:
            if p.name == k:        
                typeinfo = p.type
        
        if typeinfo in rtti.types(v):
            return v
       
        if inspect.isclass(typeinfo) and issubclass(type(v), typeinfo):
            # we just checked that our object is a subclass for the constraint
            return v# so we may leave it
        
        if '_casts_to' in dir(v):
            if not v._casts_to(typeinfo):
                a = 1
            assert v._casts_to(typeinfo)
            return v

        if typeinfo is not None: # consider it as a converter
            return typeinfo(v)
        
        return v
    
    def createFromMeta(self, Id, meta):
        """ Creates a new object from meta information 
        Id should be a unique number
        meta - an array of length 2 containing constructor name and parameters dictionary
        """
        if len(meta) == 3:
            ctorname, props, alias = meta
        elif len(meta) == 2:
            ctorname, props = meta
            alias = None
        else:
            assert 'wrong meta'
        ctor = _findType(ctorname)
        if ctorname == 'marketsim.Side._SellSide':
            obj = Side.Sell
        elif ctorname == 'marketsim.Side._BuySide':
            obj = Side.Buy
        elif inspect.isclass(ctor):
            dst_properties = rtti.properties_t(ctor)
            converted = dict()
            for k,v in props.iteritems():
                converted[k] = self._convert(dst_properties, k, v)
            obj = ctor(**converted)
            if alias is not None:
                obj._alias = alias
        else:
            assert inspect.isfunction(ctor)
            obj = ctor
        self._insertNew(Id, obj)
        return obj
    
    def createFromMetaEx(self, Id):
        if Id in self._metaToCreate and self._metaToCreate[Id] is not None:
            meta = self._metaToCreate[Id]
            self._metaToCreate[Id] = None
            self.createFromMeta(Id, meta)
    
    def createNewObjects(self, metaToCreate):
        self._metaToCreate = metaToCreate
        for Id in self._metaToCreate.iterkeys():
            self.createFromMetaEx(Id)
        del self._metaToCreate
        
    def _dumpPropertyValue(self, constraint, value, parent):
        typ = type(value)
        if typ is str:
            return "#"+value if len(value) and value[0]=="#" else value
        if context.primitive(typ):
            return value
        if typ is list:
            elementType = constraint.elementType if type(constraint) == meta.listOf else None
            return [self._dumpPropertyValue(elementType, x, parent) for x in value]
            #value = ListProxy(value, elementType)

        # other sequences we'll consider later
        # so value is a class instance

        Id = self.insert(value)
        value._referencedBy.add(parent)
        
        return "#" +  str(Id)

    def ofType(self, baseclass):
        return [k for (k,v) in self._id2obj.iteritems()\
                 if isinstance(v, baseclass) and not isProxy(getCtor(v))]
    
    def valuesOfType(self, baseclass):
        return [v for v in self._id2obj.itervalues()\
                 if isinstance(v, baseclass) and not isProxy(getCtor(v))]
    
    @property
    def traders(self):
        from marketsim.gen._out._iaccount import IAccount
        return self.ofType(IAccount)
    
    @property
    def books(self):
        from marketsim.gen._out._iorderbook import IOrderBook
        return self.ofType(IOrderBook)
    
    @property
    def orderBooksByName(self):
        return dict([(v._alias[-1], v)\
                 for v in self._id2obj.itervalues() \
                    if getCtor(v).startswith("marketsim.orderbook.") ])
    
    @property
    def graphs(self):
        return self.ofType("marketsim.js.Graph")
        
    def _dumpPropertyConstraint(self, constraint):
        from marketsim.side_ import Tag as Side
        if isinstance(constraint, Side):
            return "marketsim.side_.Tag" # TODO: generic procedure to treat modules
        if constraint is None or constraint == str:
            return 'identity'
        if constraint == int:
            return "_parseInt"
        if constraint == float:
            return "_parseFloat"
        if 'toJS' in dir(constraint):
            return constraint.toJS()(self._dumpPropertyConstraint)
        return getCtorT(constraint)
    
        
    def typecheck(self):
        for obj in self._id2obj.itervalues():
            for p in rtti.properties(obj):
                try:
                    rtti.typecheck(p.type, getattr(obj, p.name))
                except exception.Constraint, err:
                    print err
                    print '    at ', repr(obj), '.', p.name
                    #rtti.typecheck(p.type, getattr(obj, p.name))

    def getUsedTypes(self):
        types = set()
        usedTypes = set()
        constraints = {}
        
        for obj in self._id2obj.itervalues():
            if type(obj) not in types:
                types.add(type(obj))
                for p in rtti.properties(obj):
                    for t in rtti.usedTypes(p.type):
                        usedTypes.add(t)
                    for t in rtti.usedConstraints(p.type):
                        constraints[t] = set()
                    
        return usedTypes, constraints
        

    def getTypeInfo(self):
        self.pushAllReferences()
        types = {}
        usedTypes, constraints = self.getUsedTypes()
        
        with utils.rst.Cache():
        
            for obj in self._id2obj.itervalues():
                
                ctor = getCtor(obj)
                    
                if ctor not in types:
    
                    props = dict([( p.name, 
                                union({'type'      : self._dumpPropertyConstraint(p.type) },
                                     ({'hidden'    : True} if p.isHidden else {}), 
                                     ({'collapsed' : True} if p.collapsed else {}))) 
                                for p in rtti.properties(obj)])
                    
                    castsTo = filter(lambda t: t in usedTypes, rtti.types(obj))
                    
                    for t in castsTo:
                        constraints[t].add(ctor)
        
                    castsTo = map(self._dumpPropertyConstraint, castsTo)
                        
                    types[ctor] = { "castsTo"      : sorted(castsTo), 
                                    "properties"   : props, 
                                    "description"  : utils.rst2html(trim(obj.__doc__)) }
        
        for constraint, matching_types in constraints.iteritems():
            if self.objectConstraint(constraint):
                if len(matching_types) == 0:
                    print "No types matching to constraint ", constraint
        
        return types, constraints

    def objectConstraint(self, constraint):
        if context.primitive(constraint):
            return False
        
        if type(constraint) in [meta.listOf]:
            return False
        
        if isinstance(constraint, constraints.IConstraint):
            return False
        
        return True
        
    
    def getObjectsForAliases(self):
        """ Creates mapping: typename -> (alias -> listOf(id))
        """

        typesToAliasesToObjects = {}
        processedTypes = set()
        
        for (k_id, obj) in self._id2obj.iteritems(): 
            
            ctor = getCtor(obj)
            
            if ctor not in typesToAliasesToObjects:
                typesToAliasesToObjects[ctor] = {}
                
            aliasToIds = typesToAliasesToObjects[ctor]
            
            alias = "|".join(obj._alias)
            
            if alias not in aliasToIds:
                aliasToIds[alias] = []
            
            aliasToIds[alias].append(k_id)
            
        return typesToAliasesToObjects
        
    
    def tojson(self, Id):
        
        def impl(obj):
            if obj is None:
                return None
            ctor = getCtor(obj)
                
            if '_alias' not in dir(obj):
                obj._alias = self._findAlias(obj)
                
            alias = obj._alias
                
            props     = dict([(p.name, self._dumpPropertyValue(p.type, getattr(obj, p.name), obj)) \
                                               for p in rtti.properties(obj)])
                                     
            if props is None:
                props = {}
                
            return [ctor, props, alias, {}]
        
        return impl(self._id2obj.get(Id))
    
    def pushAllReferences(self):
        visited = set()
        root = list(self._id2obj.itervalues())                        
        for obj in root: # getting initial set of the dictionary keys
            context.assureAllReferencedAreRegistred(self, obj, visited)
            
    def tojsonall(self):

        self.pushAllReferences()
        
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
                    visit_if_ref(p)
        
        root = list(self._id2obj.iteritems())                        
        for (k_id, obj) in root: # getting initial set of the dictionary keys
            visit(k_id)
            
        return rv
        
        
    def dump(self, Id):
        obj = self._id2obj.get(Id)
        if obj is None:
            return None

        ctor = getCtor(obj)
            
        props     = dict([(p.name, (p.type, self._dumpPropertyValue(p.type, getattr(obj, p.name), obj))) \
                                                for p in rtti.properties(obj)])
        
        return [ctor, props]
                
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

import traceback

def expose(alias, constructor=None, args = None):
    def inner(f):
        if inspect.isclass(f) or args is not None:
            def inner(instance):
                try:
                    obj = f() if args is None else f(*args)
                except Exception, err:
                    print "Exposing ", f, "failed: ", err,
                    traceback.print_exc()

                obj._alias = alias
                instance.insert(obj)
            startup.append(inner)
        elif inspect.isfunction(f):
            f._constructAs = constructor if constructor else f.__module__ + "." + f.__name__
            f._alias = alias
            startup.append(lambda instance: instance.insert(f))
        return f
    return inner

from marketsim.gen._out._itrader import ITrader
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._igraph import IGraph

class Simulation(object):
    
    def __init__(self, traders = [], orderbooks = [], graphs = []):
        self._traders = traders
        self.orderbooks = orderbooks
        self.graphs = graphs
    
    _properties = { 'traders'    : meta.listOf(ITrader),
                    'orderbooks' : meta.listOf(IOrderBook),
                    'graphs'     : meta.listOf(IGraph) }
    
    @property
    def traders(self):
        return self._traders
    
    @traders.setter
    def traders(self, newtraders):
        
        for oldtrader in set(self._traders) - set(newtraders):
            oldtrader.dispose()
            
        self._traders = newtraders

def createSimulation(instance):
    instance.pushAllReferences()
    from marketsim.gen._out.trader._singleasset import SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie as SingleAsset
    traders = instance.valuesOfType(SingleAsset)

    from marketsim.gen._out.orderbook._local import Local_StringFloatIntListITimeSerie as Local
    orderbooks = instance.valuesOfType(Local)

    from marketsim.js import Graph
    graphs = instance.valuesOfType(Graph)
    return Simulation(traders, orderbooks, graphs)

def create():
    return Registry()
