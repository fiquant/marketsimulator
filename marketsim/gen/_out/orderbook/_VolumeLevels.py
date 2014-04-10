from marketsim import registry
from marketsim.gen._out._observable._observableivolumelevels import ObservableIVolumeLevels
from marketsim.gen._out._ivolumelevels import IVolumeLevels
from marketsim.gen._intrinsic.orderbook.volume_levels import VolumeLevels_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "VolumeLevels"])
class VolumeLevels_IOrderQueueFloatInt(ObservableIVolumeLevels,VolumeLevels_Impl):
    """ **Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]**
    
      Level of volume V is a price at which cumulative volume of better orders is V
    
    Parameters are:
    
    **queue**
    
    **volumeDelta**
    	 distance between two volumes 
    
    **volumeCount**
    	 number of volume levels to track 
    """ 
    def __init__(self, queue = None, volumeDelta = None, volumeCount = None):
        from marketsim import rtti
        from marketsim.gen._out._observable._observableivolumelevels import ObservableIVolumeLevels
        from marketsim.gen._out._ivolumelevels import IVolumeLevels
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        ObservableIVolumeLevels.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
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
        return "VolumeLevels(%(queue)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
def VolumeLevels(queue = None,volumeDelta = None,volumeCount = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if volumeDelta is None or rtti.can_be_casted(volumeDelta, float):
            if volumeCount is None or rtti.can_be_casted(volumeCount, int):
                return VolumeLevels_IOrderQueueFloatInt(queue,volumeDelta,volumeCount)
    raise Exception('Cannot find suitable overload for VolumeLevels('+str(queue) +':'+ str(type(queue))+','+str(volumeDelta) +':'+ str(type(volumeDelta))+','+str(volumeCount) +':'+ str(type(volumeCount))+')')
