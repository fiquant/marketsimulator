def Market(side = None): 
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        return Market_SideIFunctionFloat(side)
    raise Exception("Cannot find suitable overload")
