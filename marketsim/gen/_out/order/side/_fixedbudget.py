def FixedBudget(budget = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._side_fixedbudget import side_FixedBudget_Float as _order__curried_side_FixedBudget_Float
    from marketsim import rtti
    if budget is None or rtti.can_be_casted(budget, IFunctionfloat):
        return _order__curried_side_FixedBudget_Float(budget)
    raise Exception('Cannot find suitable overload for FixedBudget('+str(budget) +':'+ str(type(budget))+')')
