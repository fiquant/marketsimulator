def Market(signedVolume = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim.gen._out.order._marketsigned import MarketSigned_Float as _order_MarketSigned
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunction[float]):
        return _order_MarketSigned(signedVolume)
    raise Exception("Cannot find suitable overload")
