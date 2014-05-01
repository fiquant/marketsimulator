# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import And_Impl
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
@registry.expose(["Ops", "And"])
class And_IObservableBooleanIObservableBoolean(Observablebool,And_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        from marketsim import rtti
        Observablebool.__init__(self)
        self.x = x if x is not None else deref_opt(_observableTrue_())
        self.y = y if y is not None else deref_opt(_observableTrue_())
        rtti.check_fields(self)
        And_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablebool,
        'y' : IObservablebool
    }
    
    
    def on_x_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'x', value)
    
    
    
    def on_y_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'y', value)
    
    def __repr__(self):
        return "({%(x)s}and{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import And_Impl
@registry.expose(["Ops", "And"])
class And_BooleanIObservableBoolean(Observablebool,And_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.x = x if x is not None else deref_opt(_true_())
        self.y = y if y is not None else deref_opt(_observableTrue_())
        rtti.check_fields(self)
        And_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionbool,
        'y' : IObservablebool
    }
    
    
    
    
    
    def on_y_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'y', value)
    
    def __repr__(self):
        return "({%(x)s}and{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import And_Impl
@registry.expose(["Ops", "And"])
class And_IObservableBooleanBoolean(Observablebool,And_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.x = x if x is not None else deref_opt(_observableTrue_())
        self.y = y if y is not None else deref_opt(_true_())
        rtti.check_fields(self)
        And_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablebool,
        'y' : IFunctionbool
    }
    
    
    def on_x_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'x', value)
    
    
    
    
    def __repr__(self):
        return "({%(x)s}and{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import And_Impl
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
@registry.expose(["Ops", "And"])
class And_BooleanBoolean(Observablebool,And_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import deref_opt
        from marketsim import rtti
        Observablebool.__init__(self)
        self.x = x if x is not None else deref_opt(_true_())
        self.y = y if y is not None else deref_opt(_true_())
        rtti.check_fields(self)
        And_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionbool,
        'y' : IFunctionbool
    }
    
    
    
    
    
    
    def __repr__(self):
        return "({%(x)s}and{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
def And(x = None,y = None): 
    from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablebool):
        if y is None or rtti.can_be_casted(y, IObservablebool):
            return And_IObservableBooleanIObservableBoolean(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionbool):
        if y is None or rtti.can_be_casted(y, IObservablebool):
            return And_BooleanIObservableBoolean(x,y)
    if x is None or rtti.can_be_casted(x, IObservablebool):
        if y is None or rtti.can_be_casted(y, IFunctionbool):
            return And_IObservableBooleanBoolean(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionbool):
        if y is None or rtti.can_be_casted(y, IFunctionbool):
            return And_BooleanBoolean(x,y)
    raise Exception('Cannot find suitable overload for And('+str(x) +':'+ str(type(x))+','+str(y) +':'+ str(type(y))+')')
