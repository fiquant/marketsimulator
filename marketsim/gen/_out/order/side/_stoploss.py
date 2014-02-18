def StopLoss(maxloss = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out.order._curried._side_stoploss import side_StopLoss_FloatSideIObservableIOrder as _order__curried_side_StopLoss_FloatSideIObservableIOrder
    from marketsim import rtti
    if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
            return _order__curried_side_StopLoss_FloatSideIObservableIOrder(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss) +':'+ str(type(maxloss))+','+str(proto) +':'+ str(type(proto))+')')
