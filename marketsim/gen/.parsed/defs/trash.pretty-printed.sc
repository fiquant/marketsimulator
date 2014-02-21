@category = "internal tests"
@method = "N/A"

package _test() {
    package types() {
        type T1 = T
        
        package () {
            type T
        }
        
        package () {
            type R : T
        }
        
        package () {
            package () {
                type U : R
            }
        }
    }
    
    package overloading() {
        // defined at defs\trash.sc: 26.5
        def f(x : IFunction[Price]) = x
        
        // defined at defs\trash.sc: 27.5
        def f(x : IFunction[Volume]) = x
        
        // defined at defs\trash.sc: 29.5
        def g(x : IFunction[Volume]) = f(x)
        
        // defined at defs\trash.sc: 31.5
        def h() = f(12)
        
        // defined at defs\trash.sc: 32.5
        def hh() = f(12.2)
    }
    
    abstract package _base1() {
        // defined at defs\trash.sc: 36.27
        def toInject1() : () => Int
    }
    
    abstract package _base2() {
        // defined at defs\trash.sc: 37.27
        def toInject2() : () => Int
    }
    
    // defined at defs\trash.sc: 39.1
    def A(x = in1.in2.A()) : () => types.R
    
    package in1() extends _base1 extends _base2 {
        // defined at defs\trash.sc: 42.1
        def A(x : () => ._test.types.T1 = ._test.A()) : () => types.U
        
        package in2() {
            // defined at defs\trash.sc: 45.1
            def A(x = constant(),
                  y = if 3>x+2 then x else x*2) : () => types.T
            
            // defined at defs\trash.sc: 47.1
            def S1(y = "abc") = y
            
            // defined at defs\trash.sc: 49.1
            def S2() : Optional[String] = S1()
            
            // defined at defs\trash.sc: 51.1
            def C(x : IFunction[ICandleStick],
                  p = 12) = p
            
            // defined at defs\trash.sc: 53.1
            def IntFunc() : IFunction[Int] = const(0)
            
            // defined at defs\trash.sc: 55.1
            def F(x = IntFunc() : IFunction[Float]) = x
            
            // defined at defs\trash.sc: 57.1
            def IntObs() : IObservable[Int] = const(0)
            
            // defined at defs\trash.sc: 59.1
            def O(x = IntObs() : IObservable[Float]) = x
        }
    }
}
