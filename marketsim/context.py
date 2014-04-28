import inspect
from marketsim import bind as _
try:
    import numpy
    has_numpy = True
except:
    has_numpy = False

from marketsim import rtti

debug = False

def is_float(typ):
    if has_numpy:
        if typ is numpy.float64:
            return True
    return typ is int or typ is float

def primitive(typ):
    if has_numpy:
        if typ is numpy.float64:
            return True
    return typ is int or typ is float or typ is bool or typ is str

def is_iterable(obj):
    t = type(obj)
    return t is list or t is set
    
class Base(object):
    
    def __init__(self, indent = 0):
        self.__dict__['_indent'] = indent
        self.log = _.Method(self, '_log_debug') if debug else _.Method(self, '_log_empty')
        
    @property
    def indent(self):
        return self.__dict__['_indent']
    
    def inc(self):
        self.__dict__['_indent'] += 1
        
    def dec(self):
        self.__dict__['_indent'] -= 1
        
    def _log_debug(self, s):
        print "  " * self.indent, s
        
    def _log_empty(self, s):
        pass
    
    def enter(self, obj):
        pass
    
    def exit(self, obj):
        pass
    
    def children(self, obj):
        return rtti.children(obj, self.log)

    def apply(self, obj): 
        
        assert obj is not None
        
        if '_processing' in dir(obj):
            print "recursion!"
        
        typ = type(obj)
        if primitive(typ):
            return 
        
        self.inc()
        
        if is_iterable(obj):
            self.log('[')
            for x in iter(obj):
                self.apply(x)
            self.log(']')
        else:  
            if not self.mark_visited(obj):
                self.log('*')
            else:
                self.inc()
                
                self.log(">>> " + str(type(obj)))

                if type(obj) is tuple:
                    return

                obj._processing = True

                self.enter(obj)
                    
                for child in self.children(obj):
                    self.apply(child)
                
                methods_visited = set()    
                for base in reversed(inspect.getmro(type(obj))):
                    if self._method in dir(base):
                        method = getattr(base, self._method) 
                        if method not in methods_visited:
                            self.do(method, obj)
                            methods_visited.add(method)
                    
                self.exit(obj)
                
                del obj._processing
                        
                self.log("<<< " + str(type(obj)))
                
                self.dec()

        self.dec()

class BindingContextMutable(object):

    def __init__(self, d):
        self.__dict__['_d'] = d.copy()

    def __getattr__(self, item):
        return self.__dict__['_d'][item]

    def __setattr__(self, key, value):
        self.__dict__['_d'][key] = value

import collections

class BindingContextEx(collections.Mapping):
    """ Represents environment for model objects

    Holds references to some outer objects (scheduler, trader in hand, orderbook in hand etc.)
    This class is immutable so its instances can be easily shared.

    """
    def __init__(self, d):
        self._d = d.copy()
        self._hash = None

    def updatedFrom(self, obj):
        if hasattr(obj, 'updateContext_ex'):
            dm = BindingContextMutable(self._d)
            obj.updateContext_ex(dm)
            return  BindingContextEx(dm.__dict__['_d'])
        return self

    def __getattr__(self, item):
        if item[0:2] != '__':
            return self.__getitem__(item)
        else:
            raise AttributeError

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __getitem__(self, key):
        return self._d[key]

    def __hash__(self):
        if self._hash is None:
            self._hash = 0
            for pair in self.iteritems():
                self._hash ^= hash(pair)
        return self._hash


        
class Resetter(Base):
    
    _generation = 0
    
    def __init__(self, indent = 0):
        self._generation = Resetter._generation
        Resetter._generation += 1
        Base.__init__(self, indent)
        
    def mark_visited(self, obj):
        if '_reset_generation' in dir(obj) and obj._reset_generation == self._generation:
            return False
        else:
            try:
                obj._reset_generation = self._generation
            except AttributeError:
                pass
            return True
        
    _method = 'reset'
        
    def do(self, method, obj):       
        method(obj)
                
def reset(obj):
    
    Resetter().apply(obj)
    
class Inserter(Base):
    
    def __init__(self, reg, visited):
        Base.__init__(self)
        self.reg = reg
        self.visited = visited
        
    def mark_visited(self, obj):
        if obj in self.visited:
            return False
        self.visited.add(obj)
        return True
    
    _method = ""
    
    def children(self, obj):
        for p in rtti.properties(obj):
            if not primitive(p.type):
                yield getattr(obj, p.name)
        
    def enter(self, obj):
        self.reg.insert(obj)
    
def assureAllReferencedAreRegistred(reg, obj, visited):
    Inserter(reg, visited).apply(obj)
