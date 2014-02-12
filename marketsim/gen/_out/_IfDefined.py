from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "IfDefined"])
class IfDefined_IObservableFloatIObservableFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        self.elsePart = elsePart if elsePart is not None else _const_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'elsePart' : IObservable[float]
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % self.__dict__
    
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
        from marketsim.gen._out.ops._notequal import NotEqual_IObservableFloatIFunctionFloat as _ops_NotEqual_IObservableFloatIFunctionFloat
        from marketsim.gen._out._null import null_ as _null_
        return _ops_Condition_IObservableBooleanIObservableFloatIObservableFloat(_ops_NotEqual_IObservableFloatIFunctionFloat(self.x,_null_()),self.x,self.elsePart)
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "IfDefined"])
class IfDefined_IFunctionFloatIObservableFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        self.elsePart = elsePart if elsePart is not None else _const_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'elsePart' : IObservable[float]
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % self.__dict__
    
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
        from marketsim.gen._out.ops._condition import Condition_IFunctionBooleanIFunctionFloatIObservableFloat as _ops_Condition_IFunctionBooleanIFunctionFloatIObservableFloat
        from marketsim.gen._out.ops._notequal import NotEqual_IFunctionFloatIFunctionFloat as _ops_NotEqual_IFunctionFloatIFunctionFloat
        from marketsim.gen._out._null import null_ as _null_
        return _ops_Condition_IFunctionBooleanIFunctionFloatIObservableFloat(_ops_NotEqual_IFunctionFloatIFunctionFloat(self.x,_null_()),self.x,self.elsePart)
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "IfDefined"])
class IfDefined_IObservableFloatIFunctionFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        self.elsePart = elsePart if elsePart is not None else _constant_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'elsePart' : IFunction[float]
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % self.__dict__
    
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
        from marketsim.gen._out.ops._notequal import NotEqual_IObservableFloatIFunctionFloat as _ops_NotEqual_IObservableFloatIFunctionFloat
        from marketsim.gen._out._null import null_ as _null_
        return _ops_Condition_IObservableBooleanIObservableFloatIFunctionFloat(_ops_NotEqual_IObservableFloatIFunctionFloat(self.x,_null_()),self.x,self.elsePart)
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "IfDefined"])
class IfDefined_IFunctionFloatIFunctionFloat(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        self.elsePart = elsePart if elsePart is not None else _constant_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'elsePart' : IFunction[float]
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % self.__dict__
    
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
        from marketsim.gen._out.ops._notequal import NotEqual_IFunctionFloatIFunctionFloat as _ops_NotEqual_IFunctionFloatIFunctionFloat
        from marketsim.gen._out._null import null_ as _null_
        return _ops_Condition_IFunctionBooleanIFunctionFloatIFunctionFloat(_ops_NotEqual_IFunctionFloatIFunctionFloat(self.x,_null_()),self.x,self.elsePart)
    
def IfDefined(x = None,elsePart = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if elsePart is None or rtti.can_be_casted(elsePart, IObservable[float]):
            return IfDefined_IObservableFloatIObservableFloat(x,elsePart)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if elsePart is None or rtti.can_be_casted(elsePart, IObservable[float]):
            return IfDefined_IFunctionFloatIObservableFloat(x,elsePart)
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if elsePart is None or rtti.can_be_casted(elsePart, IFunction[float]):
            return IfDefined_IObservableFloatIFunctionFloat(x,elsePart)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if elsePart is None or rtti.can_be_casted(elsePart, IFunction[float]):
            return IfDefined_IFunctionFloatIFunctionFloat(x,elsePart)
    raise Exception('Cannot find suitable overload for IfDefined('+str(x)+','+str(elsePart)+')')
