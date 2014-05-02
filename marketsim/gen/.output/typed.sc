@category = "Side"

package side {
    /** Observable always equal to Buy side
     */
    
    @python.intrinsic.observable("side.Buy_Impl")
    def observableBuy() : .IObservable[.Side]
    
    /** Function always returning None of type Side
     */
    
    def Nothing() : () => .Side
        	 = .side.observableNothing() : () => .Side
    
    /** Function always returning Buy side
     */
    
    def Buy() : () => .Side
        	 = .side.observableBuy() : () => .Side
    
    /** Observable always equal to None of type Side
     */
    
    @python.intrinsic.observable("side.None_Impl")
    def observableNothing() : .IObservable[.Side]
    
    /** Observable always equal to Sell side
     */
    
    @python.intrinsic.observable("side.Sell_Impl")
    def observableSell() : .IObservable[.Side]
    
    /** Function always returning Sell side
     */
    
    def Sell() : () => .Side
        	 = .side.observableSell() : () => .Side
}

@category = "Event"
@method = "N/A"

package event {
    type IScheduler
    
    type ISubscription
    
    @python.intrinsic("event.GreaterThan_Impl")
    def GreaterThan(bound : .Float,
                    target : Any) : Any
    
    /** Event that once at *delay*
     */
    
    @python.intrinsic("event.After_Impl")
    def After(/** when the event should be fired */ delay : Optional[() => .Float] = .constant(10.0)) : .IEvent
    
    
    @python.intrinsic("event.Event_Impl")
    def Event() : .IEvent
    
    /** Scheduler that manages the future event set.
     * Must be a singleton
     */
    
    @python.intrinsic("scheduler.Scheduler_Impl")
    def createScheduler(currentTime : Optional[.Float] = 0.0) : .event.IScheduler
    
    /** Returns reference to the instance of the scheduler
     */
    
    @python.intrinsic("scheduler.currentScheduler_Impl")
    def Scheduler() : .event.IScheduler
    
    
    @python.intrinsic("event.LessThan_Impl")
    def LessThan(bound : .Float,
                 target : Any) : Any
    
    
    @python.intrinsic("event.Subscription_Impl")
    def Subscription(event : Any,
                     listener : Any) : .event.ISubscription
    
    /** Event that fires every *intervalFunc* moments of time
     */
    
    @python.intrinsic("event.Every_Impl")
    def Every(/** interval of time between two events */ intervalFunc : Optional[() => .Float] = .math.random.expovariate(1.0)) : .IEvent
}

@category = "internal tests"
@method = "N/A"

package _test {
    package A {@X = "X"
        @Y = "Y"
        
        package B {
            @X = "Xa"
            
            def f() : () => .Float
            
            @X = "Xb"
            
            def g() : () => .Float
            
            @X = "Xb"
            
            def h() : () => .Float
        }
        
    }
    
    
    package in1 {
        package in2 {
            
            def S1(y : Optional[.String] = "abc") : .String
                	 = y
            
            
            def F(x : Optional[() => .Float] = ._test.in1.in2.IntFunc() : () => .Float) : () => .Float
                	 = x
            
            
            def A(x : Optional[() => .Int] = .constant(),
                  y : Optional[() => .Float] = .ops.Condition(.ops.Greater(.constant(3),.ops.Add(x,.constant(2))),x,.ops.Mul(x,.constant(2)))) : () => ._test.types.T
            
            
            def IntObs() : .IObservable[.Int]
                	 = .const(0)
            
            
            def IntFunc() : () => .Int
                	 = .const(0)
            
            
            def C(x : () => .ICandleStick,
                  p : Optional[.Int] = 12) : .Int
                	 = p
            
            
            def S2() : Optional[.String]
                	 = ._test.in1.in2.S1()
            
            
            def O(x : Optional[.IObservable[.Float]] = ._test.in1.in2.IntObs() : .IObservable[.Float]) : .IObservable[.Float]
                	 = x
        }
        
        
        def A(x : () => ._test.types.T = ._test.A()) : () => ._test.types.U
        
        
        def toInject1() : () => .Int
        
        
        def toInject2() : () => .Int
    }
    
    
    package types {
        type T
        
        type T1 = T
        
        type R : T
        
        type U : R
    }
    
    
    package overloading {
        
        def f(x : () => .Int) : () => .Int
            	 = x
        
        
        def f(x : () => .Float) : () => .Float
            	 = x
        
        
        def g(x : () => .Int) : () => .Int
            	 = ._test.overloading.f(x)
        
        
        def h() : () => .Int
            	 = ._test.overloading.f(.constant(12))
        
        
        def hh() : () => .Float
            	 = ._test.overloading.f(.constant(12.2))
    }
    
    
    def A(x : Optional[() => ._test.types.T] = ._test.in1.in2.A()) : () => ._test.types.R
}

@category = "N/A"

package veusz {
    /** Graph to render at Veusz. Time series are added to it automatically in their constructor
     */
    
    @python.intrinsic("veusz.Graph_Impl")
    def Graph(name : Optional[.String] = "graph") : .IGraph
    
    
    @python.intrinsic("veusz.CSV_Impl")
    def CSV(directory : .String,
            source : Any,
            attributes : Any) : Any
}

@category = "Ops"

package ops {
    @label = "-%(x)s"
    
    @python.intrinsic.observable("ops.Negate_Impl")
    def Negate(x : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "-%(x)s"
    
    @python.intrinsic.observable("ops.Negate_Impl")
    def Negate(x : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "+"
    
    @python.intrinsic.observable("ops.Add_Impl")
    def Add(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "+"
    
    @python.intrinsic.observable("ops.Add_Impl")
    def Add(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "+"
    
    @python.intrinsic.observable("ops.Add_Impl")
    def Add(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "+"
    
    @python.intrinsic.observable("ops.Add_Impl")
    def Add(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[.IObservable[.Float]] = .const(1.0),
                  elsepart : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[.IObservable[.Side]] = .side.observableSell(),
                  elsepart : Optional[.IObservable[.Side]] = .side.observableBuy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  elsepart : Optional[.IObservable[.Boolean]] = .observableFalse()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[.IObservable[.Float]] = .const(1.0),
                  elsepart : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[() => .Float] = .constant(1.0),
                  elsepart : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[.IObservable[.Float]] = .const(1.0),
                  elsepart : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[.IObservable[.Side]] = .side.observableSell(),
                  elsepart : Optional[.IObservable[.Side]] = .side.observableBuy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[() => .Side] = .side.Sell(),
                  elsepart : Optional[.IObservable[.Side]] = .side.observableBuy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[.IObservable[.Side]] = .side.observableSell(),
                  elsepart : Optional[() => .Side] = .side.Buy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  elsepart : Optional[.IObservable[.Boolean]] = .observableFalse()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[() => .Boolean] = .true(),
                  elsepart : Optional[.IObservable[.Boolean]] = .observableFalse()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  elsepart : Optional[() => .Boolean] = .false()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[() => .Float] = .constant(1.0),
                  elsepart : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[.IObservable[.Float]] = .const(1.0),
                  elsepart : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[() => .Float] = .constant(1.0),
                  elsepart : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[() => .Side] = .side.Sell(),
                  elsepart : Optional[.IObservable[.Side]] = .side.observableBuy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[.IObservable[.Side]] = .side.observableSell(),
                  elsepart : Optional[() => .Side] = .side.Buy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[() => .Side] = .side.Sell(),
                  elsepart : Optional[() => .Side] = .side.Buy()) : .IObservable[.Side]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[() => .Boolean] = .true(),
                  elsepart : Optional[.IObservable[.Boolean]] = .observableFalse()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  elsepart : Optional[() => .Boolean] = .false()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[.IObservable[.Boolean]] = .observableTrue(),
                  ifpart : Optional[() => .Boolean] = .true(),
                  elsepart : Optional[() => .Boolean] = .false()) : .IObservable[.Boolean]
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[() => .Float] = .constant(1.0),
                  elsepart : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[() => .Side] = .side.Sell(),
                  elsepart : Optional[() => .Side] = .side.Buy()) : () => .Side
    
    @label = "(if %(cond)s then %(ifpart)s else %(elsepart)s)"
    
    @python.intrinsic.observable("ops.Condition_Impl")
    def Condition(cond : Optional[() => .Boolean] = .true(),
                  ifpart : Optional[() => .Boolean] = .true(),
                  elsepart : Optional[() => .Boolean] = .false()) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<"
    
    @python.intrinsic.observable("ops.Less_Impl")
    def Less(x : Optional[.IObservable[.Float]] = .const(1.0),
             y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<"
    
    @python.intrinsic.observable("ops.Less_Impl")
    def Less(x : Optional[() => .Float] = .constant(1.0),
             y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<"
    
    @python.intrinsic.observable("ops.Less_Impl")
    def Less(x : Optional[.IObservable[.Float]] = .const(1.0),
             y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<"
    
    @python.intrinsic.observable("ops.Less_Impl")
    def Less(x : Optional[() => .Float] = .constant(1.0),
             y : Optional[() => .Float] = .constant(1.0)) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "and"
    
    @python.intrinsic.observable("ops.And_Impl")
    def And(x : Optional[.IObservable[.Boolean]] = .observableTrue(),
            y : Optional[.IObservable[.Boolean]] = .observableTrue()) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "and"
    
    @python.intrinsic.observable("ops.And_Impl")
    def And(x : Optional[() => .Boolean] = .true(),
            y : Optional[.IObservable[.Boolean]] = .observableTrue()) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "and"
    
    @python.intrinsic.observable("ops.And_Impl")
    def And(x : Optional[.IObservable[.Boolean]] = .observableTrue(),
            y : Optional[() => .Boolean] = .true()) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "and"
    
    @python.intrinsic.observable("ops.And_Impl")
    def And(x : Optional[() => .Boolean] = .true(),
            y : Optional[() => .Boolean] = .true()) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "*"
    
    @python.intrinsic.observable("ops.Mul_Impl")
    def Mul(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "*"
    
    @python.intrinsic.observable("ops.Mul_Impl")
    def Mul(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "*"
    
    @python.intrinsic.observable("ops.Mul_Impl")
    def Mul(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "*"
    
    @python.intrinsic.observable("ops.Mul_Impl")
    def Mul(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<>"
    
    @python.intrinsic.observable("ops.NotEqual_Impl")
    def NotEqual(x : Optional[.IObservable[.Float]] = .const(1.0),
                 y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<>"
    
    @python.intrinsic.observable("ops.NotEqual_Impl")
    def NotEqual(x : Optional[() => .Float] = .constant(1.0),
                 y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<>"
    
    @python.intrinsic.observable("ops.NotEqual_Impl")
    def NotEqual(x : Optional[.IObservable[.Float]] = .const(1.0),
                 y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<>"
    
    @python.intrinsic.observable("ops.NotEqual_Impl")
    def NotEqual(x : Optional[() => .Float] = .constant(1.0),
                 y : Optional[() => .Float] = .constant(1.0)) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">="
    
    @python.intrinsic.observable("ops.GreaterEqual_Impl")
    def GreaterEqual(x : Optional[.IObservable[.Float]] = .const(1.0),
                     y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">="
    
    @python.intrinsic.observable("ops.GreaterEqual_Impl")
    def GreaterEqual(x : Optional[() => .Float] = .constant(1.0),
                     y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">="
    
    @python.intrinsic.observable("ops.GreaterEqual_Impl")
    def GreaterEqual(x : Optional[.IObservable[.Float]] = .const(1.0),
                     y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">="
    
    @python.intrinsic.observable("ops.GreaterEqual_Impl")
    def GreaterEqual(x : Optional[() => .Float] = .constant(1.0),
                     y : Optional[() => .Float] = .constant(1.0)) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "-"
    
    @python.intrinsic.observable("ops.Sub_Impl")
    def Sub(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "-"
    
    @python.intrinsic.observable("ops.Sub_Impl")
    def Sub(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "-"
    
    @python.intrinsic.observable("ops.Sub_Impl")
    def Sub(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "-"
    
    @python.intrinsic.observable("ops.Sub_Impl")
    def Sub(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @label = "\\frac{%(x)s}{%(y)s}"
    
    @python.intrinsic.observable("ops.Div_Impl")
    def Div(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "\\frac{%(x)s}{%(y)s}"
    
    @python.intrinsic.observable("ops.Div_Impl")
    def Div(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    @label = "\\frac{%(x)s}{%(y)s}"
    
    @python.intrinsic.observable("ops.Div_Impl")
    def Div(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    @label = "\\frac{%(x)s}{%(y)s}"
    
    @python.intrinsic.observable("ops.Div_Impl")
    def Div(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<="
    
    @python.intrinsic.observable("ops.LessEqual_Impl")
    def LessEqual(x : Optional[.IObservable[.Float]] = .const(1.0),
                  y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<="
    
    @python.intrinsic.observable("ops.LessEqual_Impl")
    def LessEqual(x : Optional[() => .Float] = .constant(1.0),
                  y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<="
    
    @python.intrinsic.observable("ops.LessEqual_Impl")
    def LessEqual(x : Optional[.IObservable[.Float]] = .const(1.0),
                  y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "<="
    
    @python.intrinsic.observable("ops.LessEqual_Impl")
    def LessEqual(x : Optional[() => .Float] = .constant(1.0),
                  y : Optional[() => .Float] = .constant(1.0)) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "=="
    
    @python.intrinsic.observable("ops.Equal_Impl")
    def Equal(x : Optional[.IObservable[.Float]] = .const(1.0),
              y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "=="
    
    @python.intrinsic.observable("ops.Equal_Impl")
    def Equal(x : Optional[() => .Float] = .constant(1.0),
              y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "=="
    
    @python.intrinsic.observable("ops.Equal_Impl")
    def Equal(x : Optional[.IObservable[.Float]] = .const(1.0),
              y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "=="
    
    @python.intrinsic.observable("ops.Equal_Impl")
    def Equal(x : Optional[() => .Float] = .constant(1.0),
              y : Optional[() => .Float] = .constant(1.0)) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">"
    
    @python.intrinsic.observable("ops.Greater_Impl")
    def Greater(x : Optional[.IObservable[.Float]] = .const(1.0),
                y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">"
    
    @python.intrinsic.observable("ops.Greater_Impl")
    def Greater(x : Optional[() => .Float] = .constant(1.0),
                y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">"
    
    @python.intrinsic.observable("ops.Greater_Impl")
    def Greater(x : Optional[.IObservable[.Float]] = .const(1.0),
                y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = ">"
    
    @python.intrinsic.observable("ops.Greater_Impl")
    def Greater(x : Optional[() => .Float] = .constant(1.0),
                y : Optional[() => .Float] = .constant(1.0)) : () => .Boolean
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "or"
    
    @python.intrinsic.observable("ops.Or_Impl")
    def Or(x : Optional[.IObservable[.Boolean]] = .observableTrue(),
           y : Optional[.IObservable[.Boolean]] = .observableTrue()) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "or"
    
    @python.intrinsic.observable("ops.Or_Impl")
    def Or(x : Optional[() => .Boolean] = .true(),
           y : Optional[.IObservable[.Boolean]] = .observableTrue()) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "or"
    
    @python.intrinsic.observable("ops.Or_Impl")
    def Or(x : Optional[.IObservable[.Boolean]] = .observableTrue(),
           y : Optional[() => .Boolean] = .true()) : .IObservable[.Boolean]
    
    @label = "({%(x)s}{{symbol}}{%(y)s})"
    @symbol = "or"
    
    @python.intrinsic.observable("ops.Or_Impl")
    def Or(x : Optional[() => .Boolean] = .true(),
           y : Optional[() => .Boolean] = .true()) : () => .Boolean
}

@category = "Basic"

package math {
    package random {
        /** Gamma distribution
         *
         *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         *
         *  The probability distribution function is: ::
         *
         *               x ** (alpha - 1) * math.exp(-x / beta)
         *     pdf(x) =  --------------------------------------
         *                  math.gamma(alpha) * beta ** alpha
         */
        
        @python.random()
        def gammavariate(Alpha : Optional[.Float] = 1.0,
                         Beta : Optional[.Float] = 1.0) : () => .Float
        
        /** Normal distribution
         */
        
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu : Optional[.Float] = 0.0,
                          /** |sigma| is the standard deviation */ Sigma : Optional[.Float] = 1.0) : () => .Float
        
        /** Pareto distribution
         */
        
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha : Optional[.Float] = 1.0) : () => .Float
        
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        
        @python.random()
        def triangular(Low : Optional[.Float] = 0.0,
                       High : Optional[.Float] = 1.0,
                       Mode : Optional[.Float] = 0.5) : () => .Float
        
        /** Von Mises distribution
         */
        
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu : Optional[.Float] = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa : Optional[.Float] = 0.0) : () => .Float
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        
        @python.random()
        def uniform(Low : Optional[.Float] = -10.0,
                    High : Optional[.Float] = 10.0) : () => .Float
        
        /** Weibull distribution
         */
        
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha : Optional[.Float] = 1.0,
                           /** |beta| is the shape parameter  */ Beta : Optional[.Float] = 1.0) : () => .Float
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda : Optional[.Float] = 1.0) : () => .Float
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        
        @python.random()
        def lognormvariate(Mu : Optional[.Float] = 0.0,
                           Sigma : Optional[.Float] = 1.0) : () => .Float
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        
        @python.random()
        def betavariate(Alpha : Optional[.Float] = 1.0,
                        Beta : Optional[.Float] = 1.0) : () => .Float
    }
    
    type IStatDomain
    
    type Cumulative : IStatDomain
    @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
    
    type RSI
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
    
    type macd
    @label = "EW_{%(alpha)s}(%(source)s)"
    
    type EW : IStatDomain
    @label = "Moving_{%(timeframe)s}(%(source)s)"
    
    type Moving : IStatDomain
    @category = "-"
    @label = "Moving_{%(timeframe)s}(%(source)s)"
    
    @python.accessor()
    def Timeframe(x : Optional[.math.Moving] = .math.Moving()) : .Float
    
    @category = "-"
    @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
    
    @python.accessor()
    def Timeframe(x : Optional[.math.RSI] = .math.RSI()) : .Float
    
    /** Function returning minimum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "min{%(x)s, %(y)s}"
    
    @python.observable()
    def Min(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Less(x,y),x,y)
    
    /** Function returning minimum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "min{%(x)s, %(y)s}"
    
    @python.observable()
    def Min(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Less(x,y),x,y)
    
    /** Function returning minimum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "min{%(x)s, %(y)s}"
    
    @python.observable()
    def Min(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Less(x,y),x,y)
    
    /** Function returning minimum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "min{%(x)s, %(y)s}"
    
    @python.observable()
    def Min(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : () => .Float
        	 = .ops.Condition(.ops.Less(x,y),x,y)
    
    /** Moving average convergence/divergence histogram
     */
    @category = "MACD"
    @label = "Histogram^{%(timeframe)s}_{%(step)s}(%(x)s)"
    
    def Histogram(x : Optional[.math.macd] = .math.macd(),
                  /** signal period */ timeframe : Optional[.Float] = 9.0,
                  /** discretization step */ step : Optional[.Float] = 1.0) : () => .Float
        	 = .ops.Sub(.math.Value(x),.math.Signal(x,timeframe,step))
    
    /** Relative standard deviation
     */
    @category = "Statistics"
    
    def RelStdDev(x : Optional[.math.Cumulative] = .math.Cumulative()) : .IObservable[.Float]
        	 = .ops.Div(.ops.Sub(.math.Source(x),.math.Avg(x)),.math.StdDev(x))
    
    /** Relative standard deviation
     */
    @category = "Statistics"
    
    def RelStdDev(x : Optional[.math.EW] = .math.EW()) : .IObservable[.Float]
        	 = .ops.Div(.ops.Sub(.math.Source(x),.math.Avg(x)),.math.StdDev(x))
    
    /** Relative standard deviation
     */
    @category = "Statistics"
    
    def RelStdDev(x : Optional[.math.Moving] = .math.Moving()) : .IObservable[.Float]
        	 = .ops.Div(.ops.Sub(.math.Source(x),.math.Avg(x)),.math.StdDev(x))
    
    /** Cumulative variance
     */
    @category = "Statistics"
    
    @python.intrinsic("moments.cmv.Variance_Impl")
    def Var(x : Optional[.math.Cumulative] = .math.Cumulative()) : () => .Float
    
    /** Exponentially weighted moving variance
     */
    @category = "Statistics"
    
    @python.intrinsic("moments.ewmv.EWMV_Impl")
    def Var(x : Optional[.math.EW] = .math.EW()) : () => .Float
    
    /** Simple moving variance
     */
    @category = "Statistics"
    
    @python.intrinsic("moments.mv.MV_Impl")
    def Var(x : Optional[.math.Moving] = .math.Moving()) : () => .Float
    
    /** Moving average convergence/divergence signal
     */
    @category = "MACD"
    @label = "Signal^{%(timeframe)s}_{%(step)s}(%(x)s)"
    
    def Signal(x : Optional[.math.macd] = .math.macd(),
               /** signal period */ timeframe : Optional[.Float] = 9.0,
               /** discretization step */ step : Optional[.Float] = 1.0) : .IDifferentiable
        	 = .math.Avg(.math.EW(.observable.OnEveryDt(.math.Value(x),step),2/(timeframe+1)))
    
    /** Returns negative movements of some observable *source* with lag *timeframe*
     */
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    
    def DownMovements(/** observable data source */ source : Optional[.IObservable[.Float]] = .const(1.0),
                      /** lag size */ timeframe : Optional[.Float] = 10.0) : .IObservable[.Float]
        	 = .math.Max(.constant(0.0),.ops.Sub(.math.Lagged(source,timeframe),source))
    
    /** Arc tangent of x, in radians.
     *
     */
    @category = "Trigonometric"
    
    @python.mathops("atan")
    def Atan(x : Optional[() => .Float] = .constant(0.0)) : () => .Float
    
    @category = "-"
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
    
    @python.accessor()
    def Fast(x : Optional[.math.macd] = .math.macd()) : .Float
    
    /** Observable that adds a lag to an observable data source
     *  so Lagged(x, dt)(t0+dt) == x(t0)
     */
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    
    @python.intrinsic("observable.lagged.Lagged_Impl")
    def Lagged(/** observable data source */ source : Optional[.IObservable[.Float]] = .const(1.0),
               /** lag size */ timeframe : Optional[.Float] = 10.0) : .IObservable[.Float]
    
    /** Function returning maximum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "max{%(x)s, %(y)s}"
    
    @python.observable()
    def Max(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Greater(x,y),x,y)
    
    /** Function returning maximum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "max{%(x)s, %(y)s}"
    
    @python.observable()
    def Max(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Greater(x,y),x,y)
    
    /** Function returning maximum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "max{%(x)s, %(y)s}"
    
    @python.observable()
    def Max(x : Optional[.IObservable[.Float]] = .const(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Greater(x,y),x,y)
    
    /** Function returning maximum of two functions *x* and *y*.
     * If *x* or/and *y* are observables, *Min* is also observable
     */
    @label = "max{%(x)s, %(y)s}"
    
    @python.observable()
    def Max(x : Optional[() => .Float] = .constant(1.0),
            y : Optional[() => .Float] = .constant(1.0)) : () => .Float
        	 = .ops.Condition(.ops.Greater(x,y),x,y)
    
    @category = "RSI"
    
    def Value(x : Optional[.math.RSI] = .math.RSI()) : () => .Float
        	 = .ops.Sub(.constant(100.0),.ops.Div(.constant(100.0),.ops.Add(.constant(1.0),.math.Raw(x))))
    
    /** Moving average convergence/divergence
     */
    @category = "MACD"
    
    def Value(x : Optional[.math.macd] = .math.macd()) : () => .Float
        	 = .ops.Sub(.math.Avg(.math.EW(.math.Source(x),2.0/(.math.Fast(x)+1))),.math.Avg(.math.EW(.math.Source(x),2.0/(.math.Slow(x)+1))))
    
    /** Returns positive movements of some observable *source* with lag *timeframe*
     */
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    
    def UpMovements(/** observable data source */ source : Optional[.IObservable[.Float]] = .const(1.0),
                    /** lag size */ timeframe : Optional[.Float] = 10.0) : .IObservable[.Float]
        	 = .math.Max(.constant(0.0),.ops.Sub(source,.math.Lagged(source,timeframe)))
    
    /** Square of *x*
     */
    @category = "Log/Pow"
    @label = "{%(x)s}^2"
    
    @python.observable()
    def Sqr(x : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
        	 = .ops.Mul(x,x)
    
    /** Square of *x*
     */
    @category = "Log/Pow"
    @label = "{%(x)s}^2"
    
    @python.observable()
    def Sqr(x : Optional[() => .Float] = .constant(1.0)) : () => .Float
        	 = .ops.Mul(x,x)
    
    /** Log returns
     */
    @label = "LogReturns_{%(timeframe)s}(%(x)s)"
    
    def LogReturns(/** observable data source */ x : Optional[.IObservable[.Float]] = .const(1.0),
                   /** lag size */ timeframe : Optional[.Float] = 10.0) : () => .Float
        	 = .math.Log(.ops.Div(x,.math.Lagged(x,timeframe)))
    
    /** Cumulative average
     */
    @category = "Statistics"
    
    @python.intrinsic("moments.cma.CMA_Impl")
    def Avg(x : Optional[.math.Cumulative] = .math.Cumulative()) : .IDifferentiable
    
    /** Exponentially weighted moving average
     */
    @category = "Statistics"
    
    @python.intrinsic("moments.ewma.EWMA_Impl")
    def Avg(x : Optional[.math.EW] = .math.EW()) : .IDifferentiable
    
    /** Simple moving average
     */
    @category = "Statistics"
    
    @python.intrinsic("moments.ma.MA_Impl")
    def Avg(x : Optional[.math.Moving] = .math.Moving()) : .IDifferentiable
    
    @category = "-"
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
    
    @python.accessor()
    def Slow(x : Optional[.math.macd] = .math.macd()) : .Float
    
    /** Square root of *x*
     *
     */
    @category = "Log/Pow"
    @label = "\\sqrt{%(x)s}"
    
    @python.mathops("sqrt")
    def Sqrt(x : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @category = "-"
    
    @python.constructor()
    def Cumulative(source : Optional[.IObservable[.Float]] = .const(0.0)) : .math.Cumulative
    
    @category = "-"
    @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
    
    @python.constructor()
    def RSI(/** observable data source */ source : Optional[.IObservable[.Float]] = .const(1.0),
            /** lag size */ timeframe : Optional[.Float] = 10.0,
            /** alpha parameter for EWMA */ alpha : Optional[.Float] = 0.015) : .math.RSI
    
    /** Exponent of *x*
     *
     */
    @category = "Log/Pow"
    @label = "e^{%(x)s}"
    
    @python.mathops("exp")
    def Exp(x : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    /** Natural logarithm of *x* (to base e)
     *
     */
    @category = "Log/Pow"
    @label = "log(%(x)s)"
    
    @python.mathops("log")
    def Log(x : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @category = "-"
    @label = "Moving_{%(timeframe)s}(%(source)s)"
    
    @python.accessor()
    def Source(x : Optional[.math.Moving] = .math.Moving()) : .IObservable[.Float]
    
    @category = "-"
    @label = "EW_{%(alpha)s}(%(source)s)"
    
    @python.accessor()
    def Source(x : Optional[.math.EW] = .math.EW()) : .IObservable[.Float]
    
    @category = "-"
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
    
    @python.accessor()
    def Source(x : Optional[.math.macd] = .math.macd()) : .IObservable[.Float]
    
    @category = "-"
    @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
    
    @python.accessor()
    def Source(x : Optional[.math.RSI] = .math.RSI()) : .IObservable[.Float]
    
    @category = "-"
    
    @python.accessor()
    def Source(x : Optional[.math.Cumulative] = .math.Cumulative()) : .IObservable[.Float]
    
    /** A discrete signal with user-defined increments.
     */
    @label = "%(name)s"
    
    @python.intrinsic("observable.randomwalk.RandomWalk_Impl")
    def RandomWalk(/** initial value of the signal */ initialValue : Optional[.Float] = 0.0,
                   /** increment function */ deltaDistr : Optional[() => .Float] = .math.random.normalvariate(0.0,1.0),
                   /** intervals between signal updates */ intervalDistr : Optional[() => .Float] = .math.random.expovariate(1.0),
                   name : Optional[.String] = "-random-") : .IObservable[.Float]
    
    @category = "-"
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
    
    @python.constructor()
    def macd(/** source */ source : Optional[.IObservable[.Float]] = .const(1.0),
             /** long period */ slow : Optional[.Float] = 26.0,
             /** short period */ fast : Optional[.Float] = 12.0) : .math.macd
    
    /** Cumulative minimum of a function with positive tolerance.
     *
     *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
     */
    @category = "Statistics"
    @label = "Min_{\\epsilon}(%(x)s)"
    
    @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
    def MinEpsilon(x : Optional[.math.Cumulative] = .math.Cumulative(),
                   epsilon : Optional[() => .Float] = .constant(0.01)) : .IObservable[.Float]
    
    /** Cumulative maximum of a function with positive tolerance.
     *
     *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
     */
    @category = "Statistics"
    @label = "Max_{\\epsilon}(%(x)s)"
    
    @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
    def MaxEpsilon(x : Optional[.math.Cumulative] = .math.Cumulative(),
                   epsilon : Optional[() => .Float] = .constant(0.01)) : .IObservable[.Float]
    
    /** Standard deviation
     */
    @category = "Statistics"
    
    def StdDev(x : Optional[.math.Cumulative] = .math.Cumulative()) : () => .Float
        	 = .math.Sqrt(.math.Var(x))
    
    /** Standard deviation
     */
    @category = "Statistics"
    
    def StdDev(x : Optional[.math.EW] = .math.EW()) : () => .Float
        	 = .math.Sqrt(.math.Var(x))
    
    /** Standard deviation
     */
    @category = "Statistics"
    
    def StdDev(x : Optional[.math.Moving] = .math.Moving()) : () => .Float
        	 = .math.Sqrt(.math.Var(x))
    
    @category = "-"
    @label = "EW_{%(alpha)s}(%(source)s)"
    
    @python.constructor()
    def EW(source : Optional[.IObservable[.Float]] = .const(0.0),
           alpha : Optional[.Float] = 0.015) : .math.EW
    
    /** Running maximum of a function
     */
    @category = "Statistics"
    
    @python.intrinsic("observable.minmax.Max_Impl")
    def Maximum(x : Optional[.math.Moving] = .math.Moving()) : .IObservable[.Float]
    
    /** Function returning first derivative on time of *x*
     * *x* should provide *derivative* member
     */
    @label = "\\frac{d%(x)s}{dt}"
    
    @python.intrinsic("observable.derivative.Derivative_Impl")
    def Derivative(x : Optional[.IDifferentiable] = .math.Avg(.math.EW()) : .IDifferentiable) : () => .Float
    
    /** Absolute value for Relative Strength Index
     */
    @category = "RSI"
    
    def Raw(x : Optional[.math.RSI] = .math.RSI()) : () => .Float
        	 = .ops.Div(.math.Avg(.math.EW(.math.UpMovements(.math.Source(x),.math.Timeframe(x)),.math.Alpha(x))),.math.Avg(.math.EW(.math.DownMovements(.math.Source(x),.math.Timeframe(x)),.math.Alpha(x))))
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @category = "Log/Pow"
    @label = "%(base)s^{%(power)s}"
    
    @python.mathops("pow")
    def Pow(base : Optional[() => .Float] = .constant(1.0),
            power : Optional[() => .Float] = .constant(1.0)) : () => .Float
    
    @category = "-"
    @label = "EW_{%(alpha)s}(%(source)s)"
    
    @python.accessor()
    def Alpha(x : Optional[.math.EW] = .math.EW()) : .Float
    
    @category = "-"
    @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
    
    @python.accessor()
    def Alpha(x : Optional[.math.RSI] = .math.RSI()) : .Float
    
    @category = "-"
    @label = "Moving_{%(timeframe)s}(%(source)s)"
    
    @python.constructor()
    def Moving(source : Optional[.IObservable[.Float]] = .const(0.0),
               timeframe : Optional[.Float] = 100.0) : .math.Moving
    
    /** Running minimum of a function
     */
    @category = "Statistics"
    
    @python.intrinsic("observable.minmax.Min_Impl")
    def Minimum(x : Optional[.math.Moving] = .math.Moving()) : .IObservable[.Float]
}

@category = "Order"

package order {
    package side {
        package price {
            def Limit = .order._curried.side_price_Limit
            
            def ImmediateOrCancel = .order._curried.side_price_ImmediateOrCancel
            
            def StopLoss = .order._curried.side_price_StopLoss
            
            def WithExpiry = .order._curried.side_price_WithExpiry
            
            def FloatingPrice = .order._curried.side_price_FloatingPrice
            
            def Iceberg = .order._curried.side_price_Iceberg
            
            def Peg = .order._curried.side_price_Peg
        }
        
        def Limit = .order._curried.side_Limit
        
        def ImmediateOrCancel = .order._curried.side_ImmediateOrCancel
        
        def Market = .order._curried.side_Market
        
        def StopLoss = .order._curried.side_StopLoss
        
        def WithExpiry = .order._curried.side_WithExpiry
        
        def FloatingPrice = .order._curried.side_FloatingPrice
        
        def Iceberg = .order._curried.side_Iceberg
        
        def FixedBudget = .order._curried.side_FixedBudget
        
        def Peg = .order._curried.side_Peg
    }
    
    
    package side_price {
        def Limit = .order._curried.sideprice_Limit
        
        def ImmediateOrCancel = .order._curried.sideprice_ImmediateOrCancel
        
        def StopLoss = .order._curried.sideprice_StopLoss
        
        def WithExpiry = .order._curried.sideprice_WithExpiry
        
        def FloatingPrice = .order._curried.sideprice_FloatingPrice
        
        def Iceberg = .order._curried.sideprice_Iceberg
        
        def Peg = .order._curried.sideprice_Peg
    }
    
    
    package price {
        def Limit = .order._curried.price_Limit
        
        def ImmediateOrCancel = .order._curried.price_ImmediateOrCancel
        
        def StopLoss = .order._curried.price_StopLoss
        
        def WithExpiry = .order._curried.price_WithExpiry
        
        def FloatingPrice = .order._curried.price_FloatingPrice
        
        def Iceberg = .order._curried.price_Iceberg
        
        def Peg = .order._curried.price_Peg
    }
    
    
    package signed {
        def Limit = .order.LimitSigned
        
        def Market = .order.MarketSigned
    }
    
    
    package signedVolume {
        def LimitSigned = .order._curried.signedVolume_LimitSigned
        
        def MarketSigned = .order._curried.signedVolume_MarketSigned
    }
    
    
    package _curried {
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def side_ImmediateOrCancel(/** factory for underlying orders */ proto : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Limit()) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        
        @python.order.factory.on_proto("price_StopLoss")
        def side_price_StopLoss(/** underlying orders to create */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit(),
                                /** maximal acceptable loss factor */ maxloss : Optional[() => .Float] = .constant(0.1)) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
        
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        
        @python.order.factory.on_proto("Iceberg")
        def price_Iceberg(/** underlying orders to create */ proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit(),
                          /** maximal size of order to send */ lotSize : Optional[() => .Float] = .constant(10.0)) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        
        @python.order.factory.on_proto("FloatingPrice")
        def sideprice_FloatingPrice(/** underlying orders to create */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit(),
                                    /** observable defining price of orders to create */ floatingPrice : Optional[.IObservable[.Float]] = .const(10.0)) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        
        @python.order.factory.on_proto("StopLoss")
        def price_StopLoss(/** underlying orders to create */ proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit(),
                           /** maximal acceptable loss factor */ maxloss : Optional[() => .Float] = .constant(0.1)) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def price_ImmediateOrCancel(/** factory for underlying orders */ proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit()) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        
        @python.order.factory.on_proto("StopLoss")
        def sideprice_StopLoss(/** underlying orders to create */ proto : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                               /** maximal acceptable loss factor */ maxloss : Optional[() => .Float] = .constant(0.1)) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        
        @python.order.factory.on_proto("Iceberg")
        def side_Iceberg(/** underlying orders to create */ proto : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Limit(),
                         /** maximal size of order to send */ lotSize : Optional[() => .Float] = .constant(10.0)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating fixed budget orders
         *
         *  Fixed budget order acts like a market order
         *  but the volume is implicitly given by a budget available for trades.
         *  Internally first it sends request.EvalVolumesForBudget
         *  to estimate volumes and prices of orders to sent and
         *  then sends a sequence of order.ImmediateOrCancel to be sure that
         *  cumulative price of trades to be done won't exceed the given budget.
         */
        
        @python.order.factory.curried("FixedBudget")
        def side_FixedBudget(/** function defining budget on which it may send orders at one time */ budget : Optional[() => .Float] = .constant(1000.0)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        
        @python.order.factory.curried("Limit")
        def sideprice_Limit(/** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        
        @python.order.factory.on_proto("Peg")
        def sideprice_Peg(proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit()) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        
        @python.order.factory.on_proto("Peg")
        def side_Peg(proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit()) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        
        @python.order.factory.curried("LimitSigned")
        def signedVolume_LimitSigned(/** function defining price of orders to create */ price : Optional[() => .Float] = .constant(100.0)) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        
        @python.order.factory.on_proto("price_Iceberg")
        def side_price_Iceberg(/** underlying orders to create */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit(),
                               /** maximal size of order to send */ lotSize : Optional[() => .Float] = .constant(10.0)) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
        
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        
        @python.order.factory.on_proto("price_ImmediateOrCancel")
        def side_price_ImmediateOrCancel(/** factory for underlying orders */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
        
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        
        @python.order.factory.on_proto("WithExpiry")
        def side_WithExpiry(/** underlying orders to create */ proto : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Limit(),
                            /** expiration period for orders */ expiry : Optional[() => .Float] = .constant(10.0)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating StopLoss orders
         *
         *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
         *  It keeps track of position and balance change induced by trades of the underlying order and
         *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
         *  the meta order clears its position.
         */
        
        @python.order.factory.on_proto("StopLoss")
        def side_StopLoss(/** underlying orders to create */ proto : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Limit(),
                          /** maximal acceptable loss factor */ maxloss : Optional[() => .Float] = .constant(0.1)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        
        @python.order.factory.on_proto("Peg")
        def price_Peg(proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit()) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        
        @python.order.factory.on_proto("WithExpiry")
        def sideprice_WithExpiry(/** underlying orders to create */ proto : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                                 /** expiration period for orders */ expiry : Optional[() => .Float] = .constant(10.0)) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        
        @python.order.factory.curried("Limit")
        def side_Limit(/** function defining price of orders to create */ price : Optional[() => .Float] = .constant(100.0),
                       /** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        
        @python.order.factory.on_proto("price_FloatingPrice")
        def side_price_FloatingPrice(/** underlying orders to create */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit(),
                                     /** observable defining price of orders to create */ floatingPrice : Optional[.IObservable[.Float]] = .const(10.0)) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
        
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        
        @python.order.factory.on_proto("FloatingPrice")
        def side_FloatingPrice(/** underlying orders to create */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit(),
                               /** observable defining price of orders to create */ floatingPrice : Optional[.IObservable[.Float]] = .const(10.0)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        
        @python.order.factory.on_proto("price_WithExpiry")
        def side_price_WithExpiry(/** underlying orders to create */ proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit(),
                                  /** expiration period for orders */ expiry : Optional[() => .Float] = .constant(10.0)) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
        
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        
        @python.order.factory.curried("price_Limit")
        def side_price_Limit(/** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
        
        /** Factory creating market orders
         *
         *  Market order intructs buy or sell given volume immediately
         */
        
        @python.order.factory.curried("Market")
        def side_Market(/** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : (() => .Side) => .IObservable[.IOrder]
        
        /** Factory creating orders with floating price
         *
         *  Floating price order is initialized by an order having a price and an observable that generates new prices.
         *  When the observable value changes the order is cancelled and
         *  a new order with new price is created and sent to the order book.
         */
        
        @python.order.factory.on_proto("FloatingPrice")
        def price_FloatingPrice(/** underlying orders to create */ proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit(),
                                /** observable defining price of orders to create */ floatingPrice : Optional[.IObservable[.Float]] = .const(10.0)) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating WithExpiry orders
         *
         * WithExpiry orders can be viewed as ImmediateOrCancel orders
         * where cancel order is sent not immediately but after some delay
         */
        
        @python.order.factory.on_proto("WithExpiry")
        def price_WithExpiry(/** underlying orders to create */ proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit(),
                             /** expiration period for orders */ expiry : Optional[() => .Float] = .constant(10.0)) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating limit orders
         *
         *  Limit orders ask to buy or sell some asset at price better than some limit price.
         *  If a limit order is not competely fulfilled
         *  it remains in an order book waiting to be matched with another order.
         */
        
        @python.order.factory.curried("Limit")
        def price_Limit(/** function defining side of orders to create */ side : Optional[() => .Side] = .side.Sell(),
                        /** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating iceberg orders
         *
         *  Iceberg order is initialized by an underlying order and a lot size.
         *  It sends consequently pieces of the underlying order of size equal or less to the lot size
         *  thus maximum lot size volume is visible at the market at any moment.
         */
        
        @python.order.factory.on_proto("Iceberg")
        def sideprice_Iceberg(/** underlying orders to create */ proto : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                              /** maximal size of order to send */ lotSize : Optional[() => .Float] = .constant(10.0)) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating market orders
         *
         *  Market order intructs buy or sell given volume immediately
         */
        
        @python.order.factory.curried("MarketSigned")
        def signedVolume_MarketSigned() : (() => .Float) => .IObservable[.IOrder]
        
        /** Factory creating Immediate-Or-Cancel orders
         *
         *  Immediate-Or-Cancel order sends an underlying order to the market and
         *  immediately sends a cancel request for it.
         *  It allows to combine market and limit order behaviour:
         *  the order is either executed immediately
         *  at price equal or better than given one
         *  either it is cancelled (and consequently never stored in the order queue).
         */
        
        @python.order.factory.on_proto("ImmediateOrCancel")
        def sideprice_ImmediateOrCancel(/** factory for underlying orders */ proto : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit()) : ((() => .Side),(() => .Float)) => .IObservable[.IOrder]
        
        /** Factory creating Peg orders
         *
         *  A peg order is a particular case of the floating price order
         *  with the price better at one tick than the best price of the order queue.
         *  It implies that if several peg orders are sent to the same order queue
         *  they start to race until being matched against the counterparty orders.
         */
        
        @python.order.factory.on_proto("price_Peg")
        def side_price_Peg(proto : Optional[(() => .Side) => ((() => .Float) => .IObservable[.IOrder])] = .order._curried.side_price_Limit()) : (() => .Side) => ((() => .Float) => .IObservable[.IOrder])
    }
    
    /** Factory creating limit orders
     *
     *  Limit orders ask to buy or sell some asset at price better than some limit price.
     *  If a limit order is not competely fulfilled
     *  it remains in an order book waiting to be matched with another order.
     */
    
    @python.order.factory("order.limit.Order_Impl")
    def Limit(/** function defining side of orders to create */ side : Optional[() => .Side] = .side.Sell(),
              /** function defining price of orders to create */ price : Optional[() => .Float] = .constant(100.0),
              /** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : .IObservable[.IOrder]
    
    /** Factory creating market orders
     *
     *  Market order intructs buy or sell given volume immediately
     */
    
    @python.order.factory("order.market.Order_Impl")
    def MarketSigned(/**signed volume*/ signedVolume : () => .Float = .constant(1.0)) : .IObservable[.IOrder]
    
    /** Factory creating Immediate-Or-Cancel orders
     *
     *  Immediate-Or-Cancel order sends an underlying order to the market and
     *  immediately sends a cancel request for it.
     *  It allows to combine market and limit order behaviour:
     *  the order is either executed immediately
     *  at price equal or better than given one
     *  either it is cancelled (and consequently never stored in the order queue).
     */
    
    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(/** factory for underlying orders */ proto : Optional[.IObservable[.IOrder]] = .order.Limit()) : .IObservable[.IOrder]
    
    /** Factory creating market orders
     *
     *  Market order intructs buy or sell given volume immediately
     */
    
    @python.order.factory("order.market.Order_Impl")
    def Market(/** function defining side of orders to create */ side : Optional[() => .Side] = .side.Sell(),
               /** function defining volume of orders to create */ volume : Optional[() => .Float] = .constant(1.0)) : .IObservable[.IOrder]
    
    /** Factory creating StopLoss orders
     *
     *  StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
     *  It keeps track of position and balance change induced by trades of the underlying order and
     *  if losses from keeping the position exceed certain limit (given by maximum loss factor),
     *  the meta order clears its position.
     */
    
    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(/** underlying orders to create */ proto : Optional[.IObservable[.IOrder]] = .order.Limit(),
                 /** maximal acceptable loss factor */ maxloss : Optional[() => .Float] = .constant(0.1)) : .IObservable[.IOrder]
    
    /** Factory creating WithExpiry orders
     *
     * WithExpiry orders can be viewed as ImmediateOrCancel orders
     * where cancel order is sent not immediately but after some delay
     */
    
    @python.order.factory("order.meta.with_expiry.Order_Impl")
    def WithExpiry(/** underlying orders to create */ proto : Optional[.IObservable[.IOrder]] = .order.Limit(),
                   /** expiration period for orders */ expiry : Optional[() => .Float] = .constant(10.0)) : .IObservable[.IOrder]
    
    /** Factory creating orders with floating price
     *
     *  Floating price order is initialized by an order having a price and an observable that generates new prices.
     *  When the observable value changes the order is cancelled and
     *  a new order with new price is created and sent to the order book.
     */
    
    @python.order.factory("order.meta.floating_price.Factory_Impl")
    def FloatingPrice(/** underlying orders to create */ proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit(),
                      /** observable defining price of orders to create */ floatingPrice : Optional[.IObservable[.Float]] = .const(10.0)) : .IObservable[.IOrder]
    
    /** Factory creating iceberg orders
     *
     *  Iceberg order is initialized by an underlying order and a lot size.
     *  It sends consequently pieces of the underlying order of size equal or less to the lot size
     *  thus maximum lot size volume is visible at the market at any moment.
     */
    
    @python.order.factory("order.meta.iceberg.Order_Impl")
    def Iceberg(/** underlying orders to create */ proto : Optional[.IObservable[.IOrder]] = .order.Limit(),
                /** maximal size of order to send */ lotSize : Optional[() => .Float] = .constant(10.0)) : .IObservable[.IOrder]
    
    /** Factory creating fixed budget orders
     *
     *  Fixed budget order acts like a market order
     *  but the volume is implicitly given by a budget available for trades.
     *  Internally first it sends request.EvalVolumesForBudget
     *  to estimate volumes and prices of orders to sent and
     *  then sends a sequence of order.ImmediateOrCancel to be sure that
     *  cumulative price of trades to be done won't exceed the given budget.
     */
    
    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(/** function defining side of orders to create */ side : Optional[() => .Side] = .side.Sell(),
                    /** function defining budget on which it may send orders at one time */ budget : Optional[() => .Float] = .constant(1000.0)) : .IObservable[.IOrder]
    
    /** Factory creating limit orders
     *
     *  Limit orders ask to buy or sell some asset at price better than some limit price.
     *  If a limit order is not competely fulfilled
     *  it remains in an order book waiting to be matched with another order.
     */
    
    @python.order.factory("order.limit.Order_Impl")
    def LimitSigned(/**signed volume*/ signedVolume : () => .Float = .constant(1.0),
                    /** function defining price of orders to create */ price : Optional[() => .Float] = .constant(100.0)) : .IObservable[.IOrder]
    
    /** Factory creating Peg orders
     *
     *  A peg order is a particular case of the floating price order
     *  with the price better at one tick than the best price of the order queue.
     *  It implies that if several peg orders are sent to the same order queue
     *  they start to race until being matched against the counterparty orders.
     */
    
    @python.order.factory("order.meta.peg.Factory_Impl")
    def Peg(proto : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.price_Limit()) : .IObservable[.IOrder]
}

@category = "Strategy"

package strategy {@category = "Side function"
    
    package side {
        type PairTrading : FundamentalValueStrategy
        
        type Signal : SignalStrategy
        
        type CrossingAverages : SignalStrategy
        
        type SideStrategy
        
        type TrendFollower : SignalStrategy
        
        type FundamentalValue : FundamentalValueStrategy
        
        type RSIbis : SignalStrategy
        
        type FundamentalValueStrategy : SideStrategy
        
        type MeanReversion : FundamentalValueStrategy
        
        type SignalStrategy : SideStrategy
        
        type Noise : SideStrategy
        @category = "-"
        
        @python.accessor()
        def Timeframe(x : Optional[.strategy.side.RSIbis] = .strategy.side.RSIbis()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Threshold(x : Optional[.strategy.side.RSIbis] = .strategy.side.RSIbis()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Threshold(x : Optional[.strategy.side.TrendFollower] = .strategy.side.TrendFollower()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Threshold(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Threshold(x : Optional[.strategy.side.Signal] = .strategy.side.Signal()) : .Float
        
        
        def Fundamental_Value(x : Optional[.strategy.side.MeanReversion] = .strategy.side.MeanReversion()) : .IDifferentiable
            	 = .math.Avg(.math.EW(.orderbook.MidPrice(.strategy.side.book(x)),.strategy.side.Alpha(x)))
        
        
        def Fundamental_Value(x : Optional[.strategy.side.FundamentalValue] = .strategy.side.FundamentalValue()) : () => .Float
            	 = .strategy.side.Fv(x)
        
        
        def Fundamental_Value(x : Optional[.strategy.side.PairTrading] = .strategy.side.PairTrading()) : .IObservable[.Float]
            	 = .ops.Mul(.orderbook.MidPrice(.strategy.side.BookToDependOn(x)),.constant(.strategy.side.Factor(x)))
        
        @category = "-"
        
        @python.accessor()
        def Side_distribution(x : Optional[.strategy.side.Noise] = .strategy.side.Noise()) : () => .Float
        
        @category = "-"
        
        @python.constructor()
        def PairTrading(/** reference to order book for another asset
                          * used to evaluate fair price of our asset */ bookToDependOn : Optional[.IOrderBook] = .orderbook.OfTrader(),
                        /** multiplier to obtain fair asset price from the reference asset price */ factor : Optional[.Float] = 1.0) : .strategy.side.PairTrading
        
        @category = "-"
        
        @python.constructor()
        def Signal(/** signal to be listened to */ source : Optional[() => .Float] = .constant(0.0),
                   /** threshold when the trader starts to act */ threshold : Optional[.Float] = 0.7) : .strategy.side.Signal
        
        @category = "-"
        
        @python.constructor()
        def CrossingAverages(/** parameter |alpha| for exponentially weighted moving average 1 */ alpha_1 : Optional[.Float] = 0.15,
                             /** parameter |alpha| for exponentially weighted moving average 2 */ alpha_2 : Optional[.Float] = 0.015,
                             /** threshold when the trader starts to act */ threshold : Optional[.Float] = 0.0,
                             /** asset in question */ book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .strategy.side.CrossingAverages
        
        
        def book(x : Optional[.strategy.side.MeanReversion] = .strategy.side.MeanReversion()) : .IOrderBook
            	 = .orderbook.OfTrader()
        
        
        def book(x : Optional[.strategy.side.FundamentalValue] = .strategy.side.FundamentalValue()) : .IOrderBook
            	 = .orderbook.OfTrader()
        
        
        def book(x : Optional[.strategy.side.PairTrading] = .strategy.side.PairTrading()) : .IOrderBook
            	 = .orderbook.OfTrader()
        
        @category = "-"
        
        @python.constructor()
        def TrendFollower(/** parameter |alpha| for exponentially weighted moving average */ alpha : Optional[.Float] = 0.15,
                          /** threshold when the trader starts to act */ threshold : Optional[.Float] = 0.0,
                          /** asset in question */ book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .strategy.side.TrendFollower
        
        
        def Side(x : Optional[.strategy.side.Noise] = .strategy.side.Noise()) : () => .Side
            	 = .ops.Condition(.ops.Greater(.strategy.side.Side_distribution(x),.constant(0.5)),.side.Buy(),.side.Sell())
        
        
        def Side(x : Optional[.strategy.side.MeanReversion] = .strategy.side.MeanReversion()) : .IObservable[.Side]
            	 = .ops.Condition(.ops.Greater(.orderbook.BestPrice(.orderbook.Bids(.strategy.side.book(x))),.strategy.side.Fundamental_Value(x)),.side.Sell(),.ops.Condition(.ops.Less(.orderbook.BestPrice(.orderbook.Asks(.strategy.side.book(x))),.strategy.side.Fundamental_Value(x)),.side.Buy(),.side.Nothing()))
        
        
        def Side(x : Optional[.strategy.side.RSIbis] = .strategy.side.RSIbis()) : () => .Side
            	 = .ops.Condition(.ops.Greater(.strategy.side.Signal_Value(x),.constant(.strategy.side.Threshold(x))),.side.Buy(),.ops.Condition(.ops.Less(.strategy.side.Signal_Value(x),.constant(0-.strategy.side.Threshold(x))),.side.Sell(),.side.Nothing()))
        
        
        def Side(x : Optional[.strategy.side.FundamentalValue] = .strategy.side.FundamentalValue()) : .IObservable[.Side]
            	 = .ops.Condition(.ops.Greater(.orderbook.BestPrice(.orderbook.Bids(.strategy.side.book(x))),.strategy.side.Fundamental_Value(x)),.side.Sell(),.ops.Condition(.ops.Less(.orderbook.BestPrice(.orderbook.Asks(.strategy.side.book(x))),.strategy.side.Fundamental_Value(x)),.side.Buy(),.side.Nothing()))
        
        
        def Side(x : Optional[.strategy.side.TrendFollower] = .strategy.side.TrendFollower()) : () => .Side
            	 = .ops.Condition(.ops.Greater(.strategy.side.Signal_Value(x),.constant(.strategy.side.Threshold(x))),.side.Buy(),.ops.Condition(.ops.Less(.strategy.side.Signal_Value(x),.constant(0-.strategy.side.Threshold(x))),.side.Sell(),.side.Nothing()))
        
        
        def Side(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages()) : () => .Side
            	 = .ops.Condition(.ops.Greater(.strategy.side.Signal_Value(x),.constant(.strategy.side.Threshold(x))),.side.Buy(),.ops.Condition(.ops.Less(.strategy.side.Signal_Value(x),.constant(0-.strategy.side.Threshold(x))),.side.Sell(),.side.Nothing()))
        
        
        def Side(x : Optional[.strategy.side.Signal] = .strategy.side.Signal()) : () => .Side
            	 = .ops.Condition(.ops.Greater(.strategy.side.Signal_Value(x),.constant(.strategy.side.Threshold(x))),.side.Buy(),.ops.Condition(.ops.Less(.strategy.side.Signal_Value(x),.constant(0-.strategy.side.Threshold(x))),.side.Sell(),.side.Nothing()))
        
        
        def Side(x : Optional[.strategy.side.PairTrading] = .strategy.side.PairTrading()) : .IObservable[.Side]
            	 = .ops.Condition(.ops.Greater(.orderbook.BestPrice(.orderbook.Bids(.strategy.side.book(x))),.strategy.side.Fundamental_Value(x)),.side.Sell(),.ops.Condition(.ops.Less(.orderbook.BestPrice(.orderbook.Asks(.strategy.side.book(x))),.strategy.side.Fundamental_Value(x)),.side.Buy(),.side.Nothing()))
        
        @category = "-"
        
        @python.constructor()
        def FundamentalValue(/** observable fundamental value */ fv : Optional[() => .Float] = .constant(200.0)) : .strategy.side.FundamentalValue
        
        @category = "-"
        
        @python.constructor()
        def RSIbis(/** parameter |alpha| for exponentially weighted moving average when calculating RSI */ alpha : Optional[.Float] = 1.0/14,
                   /** lag for calculating up and down movements for RSI */ timeframe : Optional[.Float] = 1.0,
                   /** strategy starts to act once RSI is out of [50-threshold, 50+threshold] */ threshold : Optional[.Float] = 30.0) : .strategy.side.RSIbis
        
        @category = "-"
        
        @python.accessor()
        def Factor(x : Optional[.strategy.side.PairTrading] = .strategy.side.PairTrading()) : .Float
        
        
        def Strategy(x : Optional[.strategy.side.Noise] = .strategy.side.Noise(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.MeanReversion] = .strategy.side.MeanReversion(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.RSIbis] = .strategy.side.RSIbis(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.FundamentalValue] = .strategy.side.FundamentalValue(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.TrendFollower] = .strategy.side.TrendFollower(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.Signal] = .strategy.side.Signal(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        
        def Strategy(x : Optional[.strategy.side.PairTrading] = .strategy.side.PairTrading(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[(() => .Side) => .IObservable[.IOrder]] = .order._curried.side_Market()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.side.Side(x)),eventGen)
        
        @category = "-"
        
        @python.accessor()
        def Book(x : Optional[.strategy.side.TrendFollower] = .strategy.side.TrendFollower()) : .IOrderBook
        
        @category = "-"
        
        @python.accessor()
        def Book(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages()) : .IOrderBook
        
        @category = "-"
        
        @python.accessor()
        def BookToDependOn(x : Optional[.strategy.side.PairTrading] = .strategy.side.PairTrading()) : .IOrderBook
        
        @category = "-"
        
        @python.constructor()
        def MeanReversion(/** parameter |alpha| for exponentially weighted moving average */ alpha : Optional[.Float] = 0.15) : .strategy.side.MeanReversion
        
        @category = "-"
        
        @python.accessor()
        def Alpha_2(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Source(x : Optional[.strategy.side.Signal] = .strategy.side.Signal()) : () => .Float
        
        @category = "-"
        
        @python.accessor()
        def Fv(x : Optional[.strategy.side.FundamentalValue] = .strategy.side.FundamentalValue()) : () => .Float
        
        
        def Signal_Value(x : Optional[.strategy.side.RSIbis] = .strategy.side.RSIbis()) : () => .Float
            	 = .ops.Sub(.constant(50.0),.math.Value(.math.RSI(.orderbook.MidPrice(.orderbook.OfTrader()),.strategy.side.Timeframe(x),.strategy.side.Alpha(x))))
        
        
        def Signal_Value(x : Optional[.strategy.side.TrendFollower] = .strategy.side.TrendFollower()) : () => .Float
            	 = .math.Derivative(.math.Avg(.math.EW(.orderbook.MidPrice(.strategy.side.Book(x)),.strategy.side.Alpha(x))))
        
        
        def Signal_Value(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages()) : () => .Float
            	 = .ops.Sub(.math.Avg(.math.EW(.orderbook.MidPrice(.strategy.side.Book(x)),.strategy.side.Alpha_1(x))),.math.Avg(.math.EW(.orderbook.MidPrice(.strategy.side.Book(x)),.strategy.side.Alpha_2(x))))
        
        
        def Signal_Value(x : Optional[.strategy.side.Signal] = .strategy.side.Signal()) : () => .Float
            	 = .strategy.side.Source(x)
        
        @category = "-"
        
        @python.accessor()
        def Alpha_1(x : Optional[.strategy.side.CrossingAverages] = .strategy.side.CrossingAverages()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Alpha(x : Optional[.strategy.side.MeanReversion] = .strategy.side.MeanReversion()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Alpha(x : Optional[.strategy.side.RSIbis] = .strategy.side.RSIbis()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Alpha(x : Optional[.strategy.side.TrendFollower] = .strategy.side.TrendFollower()) : .Float
        
        @category = "-"
        
        @python.constructor()
        def Noise(side_distribution : Optional[() => .Float] = .math.random.uniform(0.0,1.0)) : .strategy.side.Noise
    }
    
    
    package weight {
        package array {
            /** Identity function for an array of floats
             */
            
            @python.curried("IdentityL")
            def array_IdentityL() : Optional[List[.Float]] => (() => List[.Float])
            
            /** Function returning an array of length *len(array)*
             *  having 1 at the index of the maximal element and 0 are at the rest
             */
            
            @python.curried("ChooseTheBest")
            def array_ChooseTheBest() : Optional[List[.Float]] => (() => List[.Float])
        }
        
        
        package trader {
            /** Returns first derivative of a moving average of the trader efficiency
             */
            
            @python.curried("TraderEfficiencyTrend")
            def trader_TraderEfficiencyTrend(/** parameter alpha for the moving average */ alpha : Optional[.Float] = 0.15) : .IAccount => (() => .Float)
            
            /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
             */
            
            @python.curried("TraderEfficiency")
            def trader_TraderEfficiency() : .IAccount => (() => .Float)
            
            /** Calculates how many times efficiency of trader went up and went down
             * Returns difference between them.
             *
             * TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
             */
            
            @python.curried("Score")
            def trader_Score() : .IAccount => (() => .Float)
            
            /** Unit function. Used to simulate uniform random choice of a strategy
             */
            
            @python.curried("Unit")
            def trader_Unit() : .IAccount => (() => .Float)
        }
        
        
        package f {
            /** scaling function = atan(base^f(x))
             */
            
            @python.curried("AtanPow")
            def f_AtanPow(/** base for power function */ base : Optional[.Float] = 1.002) : Optional[() => .Float] => (() => .Float)
            
            /** scaling function = max(0, f(x)) + 1
             */
            
            @python.curried("Clamp0")
            def f_Clamp0() : Optional[() => .Float] => (() => .Float)
            
            /** identity scaling = f(x)
             */
            
            @python.curried("IdentityF")
            def f_IdentityF() : Optional[() => .Float] => (() => .Float)
        }
        
        def efficiency = .strategy.weight.trader.trader_TraderEfficiency
        
        /** Function returning an array of length *len(array)*
         *  having 1 at the index of the maximal element and 0 are at the rest
         */
        
        @python.intrinsic("strategy.weight.ChooseTheBest_Impl")
        @curried("array")
        def ChooseTheBest(array : Optional[List[.Float]] = []) : () => List[.Float]
        
        def chooseTheBest = .strategy.weight.array.array_ChooseTheBest
        
        def score = .strategy.weight.trader.trader_Score
        
        def identityL = .strategy.weight.array.array_IdentityL
        
        def efficiencyTrend = .strategy.weight.trader.trader_TraderEfficiencyTrend
        
        def clamp0 = .strategy.weight.f.f_Clamp0
        
        /** Calculates how many times efficiency of trader went up and went down
         * Returns difference between them.
         *
         * TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
         */
        
        @python.intrinsic("strategy.weight.Score_Impl")
        @curried("trader")
        def Score(/** account in question */ trader : .IAccount = .trader.SingleProxy()) : () => .Float
        
        /** scaling function = max(0, f(x)) + 1
         */
        
        @curried("f")
        def Clamp0(/** function to scale */ f : Optional[() => .Float] = .constant(1.0)) : () => .Float
            	 = .ops.Add(.math.Max(.constant(0),f),.constant(1))
        
        def identityF = .strategy.weight.f.f_IdentityF
        
        def atanPow = .strategy.weight.f.f_AtanPow
        
        def unit = .strategy.weight.trader.trader_Unit
        
        /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
         */
        
        @curried("trader")
        def TraderEfficiency(/** account in question */ trader : .IAccount = .trader.SingleProxy()) : () => .Float
            	 = .trader.Efficiency(trader)
        
        /** Unit function. Used to simulate uniform random choice of a strategy
         */
        
        @curried("trader")
        def Unit(/** account in question */ trader : .IAccount = .trader.SingleProxy()) : () => .Float
            	 = .constant(1.0)
        
        /** scaling function = atan(base^f(x))
         */
        
        @curried("f")
        def AtanPow(/** function to scale */ f : Optional[() => .Float] = .constant(1.0),
                    /** base for power function */ base : Optional[.Float] = 1.002) : () => .Float
            	 = .math.Atan(.math.Pow(.const(base),f))
        
        /** Identity function for an array of floats
         */
        
        @python.intrinsic("strategy.weight.Identity_Impl")
        @curried("array")
        def IdentityL(array : Optional[List[.Float]] = []) : () => List[.Float]
        
        /** identity scaling = f(x)
         */
        
        @curried("f")
        def IdentityF(f : Optional[() => .Float] = .constant(1.0)) : () => .Float
            	 = f
        
        /** Returns first derivative of a moving average of the trader efficiency
         */
        
        @curried("trader")
        def TraderEfficiencyTrend(/** account in question */ trader : .IAccount = .trader.SingleProxy(),
                                  /** parameter alpha for the moving average */ alpha : Optional[.Float] = 0.15) : () => .Float
            	 = .trader.EfficiencyTrend(trader,alpha)
    }
    
    @category = "Price function"
    
    package price {
        type LiquidityProvider
        
        type MarketData
        
        type MarketMaker
        @category = "-"
        
        @python.accessor()
        def PriceDistr(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider()) : () => .Float
        
        @category = "-"
        
        @python.accessor()
        def Delta(x : Optional[.strategy.price.MarketMaker] = .strategy.price.MarketMaker()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Delta(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Volume(x : Optional[.strategy.price.MarketMaker] = .strategy.price.MarketMaker()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Volume(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData()) : .Float
        
        
        def TwoSides(x : Optional[.strategy.price.MarketMaker] = .strategy.price.MarketMaker()) : .ISingleAssetStrategy
            	 = .strategy.Combine(.strategy.price.OneSide(x,.side.Sell(),1.0),.strategy.price.OneSide(x,.side.Buy(),-1.0))
        
        
        def TwoSides(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData()) : .ISingleAssetStrategy
            	 = .strategy.Combine(.strategy.price.OneSide(x,.side.Sell(),1.0),.strategy.price.OneSide(x,.side.Buy(),-1.0))
        
        @category = "-"
        
        @python.constructor()
        def LiquidityProvider(/** initial price which is taken if orderBook is empty */ initialValue : Optional[.Float] = 100.0,
                              /** defines multipliers for current asset price when price of
                                *             order to create is calculated*/ priceDistr : Optional[() => .Float] = .math.random.lognormvariate(0.0,0.1),
                              /** asset in question */ book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .strategy.price.LiquidityProvider
        
        
        @python.intrinsic("strategy.ladder.OneSide_Impl")
        def Ladder(orderFactory : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                   initialSize : Optional[.Int] = 10,
                   side : Optional[() => .Side] = .side.Sell()) : .ISingleAssetStrategy
        
        
        def OneSide(x : Optional[.strategy.price.MarketMaker] = .strategy.price.MarketMaker(),
                    side : Optional[.IObservable[.Side]] = .side.observableSell(),
                    sign : Optional[.Float] = 1.0) : .ISingleAssetStrategy
            	 = .strategy.Generic(.order.Iceberg(.order.FloatingPrice(.order._curried.price_Limit(side,.constant(.strategy.price.Volume(x)*1000)),.observable.BreaksAtChanges(.observable.OnEveryDt(.ops.Div(.orderbook.SafeSidePrice(.orderbook.Queue(.orderbook.OfTrader(),side),.constant(100+.strategy.price.Delta(x)*sign)),.math.Exp(.ops.Div(.math.Atan(.trader.Position()),.constant(1000)))),0.9))),.constant(.strategy.price.Volume(x))),.event.After(.constant(0.0)))
        
        
        def OneSide(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData(),
                    side : Optional[.IObservable[.Side]] = .side.observableSell(),
                    sign : Optional[.Float] = 1.0) : .ISingleAssetStrategy
            	 = .strategy.Generic(.order.Iceberg(.order.FloatingPrice(.order._curried.price_Limit(side,.constant(.strategy.price.Volume(x)*1000)),.observable.BreaksAtChanges(.ops.Add(.observable.Quote(.strategy.price.Ticker(x),.strategy.price.Start(x),.strategy.price.End(x)),.constant(.strategy.price.Delta(x)*sign)))),.constant(.strategy.price.Volume(x))),.event.After(.constant(0.0)))
        
        
        def OneSide(x : Optional[.strategy.price.MarketMaker] = .strategy.price.MarketMaker(),
                    side : Optional[() => .Side] = .side.Sell(),
                    sign : Optional[.Float] = 1.0) : .ISingleAssetStrategy
            	 = .strategy.Generic(.order.Iceberg(.order.FloatingPrice(.order._curried.price_Limit(side,.constant(.strategy.price.Volume(x)*1000)),.observable.BreaksAtChanges(.observable.OnEveryDt(.ops.Div(.orderbook.SafeSidePrice(.orderbook.Queue(.orderbook.OfTrader(),side),.constant(100+.strategy.price.Delta(x)*sign)),.math.Exp(.ops.Div(.math.Atan(.trader.Position()),.constant(1000)))),0.9))),.constant(.strategy.price.Volume(x))),.event.After(.constant(0.0)))
        
        
        def OneSide(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData(),
                    side : Optional[() => .Side] = .side.Sell(),
                    sign : Optional[.Float] = 1.0) : .ISingleAssetStrategy
            	 = .strategy.Generic(.order.Iceberg(.order.FloatingPrice(.order._curried.price_Limit(side,.constant(.strategy.price.Volume(x)*1000)),.observable.BreaksAtChanges(.ops.Add(.observable.Quote(.strategy.price.Ticker(x),.strategy.price.Start(x),.strategy.price.End(x)),.constant(.strategy.price.Delta(x)*sign)))),.constant(.strategy.price.Volume(x))),.event.After(.constant(0.0)))
        
        
        def Price(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider(),
                  side : Optional[() => .Side] = .side.Sell() : () => .Side) : .IObservable[.Float]
            	 = .ops.Mul(.orderbook.SafeSidePrice(.orderbook.Queue(.strategy.price.Book(x),side),.constant(.strategy.price.InitialValue(x))),.strategy.price.PriceDistr(x))
        
        @category = "-"
        
        @python.accessor()
        def Start(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData()) : .String
        
        
        def Strategy(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider(),
                     /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit()) : .ISingleAssetStrategy
            	 = .strategy.Combine(.strategy.price.OneSideStrategy(x,eventGen,orderFactory,.side.Sell()),.strategy.price.OneSideStrategy(x,eventGen,orderFactory,.side.Buy()))
        
        
        def StopLoss(inner : Optional[.ISuspendableStrategy] = .strategy.price.LadderMM() : .ISuspendableStrategy,
                     lossFactor : Optional[.IObservable[.Float]] = .const(0.2)) : .ISuspendableStrategy
            	 = .strategy.price.Clearable(inner,.strategy.price.isLossTooHigh(lossFactor))
        
        
        def StopLoss(inner : Optional[.ISuspendableStrategy] = .strategy.price.LadderMM() : .ISuspendableStrategy,
                     lossFactor : Optional[() => .Float] = .constant(0.2)) : .ISuspendableStrategy
            	 = .strategy.price.Clearable(inner,.strategy.price.isLossTooHigh(lossFactor))
        
        
        @python.intrinsic("strategy.ladder.Suspend_Impl")
        def Suspend(inner : Optional[.ISuspendableStrategy] = .strategy.price.LadderMM() : .ISuspendableStrategy,
                    predicate : Optional[() => .Boolean] = .false()) : .ISuspendableStrategy
        
        @category = "-"
        
        @python.accessor()
        def Book(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider()) : .IOrderBook
        
        
        def isLossTooHigh(lossFactor : Optional[.IObservable[.Float]] = .const(0.2)) : .IObservable[.Boolean]
            	 = .ops.Condition(.ops.Greater(.trader.Position(),.constant(0)),.ops.Greater(.trader.PerSharePrice(),.ops.Div(.orderbook.BestPrice(.orderbook.Asks()),.ops.Sub(.constant(1),lossFactor))),.ops.Condition(.ops.Less(.trader.Position(),.constant(0)),.ops.Less(.trader.PerSharePrice(),.ops.Mul(.orderbook.BestPrice(.orderbook.Bids()),.ops.Sub(.constant(1),lossFactor))),.false()))
        
        
        def isLossTooHigh(lossFactor : Optional[() => .Float] = .constant(0.2)) : .IObservable[.Boolean]
            	 = .ops.Condition(.ops.Greater(.trader.Position(),.constant(0)),.ops.Greater(.trader.PerSharePrice(),.ops.Div(.orderbook.BestPrice(.orderbook.Asks()),.ops.Sub(.constant(1),lossFactor))),.ops.Condition(.ops.Less(.trader.Position(),.constant(0)),.ops.Less(.trader.PerSharePrice(),.ops.Mul(.orderbook.BestPrice(.orderbook.Bids()),.ops.Sub(.constant(1),lossFactor))),.false()))
        
        
        def OneSideStrategy(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider(),
                            /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                            /** order factory function*/ orderFactory : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                            /** side of orders to create */ side : Optional[.IObservable[.Side]] = .side.observableSell()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(side,.strategy.price.Price(x,side)),eventGen)
        
        
        def OneSideStrategy(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider(),
                            /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every(.math.random.expovariate(1.0)),
                            /** order factory function*/ orderFactory : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                            /** side of orders to create */ side : Optional[() => .Side] = .side.Sell()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(side,.strategy.price.Price(x,side)),eventGen)
        
        @category = "-"
        
        @python.accessor()
        def End(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData()) : .String
        
        @category = "-"
        
        @python.constructor()
        def MarketData(/** Ticker of the asset */ ticker : Optional[.String] = "^GSPC",
                       /** Start date in DD-MM-YYYY format */ start : Optional[.String] = "2001-1-1",
                       /** End date in DD-MM-YYYY format */ end : Optional[.String] = "2010-1-1",
                       /** Price difference between orders placed and underlying quotes */ delta : Optional[.Float] = 1.0,
                       /** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume : Optional[.Float] = 1000.0) : .strategy.price.MarketData
        
        @category = "-"
        
        @python.accessor()
        def Ticker(x : Optional[.strategy.price.MarketData] = .strategy.price.MarketData()) : .String
        
        @category = "-"
        
        @python.accessor()
        def InitialValue(x : Optional[.strategy.price.LiquidityProvider] = .strategy.price.LiquidityProvider()) : .Float
        
        
        @python.intrinsic("strategy.ladder.MarketMaker_Impl")
        def LadderMM(orderFactory : Optional[((() => .Side),(() => .Float)) => .IObservable[.IOrder]] = .order._curried.sideprice_Limit(),
                     initialSize : Optional[.Int] = 10) : .ILadderStrategy
        
        
        @python.intrinsic("strategy.ladder.Balancer_Impl")
        def LadderBalancer(inner : Optional[.ILadderStrategy] = .strategy.price.LadderMM(),
                           maximalSize : Optional[.Int] = 20) : .ILadderStrategy
        
        
        @python.intrinsic("strategy.ladder.Clearable_Impl")
        def Clearable(inner : Optional[.ISuspendableStrategy] = .strategy.price.LadderMM() : .ISuspendableStrategy,
                      predicate : Optional[() => .Boolean] = .false()) : .ISuspendableStrategy
        
        @category = "-"
        
        @python.constructor()
        def MarketMaker(delta : Optional[.Float] = 1.0,
                        volume : Optional[.Float] = 20.0) : .strategy.price.MarketMaker
    }
    
    @category = "Volume function"
    
    package position {
        type DesiredPositionStrategy
        
        type Bollinger_linear : DesiredPositionStrategy
        
        type RSI_linear : DesiredPositionStrategy
        @category = "-"
        
        @python.accessor()
        def Timeframe(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear()) : .Float
        
        @category = "-"
        
        @python.constructor()
        def RSI_linear(/** alpha parameter for exponentially moving averages of up movements and down movements */ alpha : Optional[.Float] = 1.0/14.0,
                       /** observable scaling function that maps RSI deviation from 50 to the desired position */ k : Optional[.IObservable[.Float]] = .const(-0.04),
                       /** lag for calculating up and down movements */ timeframe : Optional[.Float] = 1.0,
                       /** trader in question */ trader : Optional[.ISingleAssetTrader] = .trader.SingleProxy()) : .strategy.position.RSI_linear
        
        @category = "-"
        
        @python.accessor()
        def Trader(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear()) : .ISingleAssetTrader
        
        @category = "-"
        
        @python.accessor()
        def Trader(x : Optional[.strategy.position.Bollinger_linear] = .strategy.position.Bollinger_linear()) : .ISingleAssetTrader
        
        
        def DesiredPosition(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear()) : .IObservable[.Float]
            	 = .ops.Mul(.ops.Sub(.constant(50.0),.observable.OnEveryDt(.math.Value(.math.RSI(.orderbook.MidPrice(.orderbook.OfTrader(.strategy.position.Trader(x))),.strategy.position.Timeframe(x),.strategy.position.Alpha(x))),1.0)),.strategy.position.K(x))
        
        
        def DesiredPosition(x : Optional[.strategy.position.Bollinger_linear] = .strategy.position.Bollinger_linear()) : .IObservable[.Float]
            	 = .ops.Mul(.observable.OnEveryDt(.math.RelStdDev(.math.EW(.orderbook.MidPrice(.orderbook.OfTrader(.strategy.position.Trader(x))),.strategy.position.Alpha(x))),1.0),.strategy.position.K(x))
        
        
        def Position(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear()) : .IObservable[.Float]
            	 = .ops.Sub(.ops.Sub(.strategy.position.DesiredPosition(x),.trader.Position(.strategy.position.Trader(x))),.trader.PendingVolume(.strategy.position.Trader(x)))
        
        
        def Position(x : Optional[.strategy.position.Bollinger_linear] = .strategy.position.Bollinger_linear()) : .IObservable[.Float]
            	 = .ops.Sub(.ops.Sub(.strategy.position.DesiredPosition(x),.trader.Position(.strategy.position.Trader(x))),.trader.PendingVolume(.strategy.position.Trader(x)))
        
        
        def Strategy(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear(),
                     /** order factory function */ orderFactory : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.signedVolume_MarketSigned()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.position.Position(x)))
        
        
        def Strategy(x : Optional[.strategy.position.Bollinger_linear] = .strategy.position.Bollinger_linear(),
                     /** order factory function */ orderFactory : Optional[(() => .Float) => .IObservable[.IOrder]] = .order._curried.signedVolume_MarketSigned()) : .ISingleAssetStrategy
            	 = .strategy.Generic(orderFactory(.strategy.position.Position(x)))
        
        @category = "-"
        
        @python.accessor()
        def K(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear()) : .IObservable[.Float]
        
        @category = "-"
        
        @python.accessor()
        def K(x : Optional[.strategy.position.Bollinger_linear] = .strategy.position.Bollinger_linear()) : .IObservable[.Float]
        
        @category = "-"
        
        @python.accessor()
        def Alpha(x : Optional[.strategy.position.RSI_linear] = .strategy.position.RSI_linear()) : .Float
        
        @category = "-"
        
        @python.accessor()
        def Alpha(x : Optional[.strategy.position.Bollinger_linear] = .strategy.position.Bollinger_linear()) : .Float
        
        @category = "-"
        
        @python.constructor()
        def Bollinger_linear(/** alpha parameter for exponentially weighted
                               * moving everage and variance */ alpha : Optional[.Float] = 0.15,
                             /** observable scaling function that maps
                               * relative deviation to desired position */ k : Optional[.IObservable[.Float]] = .const(0.5),
                             /** trader in question */ trader : Optional[.ISingleAssetTrader] = .trader.SingleProxy()) : .strategy.position.Bollinger_linear
    }
    
    
    package account {
        package inner {
            /** Associated with a strategy account that evaluates for every order sent by the strategy
             *  how it would be traded by sending request.evalMarketOrder
             *  (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
             *  but we want evaluate in any case would it be profitable or not)
             */
            
            @python.curried("VirtualMarket")
            def inner_VirtualMarket() : Optional[.ISingleAssetStrategy] => .IAccount
            
            /** Associated with a strategy account that tracks
             *  how orders sent by the strategy have been actually traded
             */
            
            @python.curried("Real")
            def inner_Real() : Optional[.ISingleAssetStrategy] => .IAccount
        }
        
        /** Associated with a strategy account that tracks
         *  how orders sent by the strategy have been actually traded
         */
        
        @python.intrinsic("strategy.account.Account_Impl")
        @curried("inner")
        def Real(/** strategy to track */ inner : Optional[.ISingleAssetStrategy] = .strategy.Empty()) : .IAccount
        
        /** Associated with a strategy account that evaluates for every order sent by the strategy
         *  how it would be traded by sending request.evalMarketOrder
         *  (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
         *  but we want evaluate in any case would it be profitable or not)
         */
        
        @python.intrinsic("strategy.account.VirtualMarket_Impl")
        @curried("inner")
        def VirtualMarket(/** strategy to track */ inner : Optional[.ISingleAssetStrategy] = .strategy.Empty()) : .IAccount
        
        def real = .strategy.account.inner.inner_Real
        
        def virtualMarket = .strategy.account.inner.inner_VirtualMarket
    }
    
    /** Creates a strategy combining two strategies
     *  Can be considered as a particular case of Array strategy
     */
    
    @python.intrinsic("strategy.combine.Combine_Impl")
    def Combine(A : Optional[.ISingleAssetStrategy] = .strategy.Empty(),
                B : Optional[.ISingleAssetStrategy] = .strategy.Empty()) : .ISingleAssetStrategy
    
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the most effective strategy
     * is chosen and made running; other strategies are suspended.
     * It can be considered as a particular case for MultiArmedBandit strategy with
     * *corrector* parameter set to *chooseTheBest*
     */
    
    @python.intrinsic("strategy.choose_the_best.ChooseTheBest_Impl")
    def ChooseTheBest(/** original strategies that can be suspended */ strategies : Optional[List[.ISingleAssetStrategy]] = [.strategy.Empty()],
                      /** function creating phantom strategy used for efficiency estimation */ account : Optional[Optional[.ISingleAssetStrategy] => .IAccount] = .strategy.account.inner.inner_VirtualMarket(),
                      /** function estimating is the strategy efficient or not */ performance : Optional[.IAccount => (() => .Float)] = .strategy.weight.trader.trader_TraderEfficiencyTrend()) : .ISingleAssetStrategy
    
    /** Strategy that wraps another strategy and passes its orders only if *predicate* is true
     */
    
    @python.intrinsic("strategy.suspendable.Suspendable_Impl")
    def Suspendable(/** wrapped strategy */ inner : Optional[.ISingleAssetStrategy] = .strategy.Empty(),
                    /** predicate to evaluate */ predicate : Optional[() => .Boolean] = .true()) : .ISingleAssetStrategy
    
    /** Strategy for a multi asset trader.
     * It believes that these assets represent a single asset traded on different venues
     * Once an ask at one venue becomes lower than a bid at another venue
     * it sends market sell and buy orders in order to exploit this arbitrage possibility
     */
    
    @python.intrinsic("strategy.arbitrage.Arbitrage_Impl")
    def Arbitrage() : .IMultiAssetStrategy
    
    /** Adaptive strategy that evaluates *inner* strategy efficiency
     *  and if it is considered as good, sends orders
     */
    
    def TradeIfProfitable(/** wrapped strategy */ inner : Optional[.ISingleAssetStrategy] = .strategy.Empty(),
                          /** defines how strategy trades are booked:
                            * actually traded amount or virtual market orders are
                            * used in order to estimate how the strategy would have traded
                            * if all its orders appeared at market */ account : Optional[Optional[.ISingleAssetStrategy] => .IAccount] = .strategy.account.inner.inner_VirtualMarket(),
                          /** given a trading account tells
                            * should it be considered as effective or not */ performance : Optional[.IAccount => (() => .Float)] = .strategy.weight.trader.trader_TraderEfficiencyTrend()) : .ISingleAssetStrategy
        	 = .strategy.Suspendable(inner,.ops.GreaterEqual(performance(account(inner)),.constant(0)))
    
    /** Creates a strategy combining an array of strategies
     */
    
    @python.intrinsic("strategy.combine.Array_Impl")
    def Array(/** strategies to combine */ strategies : Optional[List[.ISingleAssetStrategy]] = [.strategy.Empty()]) : .ISingleAssetStrategy
    
    /** Empty strategy doing nothing
     */
    
    @python.intrinsic("strategy.basic.Empty_Impl")
    def Empty() : .ISingleAssetStrategy
    
    /** A composite strategy initialized with an array of strategies.
     * In some moments of time the efficiency of the strategies is evaluated
     * These efficiencies are mapped into weights using *weight* and *normilizer*
     * functions per every strategy and *corrector* for the whole collection of weights
     * These weights are used to choose randomly a strategy to run for the next quant of time.
     * All other strategies are suspended
     */
    
    @python.intrinsic("strategy.multiarmed_bandit.MultiarmedBandit2_Impl")
    def MultiArmedBandit(/** original strategies that can be suspended */ strategies : Optional[List[.ISingleAssetStrategy]] = [.strategy.Empty()],
                         /** function creating a virtual account used
                           * to estimate efficiency of the strategy itself */ account : Optional[Optional[.ISingleAssetStrategy] => .IAccount] = .strategy.account.inner.inner_VirtualMarket(),
                         /** function estimating is the strategy efficient or not */ weight : Optional[.IAccount => (() => .Float)] = .strategy.weight.trader.trader_TraderEfficiencyTrend(),
                         /** function that maps trader efficiency to its weight
                           * that will be used for random choice */ normalizer : Optional[Optional[() => .Float] => (() => .Float)] = .strategy.weight.f.f_AtanPow(),
                         /** given array of strategy weights corrects them.
                           * for example it may set to 0 all weights except the maximal one */ corrector : Optional[Optional[List[.Float]] => (() => List[.Float])] = .strategy.weight.array.array_IdentityL()) : .ISingleAssetStrategy
    
    /** Strategy that listens to all orders sent by a trader to the market
     *  and in some moments of time it randomly chooses an order and cancels it
     *  Note: a similar effect can be obtained using order.WithExpiry meta orders
     */
    
    @python.intrinsic("strategy.canceller.Canceller_Impl")
    def Canceller(/** intervals between order cancellations */ cancellationIntervalDistr : Optional[() => .Float] = .math.random.expovariate(1.0)) : .ISingleAssetStrategy
    
    /** Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    @method = "Strategy"
    
    @python.intrinsic("strategy.generic.Generic_Impl")
    def Generic(/** order factory function*/ orderFactory : Optional[.IObservable[.IOrder]] = .order.Limit(),
                /** Event source making the strategy to wake up*/ eventGen : Optional[.IEvent] = .event.Every()) : .ISingleAssetStrategy
}

@category = "Trader"

package trader {
    /** Number of money owned by trader
     */
    
    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Float]
    
    /** Returns traders naive approximation of trader eficiency.
     *  It takes into account only the best price of the order queue
     */
    
    def RoughPnL(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Float]
        	 = .ops.Add(.trader.Balance(trader),.orderbook.NaiveCumulativePrice(.orderbook.OfTrader(trader),.trader.Position(trader)))
    
    /** Returns position of the trader
     *  It is negative if trader has sold more assets than has bought and
     *  positive otherwise
     */
    
    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Int]
    
    /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    
    def Efficiency(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Float]
        	 = .ops.Add(.trader.Balance(trader),.orderbook.CumulativePrice(.orderbook.OfTrader(trader),.trader.Position(trader)))
    
    /** Phantom trader that is used to refer to the current trader
     *  (normally it is used to define trader properties and strategies)
     */
    @label = "N/A"
    
    @python.intrinsic("trader.proxy.Single_Impl")
    def SingleProxy() : .ISingleAssetTrader
    
    /** A trader that trades different assets
     *  It can be considered as a composition of single asset traders and multi asset strategies
     *  At the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets
     */
    @label = "%(name)s"
    
    @python.intrinsic("trader.classes.MultiAsset_Impl")
    def MultiAsset(/** defines accounts for every asset to trade */ traders : Optional[List[.ISingleAssetTrader]] = [] : List[.ISingleAssetTrader],
                   /** multi asset strategy run by the trader */ strategy : Optional[.IMultiAssetStrategy] = .strategy.Arbitrage(),
                   name : Optional[.String] = "-trader-",
                   /** current trader balance (number of money units that it owns) */ PnL : Optional[.Float] = 0.0,
                   /** defines what data should be gathered for the trader */ timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .ITrader
    
    /** Returns first derivative of a moving average of the trader efficiency
     */
    
    def EfficiencyTrend(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount,
                        alpha : Optional[.Float] = 0.15) : () => .Float
        	 = .math.Derivative(.math.Avg(.math.EW(.trader.Efficiency(trader),alpha)))
    
    /** Cumulative volume of orders sent to the market but haven't matched yet
     */
    
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Int]
    
    
    def PerSharePrice(trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IObservable[.Float]
        	 = .ops.Sub(.constant(0),.ops.Div(.trader.Balance(trader),.trader.Position(trader)))
    
    /** A trader that trades a single asset on a single market
     */
    @label = "%(name)s"
    
    @python.intrinsic("trader.classes.SingleAsset_Impl")
    def SingleAsset(/** order book for the asset being traded */ orderBook : .IOrderBook,
                    /** strategy run by the trader */ strategy : Optional[.ISingleAssetStrategy] = .strategy.Empty(),
                    name : Optional[.String] = "-trader-",
                    /** current position of the trader (number of assets that it owns) */ amount : Optional[.Float] = 0.0,
                    /** current trader balance (number of money units that it owns) */ PnL : Optional[.Float] = 0.0,
                    /** defines what data should be gathered for the trader */ timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .ISingleAssetTrader
}

@category = "Asset"

package orderbook {
    /** Phantom orderbook that is used to refer to the current order book
     *
     *  May be used only in objects held by orderbooks (so it is normally used in orderbook properties)
     */
    @label = "N/A"
    
    @python.intrinsic("orderbook.of_trader.Proxy_Impl")
    def Proxy() : .IOrderBook
    
    /** Returns best price if defined, otherwise last price
     *  and *defaultValue* if there haven't been any trades
     */
    
    @python.observable()
    def SafeSidePrice(queue : Optional[.IOrderQueue] = .orderbook.Asks(),
                      /** price to be used if there haven't been any trades */ defaultValue : Optional[.IObservable[.Float]] = .const(100.0)) : .IObservable[.Float]
        	 = .IfDefined(.orderbook.BestPrice(queue),.IfDefined(.orderbook.LastPrice(queue),defaultValue))
    
    /** Returns best price if defined, otherwise last price
     *  and *defaultValue* if there haven't been any trades
     */
    
    @python.observable()
    def SafeSidePrice(queue : Optional[.IOrderQueue] = .orderbook.Asks(),
                      /** price to be used if there haven't been any trades */ defaultValue : Optional[() => .Float] = .constant(100.0)) : .IObservable[.Float]
        	 = .IfDefined(.orderbook.BestPrice(queue),.IfDefined(.orderbook.LastPrice(queue),defaultValue))
    
    /** Returns moving average of trade prices weighted by their volumes
     */
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    
    def WeightedPrice(queue : Optional[.IOrderQueue] = .orderbook.Asks(),
                      /** parameter alpha for the moving average  */ alpha : Optional[.Float] = 0.15) : () => .Float
        	 = .ops.Div(.math.Avg(.math.EW(.ops.Mul(.orderbook.LastTradePrice(queue),.orderbook.LastTradeVolume(queue)),alpha)),.math.Avg(.math.EW(.orderbook.LastTradeVolume(queue),alpha)))
    
    /** Returns tick size for the order *book*
     */
    
    @python.intrinsic("orderbook.props.TickSize_Impl")
    def TickSize(book : Optional[.IOrderBook] = .orderbook.OfTrader()) : () => .Float
    
    /** MidPrice of order *book*
     */
    
    def MidPrice(book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .IObservable[.Float]
        	 = .ops.Div(.ops.Add(.orderbook.BestPrice(.orderbook.Asks(book)),.orderbook.BestPrice(.orderbook.Bids(book))),.constant(2.0))
    
    /** Returns sell side order queue for *book*
     */
    
    @python.intrinsic("orderbook.proxy.Asks_Impl")
    def Asks(book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .IOrderQueue
        	 = .orderbook.Queue(book,.side.Sell())
    
    /** Returns volume of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    
    @python.intrinsic("orderbook.last_trade.LastTradeVolume_Impl")
    def LastTradeVolume(queue : Optional[.IOrderQueue] = .orderbook.Asks()) : .IObservable[.Int]
    
    /** Returns buy side order queue for *book*
     */
    
    @python.intrinsic("orderbook.proxy.Bids_Impl")
    def Bids(book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .IOrderQueue
        	 = .orderbook.Queue(book,.side.Buy())
    
    /** Returns best order price of *queue*
     *  Returns None is *queue* is empty
     */
    
    @python.intrinsic("orderbook.props.BestPrice_Impl")
    def BestPrice(queue : Optional[.IOrderQueue] = .orderbook.Asks()) : .IObservable[.Float]
    
    /** Represents latency in information propagation between two agents
     * (normally between a trader and a market).
     * Ensures that sending packets via links preserves their order.
     * Holds two one-way links in opposite directions.
     */
    
    @python.intrinsic("orderbook.link.TwoWayLink_Impl")
    def TwoWayLink(/** Forward link (normally from a trader to a market)*/ up : Optional[.ILink] = .orderbook.Link(),
                   /** Backward link (normally from a market to a trader)*/ down : Optional[.ILink] = .orderbook.Link()) : .ITwoWayLink
    
    /** Returns order queue of order *book* for trade *side*
     */
    
    @python.intrinsic("orderbook.proxy.Queue_Impl")
    def Queue(book : Optional[.IOrderBook] = .orderbook.OfTrader(),
              side : Optional[() => .Side] = .side.Sell()) : .IOrderQueue
    
    /** Phantom orderbook used to refer to the order book associated with a single asset trader
     *
     *  May be used only in objects that are held by traders (so it is used in trader properties and strategies)
     */
    @label = "N/A"
    @method = "Orderbook"
    
    @python.intrinsic("orderbook.of_trader.OfTrader_Impl")
    def OfTrader(Trader : Optional[.IAccount] = .trader.SingleProxy() : .IAccount) : .IOrderBook
    
    /** Returns price for best orders of total volume *depth*
     *
     *  In other words cumulative price corresponds to trader balance change
     *  if a market order of volume *depth* is completely matched
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    def CumulativePrice(book : Optional[.IOrderBook] = .orderbook.OfTrader(),
                        depth : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    
    /** Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]
     *  Level of volume V is a price at which cumulative volume of better orders is V
     */
    @label = "VolumeLevels(%(queue)s)"
    
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    def VolumeLevels(queue : Optional[.IOrderQueue] = .orderbook.Asks(),
                     /** distance between two volumes */ volumeDelta : Optional[.Float] = 30.0,
                     /** number of volume levels to track */ volumeCount : Optional[.Int] = 10) : .IObservable[.IVolumeLevels]
    
    /** Returns last defined price at *queue*
     *  Returns None is *queue* has been always empty
     */
    
    @python.intrinsic("orderbook.last_price.LastPrice_Impl")
    def LastPrice(queue : Optional[.IOrderQueue] = .orderbook.Asks()) : .IObservable[.Float]
    
    /** Order book for a single asset in a market.
     * Maintains two order queues for orders of different sides
     */
    @label = "%(name)s"
    
    @python.intrinsic("orderbook.local.Local_Impl")
    def Local(name : Optional[.String] = "-orderbook-",
              tickSize : Optional[.Float] = 0.01,
              _digitsToShow : Optional[.Int] = 2,
              timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .IOrderBook
    
    /** Represent an *orderbook* from point of view of a remote trader connected
     * to the market by means of a *link* that introduces some latency in information propagation
     */
    @label = "%(orderbook)s.name^remote"
    
    @python.intrinsic("orderbook.remote.Remote_Impl")
    def Remote(orderbook : Optional[.IOrderBook] = .orderbook.Local(),
               link : Optional[.ITwoWayLink] = .orderbook.TwoWayLink(),
               timeseries : Optional[List[.ITimeSerie]] = [] : List[.ITimeSerie]) : .IOrderBook
    
    /** Returns naive approximation of price for best orders of total volume *depth*
     *  by taking into account prices only for the best order
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    
    def NaiveCumulativePrice(book : Optional[.IOrderBook] = .orderbook.OfTrader(),
                             depth : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Less(depth,.constant(0.0)),.ops.Mul(depth,.orderbook.BestPrice(.orderbook.Asks(book))),.ops.Condition(.ops.Greater(depth,.constant(0.0)),.ops.Mul(depth,.orderbook.BestPrice(.orderbook.Bids(book))),.constant(0.0)))
    
    /** Returns naive approximation of price for best orders of total volume *depth*
     *  by taking into account prices only for the best order
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    
    def NaiveCumulativePrice(book : Optional[.IOrderBook] = .orderbook.OfTrader(),
                             depth : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
        	 = .ops.Condition(.ops.Less(depth,.constant(0.0)),.ops.Mul(depth,.orderbook.BestPrice(.orderbook.Asks(book))),.ops.Condition(.ops.Greater(depth,.constant(0.0)),.ops.Mul(depth,.orderbook.BestPrice(.orderbook.Bids(book))),.constant(0.0)))
    
    /** Represents latency in information propagation from one agent to another one
     * (normally between a trader and a market).
     * Ensures that sending packets via a link preserves their order.
     */
    
    @python.intrinsic("orderbook.link.Link_Impl")
    def Link(/** function called for each packet in order to determine
               * when it will appear at the end point*/ latency : Optional[.IObservable[.Float]] = .const(0.001)) : .ILink
    
    /** Spread of order *book*
     */
    
    def Spread(book : Optional[.IOrderBook] = .orderbook.OfTrader()) : .IObservable[.Float]
        	 = .ops.Sub(.orderbook.BestPrice(.orderbook.Asks(book)),.orderbook.BestPrice(.orderbook.Bids(book)))
    
    /** Returns price of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    
    @python.intrinsic("orderbook.last_trade.LastTradePrice_Impl")
    def LastTradePrice(queue : Optional[.IOrderQueue] = .orderbook.Asks()) : .IObservable[.Float]
}

@category = "Basic"

package observable {
    /** Discretizes function *x* at even time steps *dt*
     */
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    
    @python.intrinsic("observable.on_every_dt.OnEveryDt_Impl")
    def OnEveryDt(/** function to discretize */ x : Optional[() => .Float] = .constant(1.0),
                  /** time discretization step */ dt : Optional[.Float] = 1.0) : .IObservable[.Float]
    
    /** Observable listening to *source*
     *  When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
     */
    
    @python.intrinsic("observable.breaks_at_changes.BreaksAtChanges_Impl")
    def BreaksAtChanges(source : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    
    /** Observable that downloads closing prices for every day from *start* to *end* for asset given by *ticker*
     *  and follows the price in scale 1 model unit of time = 1 real day
     */
    @label = "%(ticker)s"
    
    @python.intrinsic("observable.quote.Quote_Impl")
    def Quote(/** defines quotes to download */ ticker : Optional[.String] = "^GSPC",
              /** defines first day to download in form YYYY-MM-DD */ start : Optional[.String] = "2001-1-1",
              /** defines last day to download in form YYYY-MM-DD */ end : Optional[.String] = "2010-1-1") : .IObservable[.Float]
}

type ITrader

type IGraph

type Function[T] : IFunction[T]

type Volume = Int

type Optional[T]

type IAccount

type IOrder

type Side

type Boolean

type Price = Float

type IOrderQueue

type Float

type Int : Float

type ILink

type IOrderBook

type IEvent

type ILadderStrategy : ISuspendableStrategy

type IMultiAssetStrategy

type ITwoWayLink

type IObservable[U] : IFunction[U], IEvent

type IFunction[T] = () => T

type ISingleAssetStrategy

type ISingleAssetTrader : IAccount, ITrader

type IVolumeLevels

type ISuspendableStrategy : ISingleAssetStrategy

type List[T]

type Observable[U] : IObservable[U]

type IDifferentiable : IFunction[Float]

type ITimeSerie

type Any

type ICandleStick

type IOrderGenerator = IObservable[IOrder]

type String
/** Function always returning *x*
 */
@category = "Basic"
@label = "C=%(x)s"

def constant(x : Optional[.Int] = 1) : () => .Int
    	 = .const(x) : () => .Int

/** Function always returning *x*
 */
@category = "Basic"
@label = "C=%(x)s"

def constant(x : Optional[.Float] = 1.0) : () => .Float
    	 = .const(x) : () => .Float

/** Function always returning *False*
 */
@category = "Basic"
@label = "False"

def false() : () => .Boolean
    	 = .observableFalse() : () => .Boolean

/** Trivial observable always returning *True*
 */
@category = "Basic"
@label = "True"

@python.intrinsic.observable("_constant.True_Impl")
def observableTrue() : .IObservable[.Boolean]

@category = "Basic"

@python.intrinsic("event.CurrentTime_Impl")
def CurrentTime() : .IObservable[.Float]

/** Trivial observable always returning *undefined* or *None* value
 */
@category = "Basic"

@python.intrinsic("_constant.Null_Impl")
def null() : () => .Float

/** Time serie to store and render it after on a graph
 *  Used to specify what data should be collected about order books and traders
 */
@category = "Basic"
@label = "%(source)s"

@python.intrinsic("timeserie.ToRecord_Impl")
def TimeSerie(source : Optional[.IObservable[Any]] = .const(0.0) : .IObservable[Any],
              graph : Optional[.IGraph] = .veusz.Graph(),
              _digitsToShow : Optional[.Int] = 4,
              _smooth : Optional[.Int] = 1) : .ITimeSerie

/** Trivial observable always returning *False*
 */
@category = "Basic"
@label = "False"

@python.intrinsic.observable("_constant.False_Impl")
def observableFalse() : .IObservable[.Boolean]

/** Trivial observable always returning *x*
 */
@category = "Basic"
@label = "C=%(x)s"
@trivialObservable = "true"

@python.intrinsic.observable("_constant.Constant_Impl")
def const(x : Optional[.Int] = 1) : .IObservable[.Int]

/** Trivial observable always returning *x*
 */
@category = "Basic"
@label = "C=%(x)s"
@trivialObservable = "true"

@python.intrinsic.observable("_constant.Constant_Impl")
def const(x : Optional[.Float] = 1.0) : .IObservable[.Float]

/** Observable returning at the end of every *timeframe*
 * open/close/min/max price, its average and standard deviation
 */
@category = "Basic"
@label = "Candles_{%(source)s}"

@python.intrinsic("observable.candlestick.CandleSticks_Impl")
def CandleSticks(/** observable data source considered as asset price */ source : Optional[.IObservable[.Float]] = .const(1.0),
                 /** size of timeframe */ timeframe : Optional[.Float] = 10.0) : .IObservable[.ICandleStick]

/** Function always returning *True*
 */
@category = "Basic"
@label = "True"

def true() : () => .Boolean
    	 = .observableTrue() : () => .Boolean

/** Returns *x* if defined and *elsePart* otherwise
 */
@category = "Basic"
@label = "If def(%(x)s) else %(elsePart)s"
@method = "getOrElse"

@python.observable()
def IfDefined(x : Optional[.IObservable[.Float]] = .const(1.0),
              /** function to take values from when *x* is undefined */ elsePart : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    	 = .ops.Condition(.ops.NotEqual(x,.null()),x,elsePart)

/** Returns *x* if defined and *elsePart* otherwise
 */
@category = "Basic"
@label = "If def(%(x)s) else %(elsePart)s"
@method = "getOrElse"

@python.observable()
def IfDefined(x : Optional[() => .Float] = .constant(1.0),
              /** function to take values from when *x* is undefined */ elsePart : Optional[.IObservable[.Float]] = .const(1.0)) : .IObservable[.Float]
    	 = .ops.Condition(.ops.NotEqual(x,.null()),x,elsePart)

/** Returns *x* if defined and *elsePart* otherwise
 */
@category = "Basic"
@label = "If def(%(x)s) else %(elsePart)s"
@method = "getOrElse"

@python.observable()
def IfDefined(x : Optional[.IObservable[.Float]] = .const(1.0),
              /** function to take values from when *x* is undefined */ elsePart : Optional[() => .Float] = .constant(1.0)) : .IObservable[.Float]
    	 = .ops.Condition(.ops.NotEqual(x,.null()),x,elsePart)

/** Returns *x* if defined and *elsePart* otherwise
 */
@category = "Basic"
@label = "If def(%(x)s) else %(elsePart)s"
@method = "getOrElse"

@python.observable()
def IfDefined(x : Optional[() => .Float] = .constant(1.0),
              /** function to take values from when *x* is undefined */ elsePart : Optional[() => .Float] = .constant(1.0)) : () => .Float
    	 = .ops.Condition(.ops.NotEqual(x,.null()),x,elsePart)

/** Time serie holding volume levels of an asset
 * Level of volume V is a price at which cumulative volume of better orders is V
 */
@category = "Basic"
@label = "%(source)s"

@python.intrinsic("timeserie.VolumeLevels_Impl")
def volumeLevels(source : () => .IVolumeLevels,
                 graph : Optional[.IGraph] = .veusz.Graph(),
                 _digitsToShow : Optional[.Int] = 4,
                 _smooth : Optional[.Int] = 1,
                 _volumes : Optional[List[.Float]] = [30.0],
                 _isBuy : Optional[.Int] = 1) : .ITimeSerie
