def Limit(price = None,volume = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunction[float]):
        if volume is None or rtti.can_be_casted(volume, IFunction[float]):
            return Limit_SideIFunctionFloatIFunctionFloat(price,volume)
    raise Exception("Cannot find suitable overload")
