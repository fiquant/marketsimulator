def StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out.order._curried._volume_price_stoploss import volume_price_StopLoss_FloatFloatFloatIObservableIOrder as _order__curried_volume_price_StopLoss_FloatFloatFloatIObservableIOrder
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
            return _order__curried_volume_price_StopLoss_FloatFloatFloatIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
