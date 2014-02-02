
type Side
@category = "Side"

package side {
    // defined at defs\side.sc: 10.5
    /** Function always returning Sell side
     */
    @python.intrinsic("side._Sell_Impl")
    def Sell() : () => Side
    
    // defined at defs\side.sc: 16.5
    /** Function always returning Buy side
     */
    @python.intrinsic("side._Buy_Impl")
    def Buy() : () => Side
    
    // defined at defs\side.sc: 22.5
    /** Function always returning None of type Side
     */
    @python.intrinsic("side._None_Impl")
    def Nothing() : () => Side
}
