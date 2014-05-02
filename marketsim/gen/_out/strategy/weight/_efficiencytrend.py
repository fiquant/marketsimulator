def efficiencyTrend(alpha = None): 
    from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        return _strategy_weight_trader_trader_TraderEfficiencyTrend_Float(alpha)
    raise Exception('Cannot find suitable overload for efficiencyTrend('+str(alpha) +':'+ str(type(alpha))+')')
