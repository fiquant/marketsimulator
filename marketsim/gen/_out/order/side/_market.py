def Market(volume = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunctionfloat):
        return _order__curried_side_Market_Float(volume)
    raise Exception('Cannot find suitable overload for Market('+str(volume) +':'+ str(type(volume))+')')
