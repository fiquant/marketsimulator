import inspect

class merge(object):
    def __init__(self, d, **kwargs):
        self.__dict__ = d.__dict__.copy()
        for k in kwargs:
            self.__dict__[k] = kwargs[k]
            
currentframe = inspect.currentframe

class Params(object):

    def __init__(self, ctor, properties):
                
        for k in properties:
            if k != 'self' and k != 'frame':
                self.__dict__[k] = properties[k]
                
        self._ctor = ctor
        
    @staticmethod
    def fromFrame(ctor, frame):
        _, _, _, values = inspect.getargvalues(frame)
        return Params(ctor, dict(values))
    
    def With(self, **kwargs):
        return Params(self._ctor, merge(self, **kwargs).__dict__)    
    
    def runAt(self, trader):
        return Running(trader, self._ctor, self.__dict__)
        
    def __getattr__(self, item):
        if self._impl is not None:
            return getattr(self._impl, item)
        
    def __setattr__(self, item, value):
        self.__dict__[item] = value
        if item[0] != '_':
            self._respawn()

class Running(Params):
    
    def __init__(self, trader, ctor, properties):
                
        for k in properties:
            if k != 'self' and k != 'frame':
                self.__dict__[k] = properties[k]
                
        self._ctor = ctor
        self._impl = None
        self._trader = trader
        self._respawn()
        
    def _respawn(self):
        if self._impl is not None:
            self._impl.dispose()
        self._impl = self._ctor(self._trader, self)
        
    def __getattr__(self, item):
        if self._impl is not None:
            return getattr(self._impl, item)
        
    def __setattr__(self, item, value):
        self.__dict__[item] = value
        if item[0] != '_':
            self._respawn()
