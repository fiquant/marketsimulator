def FixedBudget(budget = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if budget is None or rtti.can_be_casted(budget, IFunction[float]):
        return FixedBudget_SideIFunctionFloat(budget)
    raise Exception("Cannot find suitable overload")
