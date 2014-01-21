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
    @python.intrinsic("side._Sell_Impl")
    def Sell() => Side

    /**
     * Function always returning Buy side
     */
    @python.intrinsic("side._Buy_Impl")
    def Buy() => Side

    /**
     * Function always returning None of type Side
     */
    @python.intrinsic("side._None_Impl")
    def Nothing() => Side
}
