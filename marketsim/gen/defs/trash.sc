@python = "no"
package trash

package types {
    type T1 = T

    package {
        type T
    }

    package {
        type R : T
    }

    package {
        package {
            type U : T, R
        }
    }

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
def A(x : () => .trash.types.T1 = .trash.A()) => types.U

package in2
def A(x = constant(), y = if 3 > x + 2 then x else x*2) => types.T

def S1(y = "abc") = y

def S2() : Optional[String] = S1()

def C(x : IFunction[CandleStick], p = [12, 23.2, 0]) = p

def IntFunc() : IFunction[Int]

def F(x  = IntFunc() : IFunction[Float]) = x

def IntObs() : IObservable[Int]

def O(x = IntObs() : IObservable[Float] ) = x





