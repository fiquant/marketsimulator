from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "TwoSide"])
class TwoSide_FloatFloatIEventSideFloatIOrderGenerator(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, initialValue = None, priceDistr = None, eventGen = None, orderFactory = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate_FloatFloat as _math_random_lognormvariate_FloatFloat
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_IFunctionFloat as _order__curried_sideprice_Limit_IFunctionFloat
        from marketsim import event
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else _math_random_lognormvariate_FloatFloat(0.0,0.1)
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float(_math_random_expovariate_Float(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_sideprice_Limit_IFunctionFloat()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'initialValue' : float,
        'priceDistr' : IFunction[float],
        'eventGen' : IEvent,
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]]
    }
    def __repr__(self):
        return "TwoSide(%(initialValue)s, %(priceDistr)s, %(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._array import Array_ListISingleAssetStrategy as _strategy_Array_ListISingleAssetStrategy
        from marketsim.gen._out.strategy.lp._oneside import OneSide_FloatFloatIEventSideFloatIOrderGeneratorIFunctionSide as _strategy_lp_OneSide_FloatFloatIEventSideFloatIOrderGeneratorIFunctionSide
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        return _strategy_Array_ListISingleAssetStrategy([_strategy_lp_OneSide_FloatFloatIEventSideFloatIOrderGeneratorIFunctionSide(self.initialValue,self.priceDistr,self.eventGen,self.orderFactory,_side_Sell_()),_strategy_lp_OneSide_FloatFloatIEventSideFloatIOrderGeneratorIFunctionSide(self.initialValue,self.priceDistr,self.eventGen,self.orderFactory,_side_Buy_())])
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def TwoSide(initialValue = None,priceDistr = None,eventGen = None,orderFactory = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if initialValue is None or rtti.can_be_casted(initialValue, float):
        if priceDistr is None or rtti.can_be_casted(priceDistr, IFunction[float]):
            if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
                if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]
                ,IFunction[float]]):
                    return TwoSide_FloatFloatIEventSideFloatIOrderGenerator(initialValue,priceDistr,eventGen,orderFactory)
    raise Exception('Cannot find suitable overload for TwoSide('+str(initialValue)+','+str(priceDistr)+','+str(eventGen)+','+str(orderFactory)+')')
