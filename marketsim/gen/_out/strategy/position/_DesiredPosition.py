from marketsim.ops._all import Observable
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
from marketsim import context
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition_IObservableFloatISingleAssetTrader(Observable[float]):
    """ 
    """ 
    def __init__(self, desiredPosition = None, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.desiredPosition = desiredPosition if desiredPosition is not None else _const_Float(1.0)
        self.trader = trader if trader is not None else _trader_SingleProxy_()
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
        from marketsim.gen._out.trader._pendingvolume import PendingVolume_IAccount as _trader_PendingVolume_IAccount
        return _ops_Sub_IObservableFloatIObservableFloat(_ops_Sub_IObservableFloatIObservableFloat(self.desiredPosition,_trader_Position_IAccount(self.trader)),_trader_PendingVolume_IAccount(self.trader))
    
def DesiredPosition(desiredPosition = None,trader = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
    from marketsim import rtti
    if desiredPosition is None or rtti.can_be_casted(desiredPosition, IObservablefloat):
        if trader is None or rtti.can_be_casted(trader, ISingleAssetTrader):
            return DesiredPosition_IObservableFloatISingleAssetTrader(desiredPosition,trader)
    raise Exception('Cannot find suitable overload for DesiredPosition('+str(desiredPosition) +':'+ str(type(desiredPosition))+','+str(trader) +':'+ str(type(trader))+')')
