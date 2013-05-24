from marketsim.registry import properties, internals, children_to_visit

debug = False

class Binder(object):
    
    def __init__(self, context = None, visited = None, indent = 0):
        self.__dict__['_visited'] = visited if visited else set()
        self.__dict__['_context'] = context.copy() if context else {}
        self.__dict__['_indent'] = indent
        self.log = self._log_debug if debug else self._log_empty
        
    def __setattr__(self, item, value):
        self.__dict__['_context'][item] = value
        
    def __getattr__(self, item):
        return self.__dict__['_context'][item]
    
    def clone(self):
        return Binder(self.__dict__['_context'], self.__dict__['_visited'], self.indent)
    
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
    
    def bind(self, obj): 
        typ = type(obj)
        if typ is int or typ is float or typ is bool or typ is str:
            return 
        
        self.inc()
        
        if typ is set:
            self.log('{')
            for x in obj:
                self.bind(x)
            self.log('}')
        elif typ is list:
            self.log('[')
            for x in obj:
                self.bind(x)
            self.log(']')
        else:
            if obj in self.__dict__['_visited']:
                self.log('*')
                self.dec()
                return
            
            self.__dict__['_visited'].add(obj)
            
            self.inc()
            
            self.log(">>> " + str(type(obj)))
            
            propnames = properties(obj)
            if propnames is None:
                propnames = {}                
            
            if 'updateContext' in dir(obj):
                childContext = self.clone()
                obj.updateContext(childContext)
            else:
                childContext = self
                
            if '_subscriptions' in dir(obj):
                childContext.bind(obj._subscriptions)
                
            for propname in propnames.iterkeys():
                if propname[0] != '_':
                    self.log(propname)
                    childContext.bind(getattr(obj, propname))
                
            for propname in internals(obj):
                self.log(propname)
                childContext.bind(getattr(obj, propname))
                
            for child in children_to_visit(obj):
                childContext.bind(child)
                
            if 'bind' in dir(obj):
                if '_bound' not in dir(obj):
                    obj.bind(self)
                    obj._bound = True
                    
            self.log("<<< " + str(type(obj)))
            
            self.dec()

        self.dec()