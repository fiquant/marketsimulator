import inspect

from marketsim import rtti

debug = False

class Base(object):
    
    def __init__(self, indent = 0):
        self.__dict__['_indent'] = indent
        self.log = self._log_debug if debug else self._log_empty
        
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

    def apply(self, obj): 
        typ = type(obj)
        if typ is int or typ is float or typ is bool or typ is str:
            return 
        
        self.inc()
        
        if typ is set:
            self.log('{')
            for x in obj:
                self.apply(x)
            self.log('}')
        elif typ is list:
            self.log('[')
            for x in obj:
                self.apply(x)
            self.log(']')
        else:
            if not self.mark_visited(obj):
                self.log('*')
            else:
                self.inc()
                
                self.log(">>> " + str(type(obj)))

                self.enter(obj)
                    
                for child in rtti.children(obj, self.log):
                    self.apply(child)
                    
                for base in reversed(inspect.getmro(type(obj))):
                    if self._method in dir(base):
                        self.do(getattr(base, self._method), obj)
                    
                self.exit(obj)
                        
                self.log("<<< " + str(type(obj)))
                
                self.dec()

        self.dec()


class Binder(Base):
    
    def __init__(self, context = None, indent = 0):
        self.__dict__['_context'] = [context.copy()] if context else [{}]
        Base.__init__(self, indent)
        
    @property
    def context(self):
        return self.__dict__['_context'][-1]
        
    def __setattr__(self, item, value):
        self.context[item] = value
        
    def __getattr__(self, item):
        return self.context[item]
    
    def mark_visited(self, obj):
        if '_bound' not in dir(obj):
            obj._bound = True
            return True
        else:
            return False
     
    def enter(self, obj):   
        if 'updateContext' in dir(obj):
            self.__dict__['_context'].append(dict(self.__dict__['_context'][-1]))
            obj.updateContext(self)
            
    def exit(self, obj):
        if 'updateContext' in dir(obj):
            self.__dict__['_context'].pop()
            
    _method = 'bind'
     
    def do(self, method, obj):       
        method(obj, self)

        
def bind(obj, context = None): 
    
    Binder(context).apply(obj)

        
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
            obj._reset_generation = self._generation
            return True
        
    _method = 'reset'
        
    def do(self, method, obj):       
        method(obj)
                
def reset(obj):
    
    Resetter().apply(obj)