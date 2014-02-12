def Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim.gen._out.order._curried._volume_iceberg import volume_Iceberg_IFunctionFloatFloatIOrderGenerator as _order__curried_volume_Iceberg_IFunctionFloatFloatIOrderGenerator
    from marketsim import IOrderGenerator
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return _order__curried_volume_Iceberg_IFunctionFloatFloatIOrderGenerator(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize)+','+str(proto)+')')
