def Limit(price = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit_Float as _order__curried_sidevolume_Limit_Float
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunctionfloat):
        return _order__curried_sidevolume_Limit_Float(price)
    raise Exception('Cannot find suitable overload for Limit('+str(price) +':'+ str(type(price))+')')
