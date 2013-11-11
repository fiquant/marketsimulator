def A(x = B()) : Float
def C(x = A()) : Float
def B(x = const()) : Float

 ->
def A(x = B()) : Float

def C(x = A()) : Float

def B(x = const()) : Float


