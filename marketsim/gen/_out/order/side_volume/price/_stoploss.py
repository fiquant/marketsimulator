def StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat
    from marketsim.gen._out.order._curried._sidevolume_price_stoploss import sidevolume_price_StopLoss_FloatSideFloatFloatIObservableIOrder as _order__curried_sidevolume_price_StopLoss_FloatSideFloatFloatIObservableIOrder
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat):
            return _order__curried_sidevolume_price_StopLoss_FloatSideFloatFloatIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
