def Limit(side = None,price = None): 
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if price is None or rtti.can_be_casted(price, IFunction[float]):
            return Limit_SideIFunctionFloatIFunctionFloat(side,price)
    raise Exception("Cannot find suitable overload")
