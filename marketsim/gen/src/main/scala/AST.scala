case class Parameter(name        : String,
                     ty          : Option[String],
                     initializer : Option[Expr],
                     annotations : List[Annotation])

case class QualifiedName(names   : List[String])

case class Annotation(name       : QualifiedName,
                      parameters : List[String])

case class FunDef(name           : String,
                  parameters     : List[Parameter],
                  body           : Option[Expr],
                  docstring      : Option[String],
                  annotations    : List[Annotation])

sealed abstract class Expr
case class Const(value: Double) extends Expr
case class Var(s : String) extends Expr
case class Add(x: Expr, y: Expr) extends Expr
case class Sub(x: Expr, y: Expr) extends Expr
case class Mul(x: Expr, y: Expr) extends Expr
case class Div(x: Expr, y: Expr) extends Expr
case class Neg(x: Expr) extends Expr
case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr) extends Expr
case class FunCall(name : QualifiedName, args : List[Expr]) extends Expr

sealed abstract class BooleanExpr
case class Less         (x : Expr, y : Expr) extends BooleanExpr
case class LessEqual    (x : Expr, y : Expr) extends BooleanExpr
case class Greater      (x : Expr, y : Expr) extends BooleanExpr
case class GreaterEqual (x : Expr, y : Expr) extends BooleanExpr
case class Equal        (x : Expr, y : Expr) extends BooleanExpr
case class NotEqual     (x : Expr, y : Expr) extends BooleanExpr

case class Or   (x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
case class And  (x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
case class Not  (x : BooleanExpr) extends BooleanExpr
