@python = "no"

package trash {
    package types {
        type T1 = T
        
        package  {
            type T
        }
        
        package  {
            type R : T
        }
        
        package  {
            package  {
                type U : T, R
            }
        }
    }
    
    abstract package _base1 {
        // defined at defs\trash.sc: 23.27
        def toInject1() : () => Int
    }
    
    abstract package _base2 {
        // defined at defs\trash.sc: 24.27
        def toInject2() : () => Int
    }
    
    // defined at defs\trash.sc: 26.1
    def A(x = in1.in2.A()) : () => types.R
    
    package in1 extends _base1 extends _base2 {
        // defined at defs\trash.sc: 29.1
        def A(x : () => .trash.types.T1 = .trash.A()) : () => types.U
        
        package in2 {
            // defined at defs\trash.sc: 32.1
            def A(x = constant(),
                  y = if 3>x+2 then x else x*2) : () => types.T
            
            // defined at defs\trash.sc: 34.1
            def S1(y = "abc") = y
            
            // defined at defs\trash.sc: 36.1
            def S2() : Optional[String] = S1()
            
            // defined at defs\trash.sc: 38.1
            def C(x : IFunction[CandleStick],
                  p = [12,23.2,0]) = p
            
            // defined at defs\trash.sc: 40.1
            def IntFunc() : IFunction[Int]
            
            // defined at defs\trash.sc: 42.1
            def F(x = IntFunc() : IFunction[Float]) = x
            
            // defined at defs\trash.sc: 44.1
            def IntObs() : IObservable[Int]
            
            // defined at defs\trash.sc: 46.1
            def O(x = IntObs() : IObservable[Float]) = x
        }
    }
}
