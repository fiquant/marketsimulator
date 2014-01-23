
package strategy.account() {
    @python.intrinsic("strategy.account._Account_Impl")
    @curried("inner")
    def Real(inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount
        
    
    @python.intrinsic("strategy.account._VirtualMarket_Impl")
    @curried("inner")
    def VirtualMarket(inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount
        
    
    def real = inner.inner_Real
    
    def virtualMarket = inner.inner_VirtualMarket
}

package strategy.weight() {
    def atanpow = f.f_AtanPow
    
    def clamp0 = f.f_Clamp0
    
    def identity_f = f.f_IdentityF
    
    def score = trader.trader_Score
    
    def unit = trader.trader_Unit
    
    def efficiency = trader.trader_Efficiency
    
    def efficiencyTrend = trader.trader_EfficiencyTrend
    
    def chooseTheBest = array.array_ChooseTheBest
    
    @curried("f")
    def AtanPow(f : Optional[IFunction[Float]] = constant(),
                base = 1.002) : IFunction[Float]
         = math.Atan(math.Pow(constant(base),f))
    
    @curried("f")
    def Clamp0(f : Optional[IFunction[Float]] = constant()) : IFunction[Float]
         = math.Max(constant(0),f)+1
    
    @curried("f")
    def IdentityF(f : Optional[IFunction[Float]] = constant()) : IFunction[Float]
         = f
    
    @python.intrinsic("strategy.weight._Score_Impl")
    @curried("trader")
    def Score(trader : IAccount = trader.SingleProxy()) : IFunction[Float]
        
    
    @curried("trader")
    def Unit(trader : IAccount = trader.SingleProxy()) : IFunction[Float]
         = constant(1.0)
    
    @curried("trader")
    def Efficiency(trader : IAccount = trader.SingleProxy()) : IFunction[Float]
         = trader.Efficiency(trader)
    
    @curried("trader")
    def EfficiencyTrend(trader : IAccount = trader.SingleProxy(),
                        alpha = 0.15) : IFunction[Float]
         = math.Derivative(math.EW.Avg(trader.Efficiency(trader),alpha))
    
    @python.intrinsic("strategy.weight._Identity_Impl")
    @curried("array")
    def IdentityL(array : Optional[List[Float]] = []) : List[Float]
        
    
    @python.intrinsic("strategy.weight._ChooseTheBest_Impl")
    @curried("array")
    def ChooseTheBest(array : Optional[List[Float]] = []) : List[Float]
        
}
