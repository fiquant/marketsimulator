def Peg(proto = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_peg import sidevolume_price_Peg_SideFloatFloatIObservableIOrder as _order__curried_sidevolume_price_Peg_SideFloatFloatIObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSideIFunctionfloat):
        return _order__curried_sidevolume_price_Peg_SideFloatFloatIObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for Peg('+str(proto) +':'+ str(type(proto))+')')
