from marketsim import registry
from marketsim.gen._out._itwowaylink import ITwoWayLink
from marketsim.gen._intrinsic.orderbook.link import TwoWayLink_Impl
from marketsim.gen._out._ilink import ILink
@registry.expose(["Asset", "TwoWayLink"])
class TwoWayLink_ILinkILink(ITwoWayLink,TwoWayLink_Impl):
    """ **Represents latency in information propagation between two agents**
    
     (normally between a trader and a market).
     Ensures that sending packets via links preserves their order.
     Holds two one-way links in opposite directions.
    
    Parameters are:
    
    **up**
    	 Forward link (normally from a trader to a market)
    
    **down**
    	 Backward link (normally from a market to a trader)
    """ 
    def __init__(self, up = None, down = None):
        from marketsim.gen._out.orderbook._link import Link_IObservableFloat as _orderbook_Link_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.up = up if up is not None else deref_opt(_orderbook_Link_IObservableFloat())
        self.down = down if down is not None else deref_opt(_orderbook_Link_IObservableFloat())
        rtti.check_fields(self)
        TwoWayLink_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'up' : ILink,
        'down' : ILink
    }
    
    
    
    
    def __repr__(self):
        return "TwoWayLink(%(up)s, %(down)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.up.bindEx(self._ctx_ex)
        self.down.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def TwoWayLink(up = None,down = None): 
    from marketsim.gen._out._ilink import ILink
    from marketsim import rtti
    if up is None or rtti.can_be_casted(up, ILink):
        if down is None or rtti.can_be_casted(down, ILink):
            return TwoWayLink_ILinkILink(up,down)
    raise Exception('Cannot find suitable overload for TwoWayLink('+str(up) +':'+ str(type(up))+','+str(down) +':'+ str(type(down))+')')
