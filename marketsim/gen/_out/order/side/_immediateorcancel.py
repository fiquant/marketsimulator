def ImmediateOrCancel(proto = None): 
    from marketsim import IOrderGenerator
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]]):
        return ImmediateOrCancel_IOrderGenerator(proto)
    raise Exception("Cannot find suitable overload")
