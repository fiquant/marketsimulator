def StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide
    from marketsim.gen._out.order._curried._side_price_stoploss import side_price_StopLoss_FloatSideFloatIObservableIOrder as _order__curried_side_price_StopLoss_FloatSideFloatIObservableIOrder
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide):
            return _order__curried_side_price_StopLoss_FloatSideFloatIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
