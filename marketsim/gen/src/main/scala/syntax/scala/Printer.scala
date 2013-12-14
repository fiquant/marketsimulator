package syntax.scala

import predef._

package object Printer
{
    val tab = "\t"

    trait Printable {
        def toScala : String
    }

    object base {
        trait Expr extends Printable {
            val priority : Int

            def wrap(x : Expr, rhs : Boolean = false) =
                pars(x, need_brackets(x, rhs))

            def need_brackets(x : Expr, rhs : Boolean) =
                x.priority > priority || x.priority == priority && rhs
        }

        trait Priority_0 { val priority = 0 }
        trait Priority_1 { val priority = 1 }
        trait Priority_2 { val priority = 2 }
        trait Priority_3 { val priority = 3 }

        trait BinOpSymbol extends Printable {
            val priority : Int
        }

        trait Add extends BinOpSymbol with Priority_2 { def toScala = "+"   }
        trait Sub extends BinOpSymbol with Priority_2 { def toScala = "-"   }
        trait Mul extends BinOpSymbol with Priority_1 { def toScala = "*"   }
        trait Div extends BinOpSymbol with Priority_1 { def toScala = "/"   }

        trait BinOp[T <: Expr] extends Expr {
            val x, y : T
            val symbol : BinOpSymbol
            def toScala = wrap(x) + symbol + wrap(y, rhs = true)
            val priority = symbol.priority
        }

        trait Neg[T <: Expr] extends Expr with Priority_0 {
            val x : T
            def toScala = "-" + wrap(x)
        }

        trait CondSymbol

        trait IfThenElse[T, U <: BooleanExpr] extends Expr with Priority_3 {
            val x, y : T
            val cond : U
            def toScala = s"if $cond then $x else $y"
        }

        trait BooleanExpr

        trait Or[T <: BooleanExpr] extends BooleanExpr with Printable with Priority_2 {
            val x, y : T
            def toScala = s"$x or $y"
        }

        trait And[T <: BooleanExpr] extends BooleanExpr with Printable with Priority_1 {
            val x, y : T
            def wrap(z : T) = pars(z, z.isInstanceOf[Or[T]])
            def toScala = wrap(x) + " and " + wrap(y)
        }

        trait Not[T <: BooleanExpr, U <: Expr] extends BooleanExpr with Printable with Priority_0 {
            val x : T
            def wrap(z : T) = pars(z, !z.isInstanceOf[Condition[U]])
            def toScala = "not " + wrap(x)
        }

        trait Condition[T <: Expr] extends BooleanExpr with Printable with Priority_0 {
            val x, y : T
            val symbol : CondSymbol
            def toScala = x.toString + symbol + y
        }

        trait Definition

        trait Definitions[+T <: Definition] extends Printable {
            val definitions: List[T]
            def toScala = definitions.mkString(crlf)
        }

        trait DocString extends Printable {
            val brief    : String
            val detailed : List[String]
            def toScala =
                ("/** " + brief
                        + detailed.map({ crlf + " *" + _ }).mkString("") + crlf
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
            val comment : List[String]
            val name : String
            def printType : String
            def printInitializer : String
            
            def toScala =
                ((if (comment.nonEmpty) {
                    "/**" + comment.mkString(crlf + "  *") + "*/ "
                } else "")
                        + name
                        + printType
                        + printInitializer)
        }

        trait Package[+T <: Definition] extends Printable with Definition {
            val name : AST.QualifiedName
            val members : Definitions[T]

            def toScala = (
                    crlf + "package " + name + " {"
                    + indent() { members }
                    + crlf + "}")
        }

        trait TypeDeclaration extends Printable with Definition
        {
            val name : String
            val bases : List[Any]

            def toScala = crlf + "type " + name + (if (bases.isEmpty) "" else " : " + bases.mkString(", "))
        }

        trait TypeAlias extends Printable with Definition
        {
            val name : String
            val target : Any

            def toScala = crlf + s"type $name = $target"
        }

        trait Function extends Printable with Definition {
            val docstring : Option[DocString]
            val annotations : List[Annotation]
            val name : String
            val parameters : List[Parameter]
            def printRetType : String
            def printBody : String

            def toScala = {
                (crlf   + ifSome(docstring)
                        + annotations.map({_ + crlf}).mkString("")
                        + "def " + name
                        + indent(("def " + name).length + 1){
                                parameters.mkString("(", "," + crlf, ")") }
                        + printRetType
                        + indent(printBody))
            }
        }

        trait TypeBase

        trait UnitType extends Printable {
            def toScala = "()"
        }

        trait TupleType extends Printable {
            val elems : List[TypeBase]
            def toScala = pars(elems.mkString(","))
        }

        trait FunctionType extends Printable {
            val args : List[TypeBase]
            val ret : TypeBase
            def toScala = (if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
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
        type Definitions = base.Definitions[AST.Definition]
        type DocString = base.DocString
        type QualifiedName = base.QualifiedName
        type Package = base.Package[Definition]
        type TypeDeclaration = base.TypeDeclaration
        type TypeAlias = base.TypeAlias

        trait Annotation extends base.Annotation {
            self: AST.Annotation =>
            def getName  = name.toString
        }

        trait Function extends base.Function {
            self: AST.FunDef =>
            def printRetType = ifSome(ty, " : ")
            def printBody = ifSome(body, " = ")
        }

        trait Parameter extends base.Parameter {
            self: AST.Parameter =>
            def printType = ifSome(ty, " : ")
            def printInitializer = ifSome(initializer, " = ")
        }

        import base.Priority_0

        trait Const extends Expr with Priority_0 {
            self: AST.Const =>
            def toScala = value.toString
        }

        trait Var extends Expr with Priority_0 {
            self: AST.Var =>
            def toScala = s
        }

        trait FunCall extends Expr with Priority_0 {
            self: AST.FunCall =>
            def toScala = name + pars(args.mkString(","))
        }

        type BinOp = base.BinOp[AST.Expr]
        type Neg = base.Neg[AST.Expr]
        type IfThenElse = base.IfThenElse[AST.Expr, AST.BooleanExpr]
        type And = base.And[AST.BooleanExpr]
        type Or = base.Or[AST.BooleanExpr]
        type Not = base.Not[AST.BooleanExpr, AST.Expr]
        type Condition = base.Condition[AST.Expr]

        trait Less extends Printable        {   def toScala = "<"   }
        trait LessEqual extends Printable   {   def toScala = "<="  }
        trait Greater extends Printable     {   def toScala = ">"   }
        trait GreaterEqual extends Printable{   def toScala = ">="  }
        trait Equal extends Printable       {   def toScala = "="   }
        trait NotEqual extends Printable    {   def toScala = "<>"  }

        trait SimpleType extends Printable {
            self: AST.SimpleType =>
            def toScala = name.toString
        }

        type UnitType = base.UnitType
        type TypeBase = base.TypeBase
        type TupleType = base.TupleType
        type FunctionType = base.FunctionType
    }

    object types {

        type Base = base.TypeBase
        type Unit = base.UnitType

        trait `Float` extends Printable {  def toScala = "Float"   }
        trait `Boolean` extends Printable {def toScala = "Boolean" }

        type Tuple = base.TupleType
        type Function = base.FunctionType

        trait UserDefined extends Printable {
            val name : String
            val scope : Typed.Package

            def toScala = scope qualifyName name
        }
    }

    object typed {

        trait Parameter extends base.Parameter {
            self: Typed.Parameter =>
            def printType = " : " + ty
            def printInitializer = ifSome(initializer, " = ")
        }

        trait Annotation extends base.Annotation {
            self: Typed.Annotation =>
            def getName = target.name
        }

        trait Function extends base.Function {
            self: Typed.Function =>
            def printRetType = " : " + ret_type
            def printBody = ifSome(body, crlf + tab + " = ")
        }

        trait TypeDeclaration extends Printable
        {
            self: Typed.TypeDeclaration =>
            def toScala = ty match {
                case Types.Interface(name, _, bases) =>
                    s"type $name" + (if (bases.isEmpty) "" else " : " + bases.mkString(", "))

                case Types.Alias(name, _, target) =>
                    s"type $name = $target"

            }
        }


        type Expr = base.Expr
        type BooleanExpr = base.BooleanExpr

        type BinOp = base.BinOp[Typed.Expr]
        type Neg = base.Neg[Typed.Expr]

        type IfThenElse = base.IfThenElse[Typed.Expr, Typed.Expr]
        type And = base.And[Typed.Expr]
        type Or = base.Or[Typed.Expr]
        type Not = base.Not[Typed.Expr, Typed.Expr]
        type Condition = base.Condition[Typed.Expr]

        import base.Priority_0

        trait FloatConst extends Expr with Priority_0 {
            self: Typed.FloatConst =>
            def toScala = x.toString
        }

        trait ParamRef extends Expr with Priority_0 {
            self: Typed.ParamRef =>
            def toScala = p.name
        }

        trait FunCall extends Expr with Priority_0 {
            self: Typed.FunctionCall =>
            def toScala = target.parent.qualifyName(target.name) + arguments.map({ _._2 }).mkString("(",",",")")
        }

        trait TopLevelPackage extends Printable {
            def packages : Map[String, Any]
            def functions : Map[String, Any]
            def types : Map[String, Any]
            def content =
                (packages.values mkString crlf) +
                (types.values mkString crlf) +
                (functions.values mkString crlf)
            def wrapped(name : String) =
                crlf + s"package $name {" +
                    indent() { content } +
                crlf + "}"
            def toScala = content
        }

        trait SubPackage extends TopLevelPackage  {
            def name : String
            override def toScala = wrapped(name)
        }

        trait Scope extends TopLevelPackage

        trait NamesScope extends Printable {
            val name : String
            def packages : Map[String, Any]
            def members : Map[String, Any]
            def content =
                (packages.values mkString crlf) +
                (members.values mkString crlf)

            def wrapped(name : String) =
                crlf + s"package $name {" +
                        indent() { content } +
                        crlf + "}"

            def toScala = if (name == "_root_") content else wrapped(name)
        }

    }
}

