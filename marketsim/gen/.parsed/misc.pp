@category = "Basic"

package () {
    @label = "C=%(x)s"
    def constant(x = 1.0) : IFunction[Float]
         = const(x)
    
    @python.intrinsic.function("_constant._Constant_Impl")
    @label = "C=%(x)s"
    def const(x = 1.0) : IObservable[Float]
        
    
    @python.intrinsic.function("_constant._True_Impl")
    @label = "True"
    def true() : IObservable[Boolean]
        
    
    @python.intrinsic.function("_constant._False_Impl")
    @label = "False"
    def false() : IObservable[Boolean]
        
    
    @python.intrinsic("_constant._Null_Impl")
    def null() : () => Float
        
    
    @python.observable()
    @label = "If def(%(x)s) else %(elsePart)s"
    def IfDefined(x = constant(),
                  elsePart = constant())
         = if x<>null() then x else elsePart
}
