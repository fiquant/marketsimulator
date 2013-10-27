import scala.collection.mutable
import scala.util.parsing.combinator._

case class Parameter(name : String, ty : Option[String], initializer: Option[Expr], annotations : List[Annotation])
case class Annotation(name : String, parameters : List[String])
case class FunDef(name : String, parameters : List[Parameter], body : Option[Expr], docstring : Option[String], annotations : List[Annotation])

sealed abstract class Expr
case class Const(value: Double) extends Expr
case class Var(s : String) extends Expr
case class Add(x: Expr, y: Expr) extends Expr
case class Sub(x: Expr, y: Expr) extends Expr
case class Mul(x: Expr, y: Expr) extends Expr
case class Div(x: Expr, y: Expr) extends Expr
case class Neg(x: Expr) extends Expr
case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr) extends Expr
case class FunCall(name : String, args : List[Expr]) extends Expr

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

case class Memoize[A,B](f: A => B) extends (A => B) {
    private val cache = mutable.Map.empty[A, B]
    def apply(x: A) = cache getOrElseUpdate (x, f(x))
}

object Parser extends JavaTokenParsers
{
    lazy val expr : Parser[Expr] = conditional | arithmetic

    lazy val conditional = ("if" ~> boolean) ~ ("then" ~> expr) ~ ("else" ~> expr) ^^ {
        case (cond ~ x ~ y) => IfThenElse(cond, x, y)
    }

    lazy val boolean : Parser[BooleanExpr] = boolean_factor ~ rep("or" ~ boolean_factor) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "or" ~ y) => Or(x, y)
        }
    }

    lazy val logic_op = (
                "<>" ^^ { _ => NotEqual }
            |   "<=" ^^ { _ => LessEqual }
            |   "<"  ^^ { _ => Less }
            |   ">=" ^^ { _ => GreaterEqual }
            |   ">"  ^^ { _ => Greater }
            |   "="  ^^ { _ => Equal })

    lazy val boolean_factor = boolean_term ~ rep("and" ~ boolean_term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "and" ~ y) => And(x, y)
        }
    }

    lazy val boolean_term = (expr ~ logic_op ~ expr ^^ { case (x ~ op ~ y) => op(x, y) }
                        | "not" ~> boolean ^^ { Not }
                        | "(" ~> boolean <~ ")" )

    lazy val addsub_op = "+" ^^ { _ => Add } | "-" ^^ { _ => Sub }
    lazy val muldiv_op = "*" ^^ { _ => Mul } | "/" ^^ { _ => Div }

    lazy val arithmetic = factor ~ rep(addsub_op ~ factor) ^^ {
        case start ~ list => list.foldLeft(start) {
            case (x, op ~ y) => op(x, y)
        }
    }

    lazy val factor = term ~ rep(muldiv_op ~ term) ^^ {
        case start ~ list => list.foldLeft(start) {
            case (x, op ~ y) => op(x, y)
        }
    }
    lazy val term : Parser[Expr] = (
                floatingPointNumber ^^ { s => Const(s.toDouble) }
            |   funcall
            |   ident ^^ { Var }
            |   "(" ~> expr <~ ")"
            |   "-" ~> term ^^ { Neg })

    lazy val funcall = ident ~ ("(" ~> repsep(expr, ",") <~ ")") ^^ {
        case name ~ list => FunCall(name, list)
    }

    lazy val parameter = rep(annotation) ~ ident ~ opt(":" ~> ident) ~ opt("=" ~> expr) ^^ {
        case (annotations ~ name ~ ty ~ initializer) => Parameter(name, ty, initializer, annotations)
    }

    lazy val function  = opt(comment) ~ rep(annotation) ~ ("def" ~> ident) ~ ("(" ~> repsep(parameter, ",") <~ ")") ~ opt("=" ~> expr) ^^ {
        case (docstring ~ annotations ~ name ~ parameters ~ body) => FunDef(name, parameters, body, docstring, annotations)
    }

    lazy val definitions = rep(function)

    lazy val comment = "/\\*(?:.|[\\n\\r])*?\\*/".r ^^ { _ stripPrefix "/*" stripSuffix "*/" stripMargin '*' }

    lazy val string = stringLiteral ^^ { _ stripPrefix "\"" stripSuffix "\"" }

    lazy val annotation = ("@" ~> ident) ~ ("(" ~> repsep(string, ",") <~ ")") ^^ {
        case (name ~ parameters) => Annotation(name, parameters)
    }
}

