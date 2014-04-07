@category = "internal tests"
@method = "N/A"

package _test() {@X = "X"
    @Y = "Y"
    
    package A.B() {
        // defined at defs\trash.sc: 8.5
        @X = "Xa"
        def f() : () => Float
        @X = "Xb"
        
        package () {
            // defined at defs\trash.sc: 13.9
            def g() : () => Float
            
            // defined at defs\trash.sc: 14.9
            def h() : () => Float
        }
    }
    
    package types() {
        type T1 = T
        
        type T
        
        type R : T
        
        type U : R
    }
    
    package overloading() {
        // defined at defs\trash.sc: 30.5
        def f(x : IFunction[Price]) = x
        
        // defined at defs\trash.sc: 31.5
        def f(x : IFunction[Volume]) = x
        
        // defined at defs\trash.sc: 33.5
        def g(x : IFunction[Volume]) = f(x)
        
        // defined at defs\trash.sc: 35.5
        def h() = f(12)
        
        // defined at defs\trash.sc: 36.5
        def hh() = f(12.2)
    }
    
    abstract package _base1() {
        // defined at defs\trash.sc: 40.27
        def toInject1() : () => Int
    }
    
    abstract package _base2() {
        // defined at defs\trash.sc: 41.27
        def toInject2() : () => Int
    }
    
    // defined at defs\trash.sc: 43.1
    def A(x = in1.in2.A()) : () => types.R
    
    package in1() extends _base1 extends _base2 {
        // defined at defs\trash.sc: 46.1
        def A(x : () => ._test.types.T1 = ._test.A()) : () => types.U
        
        package in2() {
            // defined at defs\trash.sc: 49.1
            def A(x = constant(),
                  y = if 3>x+2 then x else x*2) : () => types.T
            
            // defined at defs\trash.sc: 51.1
            def S1(y = "abc") = y
            
            // defined at defs\trash.sc: 53.1
            def S2() : Optional[String] = S1()
            
            // defined at defs\trash.sc: 55.1
            def C(x : IFunction[ICandleStick],
                  p = 12) = p
            
            // defined at defs\trash.sc: 57.1
            def IntFunc() : IFunction[Int] = const(0)
            
            // defined at defs\trash.sc: 59.1
            def F(x = IntFunc() : IFunction[Float]) = x
            
            // defined at defs\trash.sc: 61.1
            def IntObs() : IObservable[Int] = const(0)
            
            // defined at defs\trash.sc: 63.1
            def O(x = IntObs() : IObservable[Float]) = x
        }
    }
}
