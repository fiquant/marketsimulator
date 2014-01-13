package strategy
{
    @python.intrinsic("strategy.suspendable._Suspendable_Impl")
    def Suspendable(inner = Noise(), predicate = true()) : ISingleAssetStrategy
}