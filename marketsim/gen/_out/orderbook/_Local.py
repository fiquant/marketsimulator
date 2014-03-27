from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.local import Local_Impl
from marketsim import listOf
from marketsim import registry
@registry.expose(["Asset", "Local"])
class Local_StringFloatIntListITimeSerie(IOrderBook,Local_Impl):
    """  Maintains two order queues for orders of different sides
    """ 
    def __init__(self, name = None, tickSize = None, _digitsToShow = None, timeseries = None):
        from marketsim import rtti
        self.name = name if name is not None else "-orderbook-"
        self.tickSize = tickSize if tickSize is not None else 0.01
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 2
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        Local_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'name' : str,
        'tickSize' : float,
        '_digitsToShow' : int,
        'timeseries' : listOf(ITimeSerie)
    }
    def __repr__(self):
        return "%(name)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def Local(name = None,tickSize = None,_digitsToShow = None,timeseries = None): 
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim import listOf
    from marketsim import rtti
    if name is None or rtti.can_be_casted(name, str):
        if tickSize is None or rtti.can_be_casted(tickSize, float):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                    return Local_StringFloatIntListITimeSerie(name,tickSize,_digitsToShow,timeseries)
    raise Exception('Cannot find suitable overload for Local('+str(name) +':'+ str(type(name))+','+str(tickSize) +':'+ str(type(tickSize))+','+str(_digitsToShow) +':'+ str(type(_digitsToShow))+','+str(timeseries) +':'+ str(type(timeseries))+')')
