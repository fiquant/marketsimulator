case class Parameter(name        : String,
                     ty          : Option[String],
                     initializer : Option[Expr],
                     annotations : List[Annotation]) {
    override def toString = annotations.mkString(" ") + s" $name : $ty = $initializer"
}

case class QualifiedName(names   : List[String]) {
    override def toString = names.mkString(".")
}

case class Annotation(name       : QualifiedName,
                      parameters : List[String]) {
    override def toString = s"@$name(${parameters.mkString(" ")})"
}

case class DocString(brief : String, detailed : String)

case class FunDef(name           : String,
                  parameters     : List[Parameter],
                  body           : Option[Expr],
                  docstring      : Option[DocString],
                  annotations    : List[Annotation]) {
    override def toString = annotations.mkString("\r\n") + s"$name(${parameters.mkString(",")}})"
}

sealed abstract class BinOpSymbol
case class Add() extends BinOpSymbol {
    override val toString = "+"
}
case class Sub() extends BinOpSymbol {
    override val toString = "-"
}
case class Mul() extends BinOpSymbol {
    override val toString = "*"
}
case class Div() extends BinOpSymbol {
    override val toString = "/"
}

sealed abstract class Expr {

    def priority(e : Expr) = e match {
        case Const(_) => 0
        case Var(_) => 0
        case Neg(_) => 0
        case FunCall(_, _) => 0

        case BinOp(Mul(), _, _) => 1
        case BinOp(Div(), _, _) => 1

        case BinOp(Add(), _, _) => 2
        case BinOp(Sub(), _, _) => 2

        case IfThenElse(_,_,_) => 3
    }

    def need_brackets(x : Expr, e : Expr, rhs : Boolean = false) =
        priority(x) > priority(e) || (priority(x) == priority(e) && rhs)

    def wrap_if_needed(x : Expr, e : Expr, rhs : Boolean = false) =
        if (need_brackets(x,e,rhs)) parens(x.toString) else x.toString

    def parens(x : String) = "(" + x + ")"
}

case class Const(value: Double) extends Expr {
    override val toString = value.toString
}
case class Var(s : String) extends Expr {
    override val toString = s
}
case class BinOp(symbol : BinOpSymbol, x: Expr, y: Expr) extends Expr {
    override def toString = wrap_if_needed(x, this) + symbol + wrap_if_needed(y, this, rhs = true)
}

case class Neg(x: Expr) extends Expr {
    override def toString = "-" + wrap_if_needed(x, this)
}

case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr) extends Expr {
    override def toString = s"if $cond then ${wrap_if_needed(x, this)} else ${wrap_if_needed(y, this)}"
}
case class FunCall(name : QualifiedName, args : List[Expr]) extends Expr {
    override def toString = name.toString + parens(args.map(_.toString).mkString(","))
}

sealed abstract class CondSymbol

case class Less() extends CondSymbol {
    override val toString = "<"
}
case class LessEqual() extends CondSymbol {
    override val toString = "<="
}
case class Greater() extends CondSymbol {
    override val toString = ">"
}
case class GreaterEqual() extends CondSymbol {
    override val toString = ">="
}
case class Equal() extends CondSymbol {
    override val toString = "="
}
case class NotEqual() extends CondSymbol {
    override val toString = "<>"
}

sealed abstract class BooleanExpr {
    def wrap_if_needed(x : BooleanExpr, e : And) = x match {
        case y : Or => "(" + y + ")"
        case y => y.toString
    }

    def wrap_if_needed(x : BooleanExpr, e : Not) = x match {
        case Condition(_,_,_) => x.toString
        case _ => "(" + x + ")"
    }

}
case class Condition(symbol : CondSymbol, x : Expr, y : Expr) extends BooleanExpr {
    override def toString = x.toString + symbol + y
}

case class Or   (x : BooleanExpr, y : BooleanExpr) extends BooleanExpr {
    override def toString = x + " or " + y
}

case class And  (x : BooleanExpr, y : BooleanExpr) extends BooleanExpr {
    override def toString = wrap_if_needed(x, this) + " and " + wrap_if_needed(y, this)
}

case class Not  (x : BooleanExpr) extends BooleanExpr {
    override def toString = "not " +  wrap_if_needed(x, this)
}
