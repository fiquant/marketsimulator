# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableFloatIObservableFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservablefloat,
        'elsepart' : IObservablefloat
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableSideIObservableSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim import rtti
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservableSide,
        'elsepart' : IObservableSide
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableBooleanIObservableBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import rtti
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._observablefalse import observableFalse_ as _observableFalse_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_observableTrue_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_observableFalse_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservablebool,
        'elsepart' : IObservablebool
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableFloatIObservableFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservablefloat,
        'elsepart' : IObservablefloat
    }
    
    
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanFloatIObservableFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IObservablefloat
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableFloatFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservablefloat,
        'elsepart' : IFunctionfloat
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableSideIObservableSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservableSide,
        'elsepart' : IObservableSide
    }
    
    
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanSideIObservableSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionSide,
        'elsepart' : IObservableSide
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableSideSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim import rtti
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservableSide,
        'elsepart' : IFunctionSide
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableBooleanIObservableBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._observablefalse import observableFalse_ as _observableFalse_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_observableTrue_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_observableFalse_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservablebool,
        'elsepart' : IObservablebool
    }
    
    
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanBooleanIObservableBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._observablefalse import observableFalse_ as _observableFalse_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_true_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_observableFalse_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionbool,
        'elsepart' : IObservablebool
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableBooleanBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._false import false_ as _false_
        from marketsim import rtti
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_observableTrue_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_false_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservablebool,
        'elsepart' : IFunctionbool
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanFloatIObservableFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IObservablefloat
    }
    
    
    
    
    
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableFloatFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservablefloat,
        'elsepart' : IFunctionfloat
    }
    
    
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanFloatFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import rtti
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IFunctionfloat
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanSideIObservableSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionSide,
        'elsepart' : IObservableSide
    }
    
    
    
    
    
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableSideSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservableSide,
        'elsepart' : IFunctionSide
    }
    
    
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanSideSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionSide,
        'elsepart' : IFunctionSide
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanBooleanIObservableBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observablefalse import observableFalse_ as _observableFalse_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_true_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_observableFalse_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionbool,
        'elsepart' : IObservablebool
    }
    
    
    
    
    
    
    
    
    def on_elsepart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'elsepart', value)
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableBooleanBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._false import false_ as _false_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_observableTrue_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_false_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservablebool,
        'elsepart' : IFunctionbool
    }
    
    
    
    
    
    def on_ifpart_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'ifpart', value)
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanBooleanBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._false import false_ as _false_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_true_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_false_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionbool,
        'elsepart' : IFunctionbool
    }
    
    
    def on_cond_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'cond', value)
    
    
    
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanFloatFloat(Observablefloat,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IFunctionfloat
    }
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._intrinsic.ops import Condition_Impl
@registry.expose(["Ops", "Condition"])
class Condition_BooleanSideSide(ObservableSide,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._side import Side
        from marketsim import deref_opt
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionSide,
        'elsepart' : IFunctionSide
    }
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic.ops import Condition_Impl
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
@registry.expose(["Ops", "Condition"])
class Condition_BooleanBooleanBoolean(Observablebool,Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._false import false_ as _false_
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim import deref_opt
        Observablebool.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        self.ifpart = ifpart if ifpart is not None else deref_opt(_true_())
        self.elsepart = elsepart if elsepart is not None else deref_opt(_false_())
        rtti.check_fields(self)
        Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionbool,
        'elsepart' : IFunctionbool
    }
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.cond.bind_ex(self._ctx_ex)
        self.ifpart.bind_ex(self._ctx_ex)
        self.elsepart.bind_ex(self._ctx_ex)
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
        self.cond.reset_ex(generation)
        self.ifpart.reset_ex(generation)
        self.elsepart.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def Condition(cond = None,ifpart = None,elsepart = None): 
    from marketsim import rtti
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out._side import Side
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._iobservable._iobservableside import IObservableSide
    from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_IObservableBooleanIObservableFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_IObservableBooleanIObservableSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablebool):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablebool):
                return Condition_IObservableBooleanIObservableBooleanIObservableBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_BooleanIObservableFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_IObservableBooleanFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_IObservableBooleanIObservableFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_BooleanIObservableSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_IObservableBooleanSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_IObservableBooleanIObservableSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablebool):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablebool):
                return Condition_BooleanIObservableBooleanIObservableBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionbool):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablebool):
                return Condition_IObservableBooleanBooleanIObservableBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablebool):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionbool):
                return Condition_IObservableBooleanIObservableBooleanBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_BooleanFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_BooleanIObservableFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_IObservableBooleanFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_BooleanSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_BooleanIObservableSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_IObservableBooleanSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionbool):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablebool):
                return Condition_BooleanBooleanIObservableBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablebool):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionbool):
                return Condition_BooleanIObservableBooleanBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionbool):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionbool):
                return Condition_IObservableBooleanBooleanBoolean(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_BooleanFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_BooleanSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionbool):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionbool):
                return Condition_BooleanBooleanBoolean(cond,ifpart,elsepart)
    raise Exception('Cannot find suitable overload for Condition('+str(cond) +':'+ str(type(cond))+','+str(ifpart) +':'+ str(type(ifpart))+','+str(elsepart) +':'+ str(type(elsepart))+')')
