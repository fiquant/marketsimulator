def StopLoss(proto = None,maxloss = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionsideifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_stoploss import sidevolume_price_StopLoss_SideFloatFloatIObservableIOrderFloat as _order__curried_sidevolume_price_StopLoss_SideFloatFloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
        if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
            return _order__curried_sidevolume_price_StopLoss_SideFloatFloatIObservableIOrderFloat(proto,maxloss)
    raise Exception('Cannot find suitable overload for StopLoss('+str(proto) +':'+ str(type(proto))+','+str(maxloss) +':'+ str(type(maxloss))+')')
