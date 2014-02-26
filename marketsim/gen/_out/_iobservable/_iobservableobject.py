from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction import IFunctionobject
class IObservableobject(IEvent, IFunctionobject):
    def TimeSerie(self, graph = None,_digitsToShow = None,_smooth = None):
        from marketsim.gen._out._timeserie import TimeSerie
        return TimeSerie(self,graph,_digitsToShow,_smooth)
    
    pass
