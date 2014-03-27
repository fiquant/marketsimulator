
type Side
@category = "Side"

package side() {
    // defined at defs\side.sc: 10.5
    /** Function always returning Sell side
     */
    def Sell() = observableSell() : IFunction[Side]
    
    // defined at defs\side.sc: 15.5
    /** Function always returning Buy side
     */
    def Buy() = observableBuy() : IFunction[Side]
    
    // defined at defs\side.sc: 20.5
    /** Function always returning None of type Side
     */
    def Nothing() = observableNothing() : IFunction[Side]
    
    // defined at defs\side.sc: 25.5
    /** Observable always equal to Sell side
     */
    @python.intrinsic.observable("side.Sell_Impl")
    def observableSell() : IObservable[Side]
    
    // defined at defs\side.sc: 31.5
    /** Observable always equal to Buy side
     */
    @python.intrinsic.observable("side.Buy_Impl")
    def observableBuy() : IObservable[Side]
    
    // defined at defs\side.sc: 37.5
    /** Observable always equal to None of type Side
     */
    @python.intrinsic.observable("side.None_Impl")
    def observableNothing() : IObservable[Side]
}
