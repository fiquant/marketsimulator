package strategy.account
{
    /**
     *  Associated with a strategy account that tracks
     *  how orders sent by the strategy have been actually traded
     */
    @python.intrinsic("strategy.account._Account_Impl")
    @curried("inner")
    def Real(/** strategy to track */
             inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount

    /**
     *  Associated with a strategy account that evaluates for every order sent by the strategy
     *  how it would be traded by sending request.evalMarketOrder
     *  (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
     *  but we want evaluate in any case would it be profitable or not)
     */
    @python.intrinsic("strategy.account._VirtualMarket_Impl")
    @curried("inner")
    def VirtualMarket(  /** strategy to track */
                        inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount

    // inner => Real(inner)
    def real = inner.inner_Real

    // inner => VirtualMarket(inner)
    def virtualMarket = inner.inner_VirtualMarket
}

package strategy.weight
{
    // f => AtanPow(f, base)
    def atanpow = f.f_AtanPow
    // f => Clamp0(f)
    def clamp0 = f.f_Clamp0
    // f => IdentityF(F)
    def identity_f = f.f_IdentityF

    // trader => Score(trader)
    def score = trader.trader_Score
    // trader => Unit(score)
    def unit = trader.trader_Unit
    // trader => Efficiency(trader)
    def efficiency = trader.trader_Efficiency
    // trader => EfficiencyTrend(trader)
    def efficiencyTrend = trader.trader_EfficiencyTrend

    // array => ChooseTheBest(array)
    def chooseTheBest = array.array_ChooseTheBest

    /**
     *  scaling function = atan(base^f(x))
     */
    @curried("f")
    def AtanPow(
        /** function to scale */
        f : Optional[IFunction[Float]] = constant(),
        /** base for power function */
        base = 1.002) : IFunction[Float]

        = math.Atan(math.Pow(constant(base), f))

    /**
     *  scaling function = max(0, f(x)) + 1
     */
    @curried("f")
    def Clamp0( /** function to scale */
                f : Optional[IFunction[Float]] = constant()) : IFunction[Float]

        = math.Max(constant(0), f) + constant(1)

    /** identity scaling = f(x) */
    @curried("f")
    def IdentityF(f : Optional[IFunction[Float]] = constant()) : IFunction[Float]
        = f

    /** Calculates how many times efficiency of trader went up and went down
      * Returns difference between them.
      *
      * TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
      */
    @python.intrinsic("strategy.weight._Score_Impl")
    @curried("trader")
    def Score(  /** account in question */
                trader : IAccount = trader.SingleProxy()) : IFunction[Float]

    /**
     *  Unit function. Used to simulate uniform random choice of a strategy
     */
    @curried("trader")
    def Unit(   /** account in question */
                trader : IAccount = trader.SingleProxy()) : IFunction[Float]

        = constant(1.)

    /**
     *  Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    @curried("trader")
    def Efficiency( /** account in question */
                    trader : IAccount = trader.SingleProxy()) : IFunction[Float]

        = trader.Efficiency(trader)

    /**
     *  Returns first derivative of a moving average of the trader efficiency
     */
    @curried("trader")
    def EfficiencyTrend(
            /** account in question */
            trader : IAccount = trader.SingleProxy(),
            /** parameter alpha for the moving average */
            alpha = 0.15) : IFunction[Float]

        = math.Derivative(
                math.EW.Avg(trader.Efficiency(trader),
                            alpha))

    /**
     *   Identity function for an array of floats
     */
    @python.intrinsic("strategy.weight._Identity_Impl")
    @curried("array")
    def IdentityL(array : Optional[List[Float]] = []) : List[Float]

    /**
     *  Function returning an array of length *len(array)*
     *  having 1 at the index of the maximal element and 0 are at the rest
     */
    @python.intrinsic("strategy.weight._ChooseTheBest_Impl")
    @curried("array")
    def ChooseTheBest(array : Optional[List[Float]] = []) : List[Float]
}
