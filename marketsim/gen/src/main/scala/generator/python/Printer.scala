package generator.python

object Printer {

    import syntax.scala.Printer.{base => pp, types => st}

    trait Printable {
        def toPython : String
        def imports : List[predef.Importable]
    }

    object types {

        trait Base

        trait Unit extends Printable {
            def toPython =
                throw new Exception("Unit types are not supported yet for python generation")
            def imports = Nil

        }

        trait Tuple extends Printable {
            val elems : List[Base]
            def toPython = {
                throw new Exception("Tuple types are not supported yet for python generation")
                //elems.mkString("(", ",", ")")
            }

            def imports = Nil
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

            def imports = Nil
        }

        trait `Float`    extends Printable
        {
            def toPython = "float"
            def imports = Nil
        }

        trait `Boolean`  extends Printable
        {
            def toPython = "bool"
            def imports = Nil
        }

        trait UserDefined extends st.UserDefined with PrintablePort
        {
            def imports = Nil
        }
    }

    trait PrintablePort extends Printable
    {
        def toScala : String
        override def toPython = toScala
    }

    trait Expr extends pp.Expr with PrintablePort
    trait BooleanExpr extends pp.BooleanExpr with PrintablePort

    trait BinOp extends pp.BinOp[Typed.ArithExpr] with PrintablePort
    {
        override def imports = x.imports ++ y.imports
    }

    trait Neg extends pp.Neg[Typed.ArithExpr] with PrintablePort
    {
        override def imports = x.imports
    }

    trait IfThenElse extends pp.IfThenElse[Typed.ArithExpr, Typed.BooleanExpr] with PrintablePort
    {
        override def toPython = s"($cond)[${wrap(x)}, ${wrap(y)}]"

        override def imports = x.imports ++ y.imports ++ cond.imports
    }

    trait And extends pp.And[Typed.BooleanExpr] with PrintablePort
    {
        override def imports = x.imports ++ y.imports
    }
    trait Or extends pp.Or[Typed.BooleanExpr] with PrintablePort {
        override def imports = x.imports ++ y.imports
    }

    trait Not extends pp.Not[Typed.BooleanExpr, Typed.ArithExpr] with PrintablePort {
        override def imports = x.imports
    }

    trait Condition extends pp.Condition[Typed.ArithExpr] with PrintablePort {
        override def imports = x.imports ++ y.imports
    }

    type Priority_0 = pp.Priority_0

    trait FloatConst extends Expr with Priority_0 {
        self: Typed.FloatConst =>
        override def toPython = x.toString

        def imports = Nil
    }

    trait ParamRef extends Expr with Priority_0 {
        self: Typed.ParamRef =>
        override def toPython = "self." + p.name

        def imports = Nil
    }

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>
        override def toPython = target.name + arguments.map({ _._2 }).mkString("(",",",")")

        def moduleName = {
            val name = target.parent.qualifiedName mkString "."
            val d = if (name == "") name else "." + name
            "marketsim.gen._out" + (if (name == "") name else "." + name)
        }

        override def imports = predef.ImportFrom(target.name, moduleName) :: Nil
    }

}
