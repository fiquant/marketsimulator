def Limit(price = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunction[float]):
        return Limit_SideIFunctionFloatIFunctionFloat(price)
    raise Exception("Cannot find suitable overload")
