
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
    
    package observable {
        // defined at defs\side.sc: 29.9
        /** Observable always equal to Sell side
         */
        @python.intrinsic.observable("side._Sell_Impl")
        def Sell() : IObservable[Side]
        
        // defined at defs\side.sc: 35.9
        /** Observable always equal to Buy side
         */
        @python.intrinsic.observable("side._Buy_Impl")
        def Buy() : IObservable[Side]
        
        // defined at defs\side.sc: 41.9
        /** Observable always equal to None of type Side
         */
        @python.intrinsic.observable("side._None_Impl")
        def Nothing() : IObservable[Side]
    }
}
