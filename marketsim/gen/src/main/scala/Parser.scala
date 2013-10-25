import java.io.PrintWriter
import scala.collection.mutable
import scala.util.parsing.combinator._
import resource._
import sext._

sealed abstract class Expr
case class Const(value: Double) extends Expr
case class Var(s : String) extends Expr
case class Add(x: Expr, y: Expr) extends Expr
case class Sub(x: Expr, y: Expr) extends Expr
case class Mul(x: Expr, y: Expr) extends Expr
case class Div(x: Expr, y: Expr) extends Expr
case class Neg(x: Expr) extends Expr
case class IfThenElse(cond : BooleanExpr, x : Expr, y : Expr) extends Expr

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

    lazy val conditional : Parser[Expr] = ("if" ~> boolean) ~ ("then" ~> expr) ~ ("else" ~> expr) ^^ {
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
        case op ~ list => list.foldLeft(op) {
            case (x, op ~ y) => op(x, y)
        }
    }

    lazy val factor = term ~ rep(muldiv_op ~ term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, op ~ y) => op(x, y)
        }
    }
    lazy val term : Parser[Expr] = (
                floatingPointNumber ^^ { s => Const(s.toDouble) }
            |   ident ^^ { Var }
            |   "(" ~> expr <~ ")"
            |   "-" ~> term ^^ { Neg })

    def apply(input: String): Option[Expr] = parseAll(expr, input) match {
        case Success(result, _) => Some(result)
        case NoSuccess(_, _) => None
    }

    def main(args: Array[String]) {

        for (input <- managed(io.Source.fromFile("test/arithmetic.in"));
             output <- managed(new PrintWriter("test/arithmetic.out")))
        {
            for (line <- input.getLines) {
                output.println(s"$line ->")
                output.println(parseAll(expr, line) match {
                    case Success(result, _) =>  s"${result.treeString}\n\n"
                    case x => x.toString
                })
            }
        }
    }
}

