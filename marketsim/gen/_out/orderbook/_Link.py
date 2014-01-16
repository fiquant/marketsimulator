from marketsim import registry
from marketsim.gen._intrinsic.orderbook.link import _Link_Impl
from marketsim import IObservable
@registry.expose(["Asset", "Link"])
class Link(_Link_Impl):
    """  (normally between a trader and a market).
     Ensures that sending packets via a link preserves their order.
    """ 
    def __init__(self, latency = None):
        from marketsim.gen._out._const import const as _const
        self.latency = latency if latency is not None else _const(0.0010)
        _Link_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'latency' : IObservable[float]
    }
    def __repr__(self):
        return "Link(%(latency)s)" % self.__dict__
    
