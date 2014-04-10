from marketsim import registry
from marketsim.gen._out._ilink import ILink
from marketsim.gen._intrinsic.orderbook.link import Link_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Asset", "Link"])
class Link_IObservableFloat(ILink,Link_Impl):
    """ **Represents latency in information propagation from one agent to another one**
    
     (normally between a trader and a market).
     Ensures that sending packets via a link preserves their order.
    
    Parameters are:
    
    **latency**
    	 function called for each packet in order to determine
    	 when it will appear at the end point
    """ 
    def __init__(self, latency = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.latency = latency if latency is not None else deref_opt(_const_Float(0.001))
        rtti.check_fields(self)
        Link_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'latency' : IObservablefloat
    }
    
    
    def __repr__(self):
        return "Link(%(latency)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.latency.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Link(latency = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if latency is None or rtti.can_be_casted(latency, IObservablefloat):
        return Link_IObservableFloat(latency)
    raise Exception('Cannot find suitable overload for Link('+str(latency) +':'+ str(type(latency))+')')
