from marketsim import registry
from marketsim.gen._intrinsic.orderbook.local import _Local_Impl
from marketsim import listOf
from marketsim import ITimeSerie
@registry.expose(["Asset", "Local"])
class Local(_Local_Impl):"""  Maintains two order queues for orders of different sides
    """ 
    def __init__(self, tickSize = None, _digitsToShow = None, name = None, timeseries = None):from marketsim import rtti
        self.tickSize = tickSize if tickSize is not None else 0.01
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 2
        self.name = name if name is not None else "-orderbook-"
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        _Local_Impl.__init__(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'tickSize' : float,
        '_digitsToShow' : int,
        'name' : str,
        'timeseries' : listOf(ITimeSerie)
        
    }
    def __repr__(self):return "%(name)s" % self.__dict__
    
