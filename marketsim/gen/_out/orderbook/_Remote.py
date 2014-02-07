from marketsim.gen._intrinsic.orderbook.remote import _Remote_Impl
from marketsim import ITimeSerie
from marketsim import ITwoWayLink
from marketsim import IOrderBook
from marketsim import listOf
from marketsim import registry
@registry.expose(["Asset", "Remote"])
class Remote_IOrderBookITwoWayLinkListITimeSerie(_Remote_Impl):
    """  to the market by means of a *link* that introduces some latency in information propagation
    """ 
    def __init__(self, orderbook = None, link = None, timeseries = None):
        from marketsim.gen._out.orderbook._Local import Local as _orderbook_Local
        from marketsim.gen._out.orderbook._TwoWayLink import TwoWayLink as _orderbook_TwoWayLink
        from marketsim import rtti
        self.orderbook = orderbook if orderbook is not None else _orderbook_Local()
        self.link = link if link is not None else _orderbook_TwoWayLink()
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        _Remote_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderbook' : IOrderBook,
        'link' : ITwoWayLink,
        'timeseries' : listOf(ITimeSerie)
    }
    def __repr__(self):
        return "%(orderbook)s.name^remote" % self.__dict__
    
Remote = Remote_IOrderBookITwoWayLinkListITimeSerie
