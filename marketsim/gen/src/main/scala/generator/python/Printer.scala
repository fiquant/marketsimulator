package generator.python

object Printer {

    trait Printable {
        def toPython : String
    }

    object types {

        trait Base

        trait Unit extends Printable {
            def toPython =
                throw new Exception("Unit types are not supported yet for python generation")
        }

        trait Tuple extends Printable {
            val elems : List[Base]
            def toPython = {
                throw new Exception("Tuple types are not supported yet for python generation")
                //elems.mkString("(", ",", ")")
            }

        }

        trait Function extends Printable {
            val args : List[Base]
            val ret : Base
            def toPython = {
                val a = args match {
                    case Nil => ""
                    case x :: Nil => "," + x
                    case _ => throw new Exception("Only unary and nullary functions are supported for python generation")
                }
                s"types.IFunction[$ret$a]"
                //(if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
            }
        }

        trait `Float`    extends Printable {  def toPython = "float"  }
        trait `Boolean`  extends Printable {  def toPython = "bool"   }

    }

    import syntax.scala.Printer.{base => pp}

    trait PrintablePort extends Printable
    {
        def toScala : String
        override def toPython = toScala
    }

    trait Expr extends pp.Expr with PrintablePort
    trait BooleanExpr extends pp.BooleanExpr with PrintablePort

    trait BinOp extends pp.BinOp[Typed.ArithExpr] with PrintablePort
    trait Neg extends pp.Neg[Typed.ArithExpr] with PrintablePort

    trait IfThenElse extends pp.IfThenElse[Typed.ArithExpr, Typed.BooleanExpr] with PrintablePort
    trait And extends pp.And[Typed.BooleanExpr] with PrintablePort
    trait Or extends pp.Or[Typed.BooleanExpr] with PrintablePort
    trait Not extends pp.Not[Typed.BooleanExpr, Typed.ArithExpr] with PrintablePort
    trait Condition extends pp.Condition[Typed.ArithExpr] with PrintablePort

    type Priority_0 = pp.Priority_0

    trait FloatConst extends Expr with Priority_0 {
        self: Typed.FloatConst =>
        override def toPython = x.toString
    }

    trait ParamRef extends Expr with Priority_0 {
        self: Typed.ParamRef =>
        override def toPython = p.name
    }

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>
        override def toPython = target.parent.qualifyName(target.name) + arguments.map({ _._2 }).mkString("(",",",")")
    }

}
