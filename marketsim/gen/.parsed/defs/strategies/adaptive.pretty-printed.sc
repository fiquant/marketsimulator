
package strategy() {
    // defined at defs\strategies\adaptive.sc: 3.5
    /** Strategy that wraps another strategy and passes its orders only if *predicate* is true
     */
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(/** wrapped strategy */ inner = Noise(),
                    /** predicate to evaluate */ predicate = true()) : ISingleAssetStrategy
    
    // defined at defs\strategies\adaptive.sc: 13.5
    /** Adaptive strategy that evaluates *inner* strategy efficiency and if it is considered as good, sends orders
     */
    def TradeIfProfitable(/** wrapped strategy */ inner = Noise(),
                          /** defines how strategy trades are booked: actually traded amount or virtual market orders are
                            * used in order to estimate how the strategy would have traded if all her orders appear at market */ account = account.virtualMarket(),
                          /** given a trading account tells should it be considered as effective or not */ performance = weight.efficiencyTrend()) = Suspendable(inner,performance(account(inner))>=0)
    
    // defined at defs\strategies\adaptive.sc: 27.5
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the efficiency of the strategies is evaluated
     * These efficiencies are mapped into weights using *weight* and *normilizer*
     * functions per every strategy and *corrector* for the whole collection of weights
     * These weights are used to choose randomly a strategy to run for the next quant of time.
     * All other strategies are suspended
     */
    @python.intrinsic("strategy.multiarmed_bandit._MultiarmedBandit2_Impl")
    def MultiArmedBandit(/** original strategies that can be suspended */ strategies = [Noise()],
                         /** function creating a virtual account used for estimate efficiency of the strategy itself */ account = account.virtualMarket(),
                         /** function estimating is the strategy efficient or not */ weight = weight.efficiencyTrend(),
                         /** function that maps trader efficiency to its weight that will be used for random choice */ normalizer = weight.atanPow(),
                         /** given array of strategy weights corrects them.
                           * for example it may set to 0 all weights except the maximal one */ corrector = weight.identityL()) : ISingleAssetStrategy
    
    // defined at defs\strategies\adaptive.sc: 49.5
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     * It can be considered as a particular case for MultiArmedBandit strategy with
     * *corrector* parameter set to *chooseTheBest*
     */
    @python.intrinsic("strategy.choose_the_best._ChooseTheBest_Impl")
    def ChooseTheBest(/** original strategies that can be suspended */ strategies = [Noise()],
                      /** function creating phantom strategy used for efficiency estimation */ account = account.virtualMarket(),
                      /** function estimating is the strategy efficient or not */ performance = weight.efficiencyTrend()) : ISingleAssetStrategy
}
