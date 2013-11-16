package syntax.scala

package object Printer
{
    val crlf = "\r\n"
    val tab = "\t"
    
    trait Printable {
        def toScala : String
    }

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

    def prefixedIfSome[A](p : Option[A], prefix : String = "") =
        if (p.nonEmpty) prefix + p.get else ""

    object base {
        trait Expr extends Printable {
            val priority : Int

            def wrap(x : Expr, rhs : Boolean = false) =
                pars(x, need_brackets(x, rhs))

            def need_brackets(x : Expr, rhs : Boolean) =
                x.priority > priority || x.priority == priority && rhs
        }

        trait BinOpSymbol extends Printable {
            val priority : Int
        }

        trait Add extends BinOpSymbol {
            def toScala = "+"
            val priority = 2
        }
        trait Sub extends BinOpSymbol {
            def toScala = "-"
            val priority = 2
        }
        trait Mul extends BinOpSymbol {
            def toScala = "*"
            val priority = 1
        }
        trait Div extends BinOpSymbol {
            def toScala = "/"
            val priority = 1
        }

        trait BinOp[T <: Expr] extends Expr {
            val x, y : T
            val symbol : BinOpSymbol
            def toScala = wrap(x) + symbol + wrap(y, rhs = true)
            val priority = symbol.priority
        }

        trait Neg[T <: Expr] extends Expr {
            val x : T
            def toScala = "-" + wrap(x)
            val priority = 0
        }

        trait CondSymbol

        trait IfThenElse[T <: Expr, U <: BooleanExpr] extends Expr {
            val x, y : T
            val cond : U
            def toScala = s"if $cond then ${wrap(x)} else ${wrap(y)}"
            val priority = 3
        }

        trait BooleanExpr

        trait Or[T <: BooleanExpr] extends BooleanExpr with Printable {
            val x, y : T
            def toScala = s"$x or $y"
        }

        trait And[T <: BooleanExpr] extends BooleanExpr with Printable {
            val x, y : T
            def wrap(z : T) = pars(z, z.isInstanceOf[Or[T]])
            def toScala = wrap(x) + " and " + wrap(y)
        }

        trait Not[T <: BooleanExpr, U <: Expr] extends BooleanExpr with Printable {
            val x : T
            def wrap(z : T) = pars(z, !z.isInstanceOf[Condition[U]])
            def toScala = "not " + wrap(x)
        }

        trait Condition[T <: Expr] extends BooleanExpr with Printable {
            val x, y : Expr
            val symbol : CondSymbol
            def toScala = x.toString + symbol + y
        }

        trait Definition

        trait Definitions[T <: Definition] extends Printable {
            val definitions: List[T]
            def toScala = definitions.map({_ + crlf}).mkString("")
        }

        trait DocString extends Printable {
            val brief, detailed : String
            def toScala =
                ("/** " + brief
                        + detailed.lines.map({ crlf + " *" + _ }).mkString("") + crlf
                        + " */" + crlf)

        }

        trait QualifiedName extends Printable {
            val names : List[String]
            def toScala = names.mkString(".")
        }

        trait Annotation extends Printable {
            def getName : String
            val parameters : List[String]
            def toScala =
                "@" + getName + "(" + parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"
        }

        trait Parameter extends Printable {
            val annotations : List[Annotation]
            val name : String
            def printType : String
            def printInitializer : String
            
            def toScala =
                (annotations.map({ _ + " "}).mkString("")
                        + name
                        + printType
                        + printInitializer)
        }

        trait Function extends Printable with Definition {
            val docstring : Option[DocString]
            val annotations : List[Annotation]
            val name : String
            val parameters : List[Parameter]
            def printRetType : String
            def printBody : String

            def toScala =
                (crlf   + prefixedIfSome(docstring)
                        + annotations.map({_ + crlf}).mkString("")
                        + "def " + name
                        + parameters.mkString("(", ", ", ")")
                        + printRetType
                        + printBody)
        }
    }

    object ast {

        type Expr = base.Expr
        type BooleanExpr = base.BooleanExpr
        type CondSymbol = base.CondSymbol
        type BinOpSymbol = base.BinOpSymbol
        type Add = base.Add
        type Sub = base.Sub
        type Mul = base.Mul
        type Div = base.Div
        type Definition = base.Definition
        type Definitions = base.Definitions[AST.FunDef]
        type DocString = base.DocString
        type QualifiedName = base.QualifiedName

        trait Annotation extends base.Annotation {
            self: AST.Annotation =>
            def getName  = name.toString
        }

        trait Function extends base.Function {
            self: AST.FunDef =>
            def printRetType = prefixedIfSome(ret_type, " : ")
            def printBody = prefixedIfSome(body, " = ")
        }

        trait Parameter extends base.Parameter {
            self: AST.Parameter =>
            def printType = prefixedIfSome(ty, " : ")
            def printInitializer = prefixedIfSome(initializer, " = ")
        }

        trait Const extends Expr {
            self: AST.Const =>
            def toScala = value.toString
            val priority = 0
        }

        trait Var extends Expr {
            self: AST.Var =>
            def toScala = s
            val priority = 0
        }

        trait FunCall extends Expr {
            self: AST.FunCall =>
            def toScala = name + pars(args.mkString(","))
            val priority = 0
        }

        type BinOp = base.BinOp[AST.Expr]
        type Neg = base.Neg[AST.Expr]
        type IfThenElse = base.IfThenElse[AST.Expr, AST.BooleanExpr]
        type And = base.And[AST.BooleanExpr]
        type Or = base.Or[AST.BooleanExpr]
        type Not = base.Not[AST.BooleanExpr, AST.Expr]
        type Condition = base.Condition[AST.Expr]

        trait Less extends Printable {
            def toScala = "<"
        }
        trait LessEqual extends Printable {
            def toScala = "<="
        }
        trait Greater extends Printable {
            def toScala = ">"
        }
        trait GreaterEqual extends Printable {
            def toScala = ">="
        }
        trait Equal extends Printable {
            def toScala = "="
        }
        trait NotEqual extends Printable {
            def toScala = "<>"
        }

        trait SimpleType extends Printable {
            self: AST.SimpleType =>
            def toScala = name
        }

        trait UnitType extends Printable {
            def toScala = "()"
        }

        trait TupleType extends Printable {
            self: AST.TupleType =>
            def toScala = pars(types.mkString(","))
        }

        trait FunctionType extends Printable {
            self: AST.FunctionType =>
            def toScala = s"$arg_type => $ret_type"
        }
    }

    object types {

        trait Unit extends ast.UnitType

        trait `Float` extends Printable {
            def toScala = "Float"
        }

        trait `Boolean` extends Printable {
            def toScala = "Boolean"
        }

        trait Tuple extends Printable {
            self: Types.Tuple =>
            def toScala = pars(elems.mkString(","))
        }

        trait Function extends Printable {
            self: Types.Function =>
            def toScala = (if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
        }
    }

    object typed {

        trait Parameter extends base.Parameter {
            self: Typed.Parameter =>
            val annotations : List[Annotation] = Nil
            def printType = " : " + ty
            def printInitializer = prefixedIfSome(initializer, " = ")
        }

        trait Annotation extends base.Annotation {
            self: Typed.Annotation =>
            def getName = target.name
        }

        trait Function extends base.Function {
            self: Typed.Function =>
            def printRetType = " : " + ret_type
            def printBody = prefixedIfSome(body, crlf + tab + " = ")
        }


        type Expr = ast.Expr
        type BooleanExpr = ast.BooleanExpr

        type BinOp = base.BinOp[Typed.ArithExpr]
        type Neg = base.Neg[Typed.ArithExpr]

        type IfThenElse = base.IfThenElse[Typed.ArithExpr, Typed.BooleanExpr]
        type And = base.And[Typed.BooleanExpr]
        type Or = base.Or[Typed.BooleanExpr]
        type Not = base.Not[Typed.BooleanExpr, Typed.ArithExpr]
        type Condition = base.Condition[Typed.ArithExpr]

        trait FloatConst extends Expr {
            self: Typed.FloatConst =>
            def toScala = x.toString
            val priority = 0
        }

        trait ParamRef extends Expr {
            self: Typed.ParamRef =>
            def toScala = p.name
            val priority = 0
        }

        trait FunCall extends Expr {
            self: Typed.FunctionCall =>
            def toScala = target.name + arguments.map({ _._2 }).mkString("(",",",")")
            val priority = 0
        }
    }
}

