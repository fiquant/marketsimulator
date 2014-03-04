@category = "internal tests"
@method = "N/A"
package _test

@X = "X"
@Y = "Y"
package A.B {
    @X = "Xa"
    def f() => Float

    @X = "Xb"
    package {
        def g() => Float
        def h() => Float
    }
}

package types {
    type T1 = T

    type T

    type R : T

    type U : R
}

package overloading {

    def f(x : IFunction[Price]) = x
    def f(x : IFunction[Volume]) = x

    def g(x : IFunction[Volume]) = f(x)

    def h() = f(12)
    def hh() = f(12.2)

}

abstract package _base1 { def toInject1() => Int }
abstract package _base2 { def toInject2() => Int }

def A(x = in1.in2.A()) => types.R

package in1 extends _base1 extends _base2
def A(x : () => ._test.types.T1 = ._test.A()) => types.U

package in2
def A(x = constant(), y = if 3 > x + 2 then x else x*2) => types.T

def S1(y = "abc") = y

def S2() : Optional[String] = S1()

def C(x : IFunction[ICandleStick], p = 12) = p

def IntFunc() : IFunction[Int] = const(0)

def F(x  = IntFunc() : IFunction[Float]) = x

def IntObs() : IObservable[Int] = const(0)

def O(x = IntObs() : IObservable[Float] ) = x





