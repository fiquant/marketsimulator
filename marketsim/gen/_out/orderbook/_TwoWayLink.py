from marketsim import registry
from marketsim.gen._intrinsic.orderbook.link import _TwoWayLink_Impl
from marketsim import ILink
from marketsim import ILink
@registry.expose(["Asset", "TwoWayLink"])
class TwoWayLink(_TwoWayLink_Impl):
    """  (normally between a trader and a market).
     Ensures that sending packets via links preserves their order.
     Holds two one-way links in opposite directions.
    """ 
    def __init__(self, up = None, down = None):
        from marketsim.gen._out.orderbook._Link import Link as _orderbook_Link
        from marketsim.gen._out.orderbook._Link import Link as _orderbook_Link
        self.up = up if up is not None else _orderbook_Link()
        self.down = down if down is not None else _orderbook_Link()
        _TwoWayLink_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'up' : ILink,
        'down' : ILink
    }
    def __repr__(self):
        return "TwoWayLink(%(up)s, %(down)s)" % self.__dict__
    
