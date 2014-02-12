from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "Max"])
class Max_IObservableFloatIObservableFloat(Observable[float]):
    """  If *x* or/and *y* are observables, *Min* is also observable
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        self.y = y if y is not None else _const_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "max{%(x)s, %(y)s}" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableFloatIObservableFloat as _ops_Condition_IObservableBooleanIObservableFloatIObservableFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatIObservableFloat as _ops_Greater_IObservableFloatIObservableFloat
        return _ops_Condition_IObservableBooleanIObservableFloatIObservableFloat(_ops_Greater_IObservableFloatIObservableFloat(self.x,self.y),self.x,self.y)
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "Max"])
class Max_IFunctionFloatIObservableFloat(Observable[float]):
    """  If *x* or/and *y* are observables, *Min* is also observable
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        self.y = y if y is not None else _const_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "max{%(x)s, %(y)s}" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIFunctionFloatIObservableFloat as _ops_Condition_IObservableBooleanIFunctionFloatIObservableFloat
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIObservableFloat as _ops_Greater_IFunctionFloatIObservableFloat
        return _ops_Condition_IObservableBooleanIFunctionFloatIObservableFloat(_ops_Greater_IFunctionFloatIObservableFloat(self.x,self.y),self.x,self.y)
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "Max"])
class Max_IObservableFloatIFunctionFloat(Observable[float]):
    """  If *x* or/and *y* are observables, *Min* is also observable
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        self.y = y if y is not None else _constant_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "max{%(x)s, %(y)s}" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableFloatIFunctionFloat as _ops_Condition_IObservableBooleanIObservableFloatIFunctionFloat
        from marketsim.gen._out.ops._greater import Greater_IObservableFloatIFunctionFloat as _ops_Greater_IObservableFloatIFunctionFloat
        return _ops_Condition_IObservableBooleanIObservableFloatIFunctionFloat(_ops_Greater_IObservableFloatIFunctionFloat(self.x,self.y),self.x,self.y)
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "Max"])
class Max_IFunctionFloatIFunctionFloat(Observable[float]):
    """  If *x* or/and *y* are observables, *Min* is also observable
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        self.y = y if y is not None else _constant_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "max{%(x)s, %(y)s}" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._condition import Condition_IFunctionBooleanIFunctionFloatIFunctionFloat as _ops_Condition_IFunctionBooleanIFunctionFloatIFunctionFloat
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIFunctionFloat as _ops_Greater_IFunctionFloatIFunctionFloat
        return _ops_Condition_IFunctionBooleanIFunctionFloatIFunctionFloat(_ops_Greater_IFunctionFloatIFunctionFloat(self.x,self.y),self.x,self.y)
    
def Max(x = None,y = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return Max_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return Max_IFunctionFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return Max_IObservableFloatIFunctionFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return Max_IFunctionFloatIFunctionFloat(x,y)
    raise Exception('Cannot find suitable overload for Max('+str(x)+','+str(y)+')')
