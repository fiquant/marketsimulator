package strategy
{
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(inner = Noise(), predicate = true() : IFunction[Boolean]) : ISingleAssetStrategy

    def TradeIfProfitable(
                inner       = Noise(),
                account     = account._.inner.inner_VirtualMarket(),
                performance = weight._.trader.trader_EfficiencyTrend())

        =   Suspendable(inner, performance(account(inner)) >= 0)

    /**
     * A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     * The choice is made randomly among the strategies that have
     * a positive efficiency trend, weighted by the efficiency value.
     */
    @python.intrinsic("strategy.multiarmed_bandit._MultiarmedBandit2_Impl")
    def MultiArmedBandit(
            /** original strategies that can be suspended */
            strategies = [Noise()],
            /** function creating phantom strategy used for efficiency estimation */
            account    = account._.inner.inner_VirtualMarket(),
            /** function estimating is the strategy efficient or not */
            weight     = weight._.trader.trader_EfficiencyTrend(),
            normalizer = weight._.f.f_AtanPow(),
            /** weighting scheme for choosing strategies */
            corrector  = weight._.array.array_IdentityL()) : ISingleAssetStrategy

    /**
     * A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     */
    @python.intrinsic("strategy.choose_the_best._ChooseTheBest_Impl")
    def ChooseTheBest(
            /** original strategies that can be suspended */
            strategies = [Noise()],
            /** function creating phantom strategy used for efficiency estimation */
            account    = account._.inner.inner_VirtualMarket(),
            /** function estimating is the strategy efficient or not */
            performance= weight._.trader.trader_EfficiencyTrend()) : ISingleAssetStrategy

    package account
    {
        @python.intrinsic("strategy.account._Account_Impl")
        @curried("inner")
        def Real(inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount

        @python.intrinsic("strategy.account._VirtualMarket_Impl")
        @curried("inner")
        def VirtualMarket(inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount

        def real = _.inner.inner_Real
        def virtualMarket = _.inner.inner_VirtualMarket
    }

    package weight
    {
        def atanpow = _.f.f_AtanPow
        def clamp0 = _.f.f_Clamp0
        def identity_f = _.f.f_IdentityF

        def score = _.trader.trader_Score
        def unit = _.trader.trader_Unit
        def efficiency = _.trader.trader_Efficiency
        def efficiencyTrend = _.trader.trader_EfficiencyTrend

        @curried("f")
        def AtanPow(f : Optional[IFunction[Float]] = constant(), base = 1.002) : IFunction[Float]
            = mathops.Atan(mathops.Pow(constant(base), f))

        @curried("f")
        def Clamp0(f : Optional[IFunction[Float]] = constant()) : IFunction[Float]
            = observable.Max(constant(0), f) + 1

        @curried("f")
        def IdentityF(f : Optional[IFunction[Float]] = constant()) : IFunction[Float]
            = f

        @python.intrinsic("strategy.weight._Score_Impl")
        @curried("trader")
        def Score(trader : IAccount = observable.trader.SingleProxy()) : IFunction[Float]

        @curried("trader")
        def Unit(trader : IAccount = observable.trader.SingleProxy()) : IFunction[Float]
            = constant(1.)

        @curried("trader")
        def Efficiency(trader : IAccount = observable.trader.SingleProxy()) : IFunction[Float]
            = observable.trader.Efficiency(trader)

        @curried("trader")
        def EfficiencyTrend(trader : IAccount = observable.trader.SingleProxy(), alpha = 0.15) : IFunction[Float]
            = Derivative(observable.EW.Avg(observable.trader.Efficiency(trader), alpha))

        @python.intrinsic("strategy.weight._Identity_Impl")
        @curried("array")
        def IdentityL(array : Optional[List[Float]] = []) : List[Float]

        @python.intrinsic("strategy.weight._ChooseTheBest_Impl")
        @curried("array")
        def ChooseTheBest(array : Optional[List[Float]] = []) : List[Float]
    }
}

