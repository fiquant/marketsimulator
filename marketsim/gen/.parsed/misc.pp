@category = "Basic"

package () {
    /** Function always returning *x*
     */
    @label = "C=%(x)s"
    def constant(x = 1.0)
         = const(x) : IFunction[Float]
    
    /** Trivial observable always returning *x*
     */
    @python.intrinsic.function("_constant._Constant_Impl")
    @label = "C=%(x)s"
    def const(x = 1.0) : IObservable[Float]
        
    
    /** Trivial observable always returning *True*
     */
    @python.intrinsic.function("_constant._True_Impl")
    @label = "True"
    def true() : IObservable[Boolean]
        
    
    /** Trivial observable always returning *False*
     */
    @python.intrinsic.function("_constant._False_Impl")
    @label = "False"
    def false() : IObservable[Boolean]
        
    
    /** Trivial observable always returning *undefined* or *None* value
     */
    @python.intrinsic("_constant._Null_Impl")
    def null() : () => Float
        
    
    /** Returns *x* if defined and *elsePart* otherwise
     */
    @python.observable()
    @label = "If def(%(x)s) else %(elsePart)s"
    def IfDefined(x = constant(),
                  /** function to take values from when *x* is undefined */ elsePart = constant())
         = if x<>null() then x else elsePart
}
