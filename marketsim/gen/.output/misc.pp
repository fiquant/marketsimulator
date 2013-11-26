
package observable {
    @python.observable("Pow/Log", "{%x}^2")
    def Sqr(x = constant()) = x*x
    
    @python.observable("Basic", "min{%x, %y}")
    def Min(x = constant(),
            y = constant()) = if x<y then x else y
    
    @python.observable("Basic", "max{%x, %y}")
    def Max(x = constant(),
            y = constant()) = if x>y then x else y
}

def constant(x = 1.0) : Float

package thrash {
    def A(x = in1.in2.B()) : Float
    
    package in1 {
        def C(x = A()) : Float
        
        package in2 {
            def B(x = constant(),
                  y = if 3.0>x+2.0 then x else x*2.0) : Float
        }
    }
}
