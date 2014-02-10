def Limit(side = None,volume = None): 
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if volume is None or rtti.can_be_casted(volume, IFunction[float]):
            return Limit_SideIFunctionFloatIFunctionFloat(side,volume)
    raise Exception("Cannot find suitable overload")
