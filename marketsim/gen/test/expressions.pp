1 + -6*z ->
1.0 + -6.0 * z


-t/p -a*l ->
-t / p - a * l


1 + 3 - (a + b) ->
1.0 + 3.0 - (a + b)


a*v / (a*p) ->
a * v / (a * p)


p + (if a + 12 < 9 then n - 2 else if j*u <> 7 or (j >= 0) and not o = i then 8 + j else k) ->
p + (if xxx then n - 2.0 else if xxx then 8.0 + j else k)


a(12, b(p, a + 8)) ->
QualifiedName(List(a))(List(Const(12.0), FunCall(QualifiedName(List(b)),List(Var(p), BinOp(Add(),Var(a),Const(8.0))))))


