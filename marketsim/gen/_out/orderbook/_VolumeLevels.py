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
        from marketsim import IVolumeLevels
        from marketsim.ops._all import Observable
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import rtti
        Observable[IVolumeLevels].__init__(self)
        self.queue = queue if queue is not None else _orderbook_Asks_IOrderBook()
        
        self.volumeDelta = volumeDelta if volumeDelta is not None else 30.0
        
        self.volumeCount = volumeCount if volumeCount is not None else 10
        
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
    
def VolumeLevels(queue = None,volumeDelta = None,volumeCount = None): 
    from marketsim import IOrderQueue
    from marketsim import float
    from marketsim import int
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if volumeDelta is None or rtti.can_be_casted(volumeDelta, float):
            if volumeCount is None or rtti.can_be_casted(volumeCount, int):
                return VolumeLevels_IOrderQueueFloatInt(queue,volumeDelta,volumeCount)
    raise Exception('Cannot find suitable overload for VolumeLevels('+str(queue)+','+str(volumeDelta)+','+str(volumeCount)+')')
