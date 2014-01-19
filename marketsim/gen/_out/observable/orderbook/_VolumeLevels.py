from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IVolumeLevels
from marketsim.gen._intrinsic.orderbook.volume_levels import VolumeLevels_Impl
from marketsim import IOrderQueue
@registry.expose(["Asset's", "VolumeLevels"])
class VolumeLevels(Function[IVolumeLevels], VolumeLevels_Impl):
    """ 
    """ 
    def __init__(self, queue = None, volumeDelta = None, volumeCount = None):
        from marketsim.gen._out.observable.orderbook._Asks import Asks as _observable_orderbook_Asks
        self.queue = queue if queue is not None else _observable_orderbook_Asks()
        self.volumeDelta = volumeDelta if volumeDelta is not None else 30.0
        self.volumeCount = volumeCount if volumeCount is not None else 10
        VolumeLevels_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'volumeDelta' : float,
        'volumeCount' : int
    }
    def __repr__(self):
        return "VolumeLevels(%(queue)s)" % self.__dict__
    
