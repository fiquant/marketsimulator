def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_peg import volume_Peg_FloatFloatIOrderGenerator as _order__curried_volume_Peg_FloatFloatIOrderGenerator
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
        return _order__curried_volume_Peg_FloatFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto)+')')
