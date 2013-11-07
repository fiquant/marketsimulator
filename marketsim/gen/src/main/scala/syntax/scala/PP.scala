package object PP {

    val crlf = "\r\n"

    trait SimpleType extends AST.SimpleType
    {
        override def toString = name
    }

    trait UnitType extends AST.UnitType
    {
        override def toString = "()"
    }

    trait TupleType extends AST.TupleType
    {
        override def toString = "(" + types.mkString(",") + ")"
    }

    trait FunctionType extends AST.FunctionType
    {
        override def toString = s"$arg_type => $ret_type"
    }

    trait Parameter extends AST.Parameter
    {
        override def toString = (annotations.map({ _ + " "}).mkString("")
                + name
                + (if (ty.nonEmpty) " : " + ty.get else "")
                + (if (initializer.nonEmpty) " = " + initializer.get else ""))
    }

    trait QualifiedName extends AST.QualifiedName
    {
        override def toString = names.mkString(".")
    }

    trait Annotation extends AST.Annotation
    {
        override def toString = "@" + name + "(" + parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"
    }

    trait DocString extends AST.DocString
    {
        override def toString = "/** " + brief + detailed.lines.map({ crlf + " *" + _ }).mkString("") + crlf + " */" + crlf
    }

    trait FunDef extends AST.FunDef
    {
        override def toString = (
                (if (docstring.nonEmpty) docstring.get else "")
                + annotations.map({_ + crlf}).mkString("")
                + "def " + name
                + "(" + parameters.mkString(", ") + ")"
                + (if (ret_type.nonEmpty) " : " + ret_type.get else "")
                + (if (body.nonEmpty) " = " + body.get else ""))
    }

    trait Definitions extends AST.Definitions {
        override def toString = definitions.map({_ + crlf + crlf}).mkString("")
    }

    trait BinOpSymbol extends AST.BinOpSymbol {
        def symbol : String
        override def toString = symbol
    }
    trait Add extends AST.Add with BinOpSymbol {
        val symbol = "+"
    }
    trait Sub extends AST.Sub with BinOpSymbol {
        val symbol = "-"
    }
    trait Mul extends AST.Mul with BinOpSymbol {
        val symbol = "*"
    }
    trait Div extends AST.Div with BinOpSymbol {
        val symbol = "/"
    }

    trait Const extends AST.Const {
        override val toString = value.toString
    }
    trait Var extends AST.Var {
        override val toString = s
    }


    trait Expr extends AST.Expr {

        def need_brackets(x : AST.Expr, rhs : Boolean = false) =
            x.priority > priority || x.priority == priority && rhs

        def wrap_if_needed(x : AST.Expr, rhs : Boolean = false) =
            if (need_brackets(x,rhs)) parens(x.toString) else x.toString

        def parens(x : String) = "(" + x + ")"
    }

    trait BinOp extends AST.BinOp with Expr {
        override def toString = wrap_if_needed(x) + symbol + wrap_if_needed(y, rhs = true)
    }

    trait Neg extends AST.Neg with Expr {
        override def toString = "-" + wrap_if_needed(x)
    }

    trait IfThenElse extends AST.IfThenElse with Expr {
        override def toString = s"if $cond then ${wrap_if_needed(x)} else ${wrap_if_needed(y)}"
    }
    trait FunCall extends AST.FunCall with Expr {
        override def toString = name.toString + parens(args.map(_.toString).mkString(","))
    }

    trait CondSymbol extends AST.CondSymbol {
        def symbol : String
        override def toString = symbol
    }

    trait Less extends AST.Less with CondSymbol { val symbol = "<" }
    trait LessEqual extends AST.LessEqual with CondSymbol { val symbol = "<=" }
    trait Greater extends AST.Greater with CondSymbol { val symbol = ">" }
    trait GreaterEqual extends AST.GreaterEqual with CondSymbol { val symbol = ">=" }
    trait Equal extends AST.Equal with CondSymbol { val symbol = "=" }
    trait NotEqual extends AST.NotEqual with CondSymbol { val symbol = "<>" }

    trait Condition extends AST.Condition {
        override def toString = x.toString + symbol + y
    }

    trait Or extends AST.Or {
        override def toString = x + " or " + y
    }

    trait And extends AST.And
    {
        override def toString = wrap_if_needed(x) + " and " + wrap_if_needed(y)

        def wrap_if_needed(x : AST.BooleanExpr) = x match {
            case z : AST.Or => "(" + z + ")"
            case z => z.toString
        }
    }

    trait Not extends AST.Not
    {
        override def toString = "not " +  wrap_if_needed(x)

        def wrap_if_needed(x : AST.BooleanExpr) = x match {
            case AST.Condition(_,_,_) => x.toString
            case _ => "(" + x + ")"
        }
    }

}
