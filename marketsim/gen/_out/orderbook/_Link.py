from marketsim import registry
from marketsim.gen._out._ilink import ILink
from marketsim.gen._intrinsic.orderbook.link import _Link_Impl
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Asset", "Link"])
class Link_IObservableFloat(ILink,_Link_Impl):
    """  (normally between a trader and a market).
     Ensures that sending packets via a link preserves their order.
    """ 
    def __init__(self, latency = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.latency = latency if latency is not None else _const_Float(0.001)
        rtti.check_fields(self)
        _Link_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'latency' : IObservablefloat
    }
    def __repr__(self):
        return "Link(%(latency)s)" % self.__dict__
    
def Link(latency = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    if latency is None or rtti.can_be_casted(latency, IObservablefloat):
        return Link_IObservableFloat(latency)
    raise Exception('Cannot find suitable overload for Link('+str(latency) +':'+ str(type(latency))+')')
