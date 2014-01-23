
package strategy() {
    /** Strategy that wraps another strategy and passes its orders only if *predicate* is true
     */
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(/** wrapped strategy */ inner = Noise(),
                    /** predicate to evaluate */ predicate = true() : IFunction[Boolean]) : ISingleAssetStrategy
        
    
    /** Adaptive strategy that evaluates *inner* strategy efficiency and if it is considered as good, sends orders
     */
    def TradeIfProfitable(/** wrapped strategy */ inner = Noise(),
                          /** defines how strategy trades are booked: actually traded amount or virtual market orders are
                            * used in order to estimate how the strategy would have traded if all her orders appear at market */ account = account.inner.inner_VirtualMarket(),
                          /** given a trading account tells should it be considered as effective or not */ performance = weight.trader.trader_EfficiencyTrend())
         = Suspendable(inner,performance(account(inner))>=0)
    
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     * The choice is made randomly among the strategies that have
     * a positive efficiency trend, weighted by the efficiency value.
     */
    @python.intrinsic("strategy.multiarmed_bandit._MultiarmedBandit2_Impl")
    def MultiArmedBandit(/** original strategies that can be suspended */ strategies = [Noise()],
                         /** function creating phantom strategy used for efficiency estimation */ account = account.inner.inner_VirtualMarket(),
                         /** function estimating is the strategy efficient or not */ weight = weight.trader.trader_EfficiencyTrend(),
                         normalizer = weight.f.f_AtanPow(),
                         /** weighting scheme for choosing strategies */ corrector = weight.array.array_IdentityL()) : ISingleAssetStrategy
        
    
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     */
    @python.intrinsic("strategy.choose_the_best._ChooseTheBest_Impl")
    def ChooseTheBest(/** original strategies that can be suspended */ strategies = [Noise()],
                      /** function creating phantom strategy used for efficiency estimation */ account = account.inner.inner_VirtualMarket(),
                      /** function estimating is the strategy efficient or not */ performance = weight.trader.trader_EfficiencyTrend()) : ISingleAssetStrategy
        
}
