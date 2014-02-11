def Peg(proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_price_peg import volume_price_Peg_FloatFloatIOrderGenerator as _order__curried_volume_price_Peg
    if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
        return _order__curried_volume_price_Peg(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto)+')')
