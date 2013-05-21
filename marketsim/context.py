from marketsim.registry import properties

class Binder(object):
    
    def __init__(self, context = None, visited = None):
        self.__dict__['_visited'] = visited if visited else set()
        self.__dict__['_context'] = context if context else {}
        
    def __setattr__(self, item, value):
        self.__dict__['_context'][item] = value
        
    def __getattr__(self, item):
        return self.__dict__['_context'][item]
    
    def clone(self):
        return Binder(self.__dict__['_context'], self.__dict__['_visited'])
    
    def bind(self, obj): 
        typ = type(obj)
        if typ is int or typ is float or typ is bool or typ is str:
            return 
        
        if typ is list:
            for x in obj:
                self.bind(x)
        else:
            if obj in self.__dict__['_visited']:
                return
            
            self.__dict__['_visited'].add(obj)
            
            propnames = properties(obj)
            if propnames is None:
                propnames = {}                
            
            if 'updateContext' in dir(obj):
                childContext = self.clone()
                obj.updateContext(childContext)
            else:
                childContext = self
                
            for propname in propnames.iterkeys():
                if propname[0] != '_':
                    childContext.bind(getattr(obj, propname))
                
            if 'bind' in dir(obj):
                if '_bound' not in dir(obj):
                    obj.bind(self)
                    obj._bound = True
