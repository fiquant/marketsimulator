def StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionfloat
    from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss_FloatFloatIObservableIOrder as _order__curried_price_StopLoss_FloatFloatIObservableIOrder
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionfloat):
            return _order__curried_price_StopLoss_FloatFloatIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
