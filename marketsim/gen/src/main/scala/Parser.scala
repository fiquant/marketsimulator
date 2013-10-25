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
case class Less(x : Expr, y : Expr) extends BooleanExpr
case class LessEqual(x : Expr, y : Expr) extends BooleanExpr
case class Greater(x : Expr, y : Expr) extends BooleanExpr
case class GreaterEqual(x : Expr, y : Expr) extends BooleanExpr
case class Equal(x : Expr, y : Expr) extends BooleanExpr
case class NotEqual(x : Expr, y : Expr) extends BooleanExpr

case class Or(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
case class And(x : BooleanExpr, y : BooleanExpr) extends BooleanExpr
case class Not(x : BooleanExpr) extends BooleanExpr


case class Memoize[A,B](f: A => B) extends (A => B) {
    private val cache = mutable.Map.empty[A, B]
    def apply(x: A) = cache getOrElseUpdate (x, f(x))
}

object Parser extends JavaTokenParsers
{
    def expr : Parser[Expr] = conditional | arithmetic

    def conditional : Parser[Expr] = ("if" ~> boolean) ~ ("then" ~> expr) ~ ("else" ~> expr) ^^ {
        case (cond ~ x ~ y) => IfThenElse(cond, x, y)
    }

    def boolean : Parser[BooleanExpr] = boolean_factor ~ rep("or" ~ boolean_factor) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "or" ~ y) => Or(x, y)
        }
    }

    def logic_op = (
                "<>" ^^ { _ => NotEqual }
            |   "<=" ^^ { _ => LessEqual }
            |   "<"  ^^ { _ => Less }
            |   ">=" ^^ { _ => GreaterEqual }
            |   ">"  ^^ { _ => Greater }
            |   "="  ^^ { _ => Equal })

    def boolean_factor = boolean_term ~ rep("and" ~ boolean_term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "and" ~ y) => And(x, y)
        }
    }

    def boolean_term = (expr ~ logic_op ~ expr ^^ {
        case (x ~ op ~ y) => op(x, y)
    }
    | "not" ~> boolean ^^ { Not }
    | "(" ~> boolean <~ ")" )

    def arithmetic = factor ~ rep(("+" | "-") ~ factor) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "+" ~ y) => Add(x, y)
            case (x, "-" ~ y) => Sub(x, y)
        }
    }

    def factor = term ~ rep(("*" | "/") ~ term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "*" ~ y) => Mul(x, y)
            case (x, "/" ~ y) => Div(x, y)
        }
    }
    def term : Parser[Expr] = constant | variable | "(" ~> expr <~ ")" | negate
    def negate = "-" ~> term ^^ { s => Neg(s) }
    def variable = ident ^^ { s => Var(s) }
    def constant = floatingPointNumber ^^ { s => Const(s.toDouble) }

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

