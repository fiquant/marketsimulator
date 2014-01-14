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
    
    def A(x = in1.in2.A()) : () => types.R
        
    
    package in1 {
        def A(x : () => .trash.types.T1 = .trash.A()) : () => types.U
            
        
        package in2 {
            def A(x = constant(),
                  y = if 3>x+2 then x else x*2) : () => types.T
                
            
            def S1(y = "abc")
                 = y
            
            def S2() : Optional[String]
                 = S1()
            
            def C(x : IFunction[CandleStick],
                  p = [12,23.2,0])
                 = p
            
            def IntFunc() : IFunction[Int]
                
            
            def F(x = IntFunc() : IFunction[Float])
                 = x
            
            def IntObs() : IObservable[Int]
                
            
            def O(x = IntObs() : IObservable[Float])
                 = x
        }
    }
}
