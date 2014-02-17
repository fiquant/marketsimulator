@category = "Basic"

package () {
    // defined at defs\misc.sc: 3.5
    /** Function always returning *x*
     */
    @label = "C=%(x)s"
    def constant(x = 1.0) = const(x) : IFunction[Float]
    
    // defined at defs\misc.sc: 9.5
    /** Trivial observable always returning *x*
     */
    @python.intrinsic.observable("_constant._Constant_Impl")
    @label = "C=%(x)s"
    @trivialObservable = "true"
    def const(x = 1.0) : IObservable[Float]
    
    // defined at defs\misc.sc: 17.5
    /** Function always returning *x*
     */
    @label = "C=%(x)s"
    def constant(x = 1) = const(x) : IFunction[Int]
    
    // defined at defs\misc.sc: 23.5
    /** Trivial observable always returning *x*
     */
    @python.intrinsic.observable("_constant._Constant_Impl")
    @label = "C=%(x)s"
    @trivialObservable = "true"
    def const(x = 1) : IObservable[Int]
    
    // defined at defs\misc.sc: 31.5
    /** Function always returning *True*
     */
    @python.intrinsic.function("_constant._True_Impl")
    @label = "True"
    def true() : IFunction[Boolean]
    
    // defined at defs\misc.sc: 38.5
    /** Function always returning *False*
     */
    @python.intrinsic.function("_constant._False_Impl")
    @label = "False"
    def false() : IFunction[Boolean]
    
    // defined at defs\misc.sc: 45.5
    /** Trivial observable always returning *True*
     */
    @python.intrinsic.observable("_constant._True_Impl")
    @label = "True"
    def observableTrue() : IObservable[Boolean]
    
    // defined at defs\misc.sc: 52.5
    /** Trivial observable always returning *False*
     */
    @python.intrinsic.observable("_constant._False_Impl")
    @label = "False"
    def observableFalse() : IObservable[Boolean]
    
    // defined at defs\misc.sc: 59.5
    /** Trivial observable always returning *undefined* or *None* value
     */
    @python.intrinsic("_constant._Null_Impl")
    def null() : () => Float
    
    // defined at defs\misc.sc: 65.5
    /** Returns *x* if defined and *elsePart* otherwise
     */
    @python.observable()
    @label = "If def(%(x)s) else %(elsePart)s"
    def IfDefined(x = constant(1.0),
                  /** function to take values from when *x* is undefined */ elsePart = constant(1.0)) = if x<>null() then x else elsePart
}
