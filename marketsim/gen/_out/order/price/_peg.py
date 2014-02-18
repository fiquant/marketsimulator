def Peg(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out.order._curried._price_peg import price_Peg_FloatIObservableIOrder as _order__curried_price_Peg_FloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
        return _order__curried_price_Peg_FloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto) +':'+ str(type(proto))+')')
