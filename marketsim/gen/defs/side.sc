/**
 * Side of a trade (Sell or Buy).
 * In fact it can also contain None values (so it is Optional[Side])
 */
type Side

@category = "Side"
package side
{
    /**
     * Function always returning Sell side
     */
    def Sell() = observableSell() : IFunction[Side]

    /**
     * Function always returning Buy side
     */
    def Buy() = observableBuy() : IFunction[Side]

    /**
     * Function always returning None of type Side
     */
    def Nothing() = observableNothing() : IFunction[Side]

    /**
     * Observable always equal to Sell side
     */
    @python.intrinsic.observable("side._Sell_Impl")
    def observableSell() : IObservable[Side]

    /**
     * Observable always equal to Buy side
     */
    @python.intrinsic.observable("side._Buy_Impl")
    def observableBuy() : IObservable[Side]

    /**
     * Observable always equal to None of type Side
     */
    @python.intrinsic.observable("side._None_Impl")
    def observableNothing() : IObservable[Side]
}
