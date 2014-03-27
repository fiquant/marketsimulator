from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._itwowaylink import ITwoWayLink
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.remote import Remote_Impl
from marketsim import listOf
from marketsim import registry
@registry.expose(["Asset", "Remote"])
class Remote_IOrderBookITwoWayLinkListITimeSerie(IOrderBook,Remote_Impl):
    """  to the market by means of a *link* that introduces some latency in information propagation
    """ 
    def __init__(self, orderbook = None, link = None, timeseries = None):
        from marketsim.gen._out.orderbook._local import Local_StringFloatIntListITimeSerie as _orderbook_Local_StringFloatIntListITimeSerie
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._twowaylink import TwoWayLink_ILinkILink as _orderbook_TwoWayLink_ILinkILink
        from marketsim import rtti
        self.orderbook = orderbook if orderbook is not None else deref_opt(_orderbook_Local_StringFloatIntListITimeSerie())
        self.link = link if link is not None else deref_opt(_orderbook_TwoWayLink_ILinkILink())
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        Remote_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderbook' : IOrderBook,
        'link' : ITwoWayLink,
        'timeseries' : listOf(ITimeSerie)
    }
    def __repr__(self):
        return "%(orderbook)s.name^remote" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def Remote(orderbook = None,link = None,timeseries = None): 
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim import rtti
    from marketsim.gen._out._itwowaylink import ITwoWayLink
    from marketsim import listOf
    from marketsim.gen._out._iorderbook import IOrderBook
    if orderbook is None or rtti.can_be_casted(orderbook, IOrderBook):
        if link is None or rtti.can_be_casted(link, ITwoWayLink):
            if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                return Remote_IOrderBookITwoWayLinkListITimeSerie(orderbook,link,timeseries)
    raise Exception('Cannot find suitable overload for Remote('+str(orderbook) +':'+ str(type(orderbook))+','+str(link) +':'+ str(type(link))+','+str(timeseries) +':'+ str(type(timeseries))+')')
