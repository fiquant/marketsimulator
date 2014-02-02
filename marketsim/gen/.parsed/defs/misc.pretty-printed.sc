@category = "Basic"

package  {
    /** Function always returning *x*
     */
    @label = "C=%(x)s"
    def constant(x = 1.0) = const(x) : IFunction[Float] // defined at defs\misc.sc: 3.5
    
    /** Trivial observable always returning *x*
     */
    @python.intrinsic.function("_constant._Constant_Impl")
    @label = "C=%(x)s"
    def const(x = 1.0) : IObservable[Float] // defined at defs\misc.sc: 9.5
    
    /** Trivial observable always returning *True*
     */
    @python.intrinsic.function("_constant._True_Impl")
    @label = "True"
    def true() : IObservable[Boolean] // defined at defs\misc.sc: 16.5
    
    /** Trivial observable always returning *False*
     */
    @python.intrinsic.function("_constant._False_Impl")
    @label = "False"
    def false() : IObservable[Boolean] // defined at defs\misc.sc: 23.5
    
    /** Trivial observable always returning *undefined* or *None* value
     */
    @python.intrinsic("_constant._Null_Impl")
    def null() : () => Float // defined at defs\misc.sc: 30.5
    
    /** Returns *x* if defined and *elsePart* otherwise
     */
    @python.observable()
    @label = "If def(%(x)s) else %(elsePart)s"
    def IfDefined(x = constant(),
                  /** function to take values from when *x* is undefined */ elsePart = constant()) = if x<>null() then x else elsePart // defined at defs\misc.sc: 36.5
}
