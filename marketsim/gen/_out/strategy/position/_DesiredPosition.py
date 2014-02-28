from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition_IObservableFloatISingleAssetTrader(Observablefloat):
    """ 
    """ 
    def __init__(self, desiredPosition = None, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.desiredPosition = desiredPosition if desiredPosition is not None else call(_const_Float,1.0)
        self.trader = trader if trader is not None else call(_trader_SingleProxy_,)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'desiredPosition' : IObservablefloat,
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "DesiredPosition(%(desiredPosition)s, %(trader)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatIObservableFloat as _ops_Sub_IObservableFloatIObservableFloat
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position_IAccount
        from marketsim import call
        from marketsim.gen._out.trader._pendingvolume import PendingVolume_IAccount as _trader_PendingVolume_IAccount
        return call(_ops_Sub_IObservableFloatIObservableFloat,call(_ops_Sub_IObservableFloatIObservableFloat,self.desiredPosition,call(_trader_Position_IAccount,self.trader)),call(_trader_PendingVolume_IAccount,self.trader))
    
def DesiredPosition(desiredPosition = None,trader = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
    from marketsim import rtti
    if desiredPosition is None or rtti.can_be_casted(desiredPosition, IObservablefloat):
        if trader is None or rtti.can_be_casted(trader, ISingleAssetTrader):
            return DesiredPosition_IObservableFloatISingleAssetTrader(desiredPosition,trader)
    raise Exception('Cannot find suitable overload for DesiredPosition('+str(desiredPosition) +':'+ str(type(desiredPosition))+','+str(trader) +':'+ str(type(trader))+')')
