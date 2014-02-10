def Limit(volume = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunction[float]):
        return Limit_SideIFunctionFloatIFunctionFloat(volume)
    raise Exception("Cannot find suitable overload")
