import context

class Reference(object):

    def __init__(self, name):
        self._impl = None
        self.name = name
        
    def bind(self, ctx):
        assert self._impl is  None
        self._impl = getattr(ctx, self.name)
        #context.bind(self._impl, ctx)
        
    @property
    def pointee(self):
        return self._impl
        
    def __getattr__(self, name):
        if name[0:2] != "__" and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
        
    def __iadd__(self, other):
        self._impl += other
        return self
    
    def __isub__(self, other):
        self._impl -= other
        return self
    
    def __call__(self, *args, **kwargs):
        return self._impl(*args, **kwargs)
    
    def __repr__(self):
        return "._" + self.name
    
    _properties = { 'name' : str }
