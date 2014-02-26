def Market(signedVolume = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._marketsigned import MarketSigned_Float as _order_MarketSigned_Float
    from marketsim import rtti
    if signedVolume is None or rtti.can_be_casted(signedVolume, IFunctionfloat):
        return _order_MarketSigned_Float(signedVolume)
    raise Exception('Cannot find suitable overload for Market('+str(signedVolume) +':'+ str(type(signedVolume))+')')
