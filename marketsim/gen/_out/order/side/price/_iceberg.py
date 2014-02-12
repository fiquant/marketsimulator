def Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._side_price_iceberg import side_price_Iceberg_IFunctionFloatSideFloatIOrderGenerator as _order__curried_side_price_Iceberg_IFunctionFloatSideFloatIOrderGenerator
    from marketsim import Side
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
            return _order__curried_side_price_Iceberg_IFunctionFloatSideFloatIOrderGenerator(lotSize,proto)
    raise Exception('Cannot find suitable overload for Iceberg('+str(lotSize)+','+str(proto)+')')
