gammavariate -> 
def gammavariate(Alpha : Float = 1.0, Beta : Float = 1.0) : Float
sqr -> 
def sqr(x : () => Float = const()) : Float
normalvariate -> 
def normalvariate(Mu : Float = 0.0, Sigma : Float = 1.0) : Float
paretovariate -> 
def paretovariate(Alpha : Float = 1.0) : Float
Atan -> 
def Atan(x : () => Float = const(0.0)) : Float
A -> 
def A(x : () => Float = B()) : Float
min -> 
def min(x : () => Float = const(), y : () => Float = const()) : Float
triangular -> 
def triangular(Low : Float = 0.0, High : Float = 1.0, Mode : Float = 0.5) : Float
vonmisesvariate -> 
def vonmisesvariate(Mu : Float = 0.0, Kappa : Float = 0.0) : Float
uniform -> 
def uniform(Low : Float = -10.0, High : Float = 10.0) : Float
Sqrt -> 
def Sqrt(x : () => Float = const(1.0)) : Float
const -> 
def const(x : Float = 1.0) : Float
max -> 
def max(x : () => Float = const(), y : () => Float = const()) : Float
Exp -> 
def Exp(x : () => Float = const(1.0)) : Float
Log -> 
def Log(x : () => Float = const(1.0)) : Float
weibullvariate -> 
def weibullvariate(Alpha : Float = 1.0, Beta : Float = 1.0) : Float
B -> 
def B(x : () => Float = const(), y : () => Float = if  then x else x*2.0) : Float
C -> 
def C(x : () => Float = A()) : Float
expovariate -> 
def expovariate(Lambda : Float = 1.0) : Float
lognormvariate -> 
def lognormvariate(Mu : Float = 0.0, Sigma : Float = 1.0) : Float
betavariate -> 
def betavariate(Alpha : Float = 1.0, Beta : Float = 1.0) : Float
Pow -> 
def Pow(base : () => Float = const(1.0), power : () => Float = const(1.0)) : Float
