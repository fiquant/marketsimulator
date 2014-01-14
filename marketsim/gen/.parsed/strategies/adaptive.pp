
package strategy {
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(inner = Noise(),
                    predicate = true()) : ISingleAssetStrategy
        
    
    package account {
        @python.intrinsic("strategy.account._Account_Impl")
        @curried()
        def Real(inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount
            
        
        @python.intrinsic("strategy.account._VirtualMarket_Impl")
        @curried()
        def VirtualMarket(inner : Optional[ISingleAssetStrategy] = Noise()) : IAccount
            
        
        def real = _.inner.inner_Real
        
        def virtualMarket = _.inner.inner_VirtualMarket
    }
}
