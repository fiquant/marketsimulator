def Iceberg(lotSize = None,proto = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if lotSize is None or rtti.can_be_casted(lotSize, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return price_Iceberg_IFunctionFloatFloatIOrderGenerator(lotSize,proto)
    raise Exception("Cannot find suitable overload")
