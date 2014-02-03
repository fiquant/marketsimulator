from marketsim import registry
from marketsim.gen._intrinsic.orderbook.volume_levels import VolumeLevels_Impl
from marketsim import IOrderQueue
from marketsim import IOrderQueue
@registry.expose(["Asset", "VolumeLevels"])
class VolumeLevels(VolumeLevels_Impl):
    """   Level of volume V is a price at which cumulative volume of better orders is V
    """ 
    def __init__(self, queue = None, volumeDelta = None, volumeCount = None):
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.queue = queue if queue is not None else _orderbook_Asks()
        self.volumeDelta = volumeDelta if volumeDelta is not None else 30.0
        self.volumeCount = volumeCount if volumeCount is not None else 10
        rtti.check_fields(self)
        VolumeLevels_Impl.__init__(self)
        if isinstance(queue, types.IEvent):
            event.subscribe(self.queue, self.fire, self)
        if isinstance(volumeDelta, types.IEvent):
            event.subscribe(self.volumeDelta, self.fire, self)
        if isinstance(volumeCount, types.IEvent):
            event.subscribe(self.volumeCount, self.fire, self)
    
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
    
