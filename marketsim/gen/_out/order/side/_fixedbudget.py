def FixedBudget(budget = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim.gen._out.order._curried._side_fixedbudget import side_FixedBudget_IFunctionFloat as _order__curried_side_FixedBudget
    from marketsim import rtti
    if budget is None or rtti.can_be_casted(budget, IFunction[float]):
        return _order__curried_side_FixedBudget(budget)
    raise Exception('Cannot find suitable overload for FixedBudget('+str(budget)+')')
