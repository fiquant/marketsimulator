from marketsim.gen._intrinsic.orderbook.volume_levels import VolumeLevels_Impl
from marketsim.ops._all import Observable
from marketsim import int
from marketsim import IOrderQueue
from marketsim import IVolumeLevels
from marketsim import registry
from marketsim import float
@registry.expose(["Asset", "VolumeLevels"])
class VolumeLevels_IOrderQueueFloatInt(Observable[IVolumeLevels],VolumeLevels_Impl):
    """   Level of volume V is a price at which cumulative volume of better orders is V
    """ 
    def __init__(self, queue = None, volumeDelta = None, volumeCount = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import IVolumeLevels
        from marketsim import event
        Observable[IVolumeLevels].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks()
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        self.volumeDelta = volumeDelta if volumeDelta is not None else 30.0
        if isinstance(volumeDelta, types.IEvent):
            event.subscribe(self.volumeDelta, self.fire, self)
        self.volumeCount = volumeCount if volumeCount is not None else 10
        if isinstance(volumeCount, types.IEvent):
            event.subscribe(self.volumeCount, self.fire, self)
        rtti.check_fields(self)
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
    
VolumeLevels = VolumeLevels_IOrderQueueFloatInt
