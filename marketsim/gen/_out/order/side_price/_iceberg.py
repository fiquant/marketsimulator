def Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim.gen._out.order._curried._sideprice_iceberg import sideprice_Iceberg_IFunctionFloatSideFloatIOrderGenerator as _order__curried_sideprice_Iceberg
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]]):
            return _order__curried_sideprice_Iceberg(lotSize,proto)
    raise Exception("Cannot find suitable overload")
