from marketsim import int
from marketsim import str
from marketsim import ITimeSerie
from marketsim.gen._intrinsic.orderbook.local import _Local_Impl
from marketsim import listOf
from marketsim import registry
from marketsim import float
@registry.expose(["Asset", "Local"])
class Local_StringFloatIntListITimeSerie(_Local_Impl):
    """  Maintains two order queues for orders of different sides
    """ 
    def __init__(self, name = None, tickSize = None, _digitsToShow = None, timeseries = None):
        from marketsim import rtti
        self.name = name if name is not None else "-orderbook-"
        self.tickSize = tickSize if tickSize is not None else 0.01
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 2
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        _Local_Impl.__init__(self)
    
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
        return "%(name)s" % self.__dict__
    
def Local(name = None,tickSize = None,_digitsToShow = None,timeseries = None): 
    from marketsim import rtti
    from marketsim import float
    from marketsim import int
    from marketsim import str
    from marketsim import listOf
    from marketsim import ITimeSerie
    if name is None or rtti.can_be_casted(name, str):
        if tickSize is None or rtti.can_be_casted(tickSize, float):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                    return Local_StringFloatIntListITimeSerie(name,tickSize,_digitsToShow,timeseries)
    raise Exception("Cannot find suitable overload")
