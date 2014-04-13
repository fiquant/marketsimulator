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
    @python.intrinsic.observable("_constant.Constant_Impl")
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
    @python.intrinsic.observable("_constant.Constant_Impl")
    @label = "C=%(x)s"
    @trivialObservable = "true"
    def const(x = 1) : IObservable[Int]
    
    // defined at defs\misc.sc: 31.5
    /** Function always returning *True*
     */
    @label = "True"
    def true() = observableTrue() : IFunction[Boolean]
    
    // defined at defs\misc.sc: 37.5
    /** Function always returning *False*
     */
    @label = "False"
    def false() = observableFalse() : IFunction[Boolean]
    
    // defined at defs\misc.sc: 43.5
    /** Trivial observable always returning *True*
     */
    @python.intrinsic.observable("_constant.True_Impl")
    @label = "True"
    def observableTrue() : IObservable[Boolean]
    
    // defined at defs\misc.sc: 50.5
    /** Trivial observable always returning *False*
     */
    @python.intrinsic.observable("_constant.False_Impl")
    @label = "False"
    def observableFalse() : IObservable[Boolean]
    
    // defined at defs\misc.sc: 57.5
    /** Trivial observable always returning *undefined* or *None* value
     */
    @python.intrinsic("_constant.Null_Impl")
    def null() : () => Float
    
    // defined at defs\misc.sc: 63.5
    /** Returns *x* if defined and *elsePart* otherwise
     */
    @python.observable()
    @label = "If def(%(x)s) else %(elsePart)s"
    @method = "getOrElse"
    def IfDefined(x = constant(1.0),
                  /** function to take values from when *x* is undefined */ elsePart = constant(1.0)) = if x<>null() then x else elsePart
    
    // defined at defs\misc.sc: 76.5
    @python.intrinsic("event.CurrentTime_Impl")
    def CurrentTime() : IObservable[Float]
}
