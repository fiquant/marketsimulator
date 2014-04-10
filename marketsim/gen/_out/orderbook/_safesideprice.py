from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Asset", "SafeSidePrice"])
class SafeSidePrice_IOrderQueueIObservableFloat(Observablefloat):
    """ **Returns best price if defined, otherwise last price**
    
      and *defaultValue* if there haven't been any trades
    
    Parameters are:
    
    **queue**
    
    **defaultValue**
    	 price to be used if there haven't been any trades 
    """ 
    def __init__(self, queue = None, defaultValue = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        self.defaultValue = defaultValue if defaultValue is not None else deref_opt(_const_Float(100.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'defaultValue' : IObservablefloat
    }
    
    
    
    
    def __repr__(self):
        return "SafeSidePrice(%(queue)s, %(defaultValue)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.queue.bindEx(self._ctx_ex)
        self.defaultValue.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out._ifdefined import IfDefined_IObservableFloatIObservableFloat as _IfDefined_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._lastprice import LastPrice_IOrderQueue as _orderbook_LastPrice_IOrderQueue
        return deref_opt(_IfDefined_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(self.queue)),deref_opt(_IfDefined_IObservableFloatIObservableFloat(deref_opt(_orderbook_LastPrice_IOrderQueue(self.queue)),self.defaultValue))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim import context
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "SafeSidePrice"])
class SafeSidePrice_IOrderQueueFloat(Observablefloat):
    """ **Returns best price if defined, otherwise last price**
    
      and *defaultValue* if there haven't been any trades
    
    Parameters are:
    
    **queue**
    
    **defaultValue**
    	 price to be used if there haven't been any trades 
    """ 
    def __init__(self, queue = None, defaultValue = None):
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        self.defaultValue = defaultValue if defaultValue is not None else deref_opt(_constant_Float(100.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'defaultValue' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "SafeSidePrice(%(queue)s, %(defaultValue)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.queue.bindEx(self._ctx_ex)
        self.defaultValue.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out.orderbook._lastprice import LastPrice_IOrderQueue as _orderbook_LastPrice_IOrderQueue
        from marketsim.gen._out.orderbook._bestprice import BestPrice_IOrderQueue as _orderbook_BestPrice_IOrderQueue
        from marketsim.gen._out._ifdefined import IfDefined_IObservableFloatFloat as _IfDefined_IObservableFloatFloat
        from marketsim.gen._out._ifdefined import IfDefined_IObservableFloatIObservableFloat as _IfDefined_IObservableFloatIObservableFloat
        from marketsim import deref_opt
        return deref_opt(_IfDefined_IObservableFloatIObservableFloat(deref_opt(_orderbook_BestPrice_IOrderQueue(self.queue)),deref_opt(_IfDefined_IObservableFloatFloat(deref_opt(_orderbook_LastPrice_IOrderQueue(self.queue)),self.defaultValue))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def SafeSidePrice(queue = None,defaultValue = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if defaultValue is None or rtti.can_be_casted(defaultValue, IObservablefloat):
            return SafeSidePrice_IOrderQueueIObservableFloat(queue,defaultValue)
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if defaultValue is None or rtti.can_be_casted(defaultValue, IFunctionfloat):
            return SafeSidePrice_IOrderQueueFloat(queue,defaultValue)
    raise Exception('Cannot find suitable overload for SafeSidePrice('+str(queue) +':'+ str(type(queue))+','+str(defaultValue) +':'+ str(type(defaultValue))+')')
