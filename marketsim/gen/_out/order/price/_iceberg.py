def Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg_IFunctionFloatFloatIOrderGenerator as _order__curried_price_Iceberg_IFunctionFloatFloatIOrderGenerator
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return _order__curried_price_Iceberg_IFunctionFloatFloatIOrderGenerator(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize)+','+str(proto)+')')
