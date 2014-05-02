class Callable(object):
    
    def __init__(self, callable, *args):
        self.callable = callable
        self.args = args
        
    def __call__(self, *args):
        return self.callable(*(self.args + args))

Function = Callable


class Method(object):
    
    def __init__(self, obj, methodname, *args):
        self.obj = obj
        self.methodname = methodname 
        self.args = args
        
    def __eq__(self, other):
        if self.obj != other.obj:
            return False
        if self.methodname != other.methodname:
            return False
        if len(self.args) != len(other.args):
            return False
        for i in range(len(self.args)):
            if self.args[i] != other.args[i]:
                return False
        return True

    def bind_ex(self, ctx):
        pass

    def reset_ex(self, generation):
        pass
        
    def registerIn(self, registry):
        registry.insert(self)

    _internals = ['methodname', 'args']
        
    def __call__(self, *args):
        try:
            return getattr(self.obj, self.methodname)(*(self.args + args))
        except TypeError:
            print "%s.%s%s failed" % (self.obj, self.methodname, self.args + args)
            raise


class Construct(object):
    
    def __init__(self, class_, *args):
        self.class_ = class_
        self.args = args
        
    def __call__(self, *args):
        return self.class_(*(self.args + args))

class Event(object):
    
    def __init__(self, target, propname):
        self.target = target
        self.propname = propname
        
    def __iadd__(self, listener):
        x = getattr(self.target, self.propname) 
        x += listener
        return self
    
    def __isub__(self, listener):
        x = getattr(self.target, self.propname) 
        x -= listener
        return self
    
    
