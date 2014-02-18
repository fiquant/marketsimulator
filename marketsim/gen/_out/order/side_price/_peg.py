def Peg(proto = None): 
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out.order._curried._sideprice_peg import sideprice_Peg_SideFloatIObservableIOrder as _order__curried_sideprice_Peg_SideFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
        return _order__curried_sideprice_Peg_SideFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto) +':'+ str(type(proto))+')')
