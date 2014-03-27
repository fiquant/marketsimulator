from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Basic", "IfDefined"])
class IfDefined_IObservableFloatIObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_const_Float(1.0))
        self.elsePart = elsePart if elsePart is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'elsePart' : IObservablefloat
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.ops._notequal import NotEqual_IObservableFloatFloat as _ops_NotEqual_IObservableFloatFloat
        from marketsim.gen._out._null import null_ as _null_
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanIObservableFloatIObservableFloat(deref_opt(_ops_NotEqual_IObservableFloatFloat(self.x,deref_opt(_null_()))),self.x,self.elsePart))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Basic", "IfDefined"])
class IfDefined_FloatIObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_constant_Float(1.0))
        self.elsePart = elsePart if elsePart is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'elsePart' : IObservablefloat
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.ops._condition import Condition_BooleanFloatIObservableFloat as _ops_Condition_BooleanFloatIObservableFloat
        from marketsim.gen._out.ops._notequal import NotEqual_FloatFloat as _ops_NotEqual_FloatFloat
        from marketsim.gen._out._null import null_ as _null_
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanFloatIObservableFloat(deref_opt(_ops_NotEqual_FloatFloat(self.x,deref_opt(_null_()))),self.x,self.elsePart))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Basic", "IfDefined"])
class IfDefined_IObservableFloatFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_const_Float(1.0))
        self.elsePart = elsePart if elsePart is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'elsePart' : IFunctionfloat
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.ops._condition import Condition_IObservableBooleanIObservableFloatFloat as _ops_Condition_IObservableBooleanIObservableFloatFloat
        from marketsim.gen._out.ops._notequal import NotEqual_IObservableFloatFloat as _ops_NotEqual_IObservableFloatFloat
        from marketsim.gen._out._null import null_ as _null_
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_IObservableBooleanIObservableFloatFloat(deref_opt(_ops_NotEqual_IObservableFloatFloat(self.x,deref_opt(_null_()))),self.x,self.elsePart))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import context
@registry.expose(["Basic", "IfDefined"])
class IfDefined_FloatFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_constant_Float(1.0))
        self.elsePart = elsePart if elsePart is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'elsePart' : IFunctionfloat
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.ops._condition import Condition_BooleanFloatFloat as _ops_Condition_BooleanFloatFloat
        from marketsim.gen._out.ops._notequal import NotEqual_FloatFloat as _ops_NotEqual_FloatFloat
        from marketsim.gen._out._null import null_ as _null_
        from marketsim import deref_opt
        return deref_opt(_ops_Condition_BooleanFloatFloat(deref_opt(_ops_NotEqual_FloatFloat(self.x,deref_opt(_null_()))),self.x,self.elsePart))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def IfDefined(x = None,elsePart = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if elsePart is None or rtti.can_be_casted(elsePart, IObservablefloat):
            return IfDefined_IObservableFloatIObservableFloat(x,elsePart)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if elsePart is None or rtti.can_be_casted(elsePart, IObservablefloat):
            return IfDefined_FloatIObservableFloat(x,elsePart)
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if elsePart is None or rtti.can_be_casted(elsePart, IFunctionfloat):
            return IfDefined_IObservableFloatFloat(x,elsePart)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if elsePart is None or rtti.can_be_casted(elsePart, IFunctionfloat):
            return IfDefined_FloatFloat(x,elsePart)
    raise Exception('Cannot find suitable overload for IfDefined('+str(x) +':'+ str(type(x))+','+str(elsePart) +':'+ str(type(elsePart))+')')
