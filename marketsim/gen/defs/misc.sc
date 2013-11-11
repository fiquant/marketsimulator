def A(x = B()) : Float
def C(x = A()) : Float
def B(x = const(), y = if 3 > x + 2 then x else x*2) : Float

