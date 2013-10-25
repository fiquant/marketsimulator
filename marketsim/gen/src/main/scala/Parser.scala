import java.io.PrintWriter
import scala.annotation.tailrec
import scala.collection.mutable
import scala.util.parsing.combinator._
import resource._

sealed abstract class Expr
case class Const(value: Double) extends Expr
case class Var(s : String) extends Expr
case class Add(x: Expr, y: Expr) extends Expr
case class Sub(x: Expr, y: Expr) extends Expr
case class Mul(x: Expr, y: Expr) extends Expr
case class Div(x: Expr, y: Expr) extends Expr
case class Neg(x: Expr) extends Expr

case class Memoize[A,B](f: A => B) extends (A => B) {
    private val cache = mutable.Map.empty[A, B]
    def apply(x: A) = cache getOrElseUpdate (x, f(x))
}

object PrettyPrinter {

    val tab = "   "

    private val tabs: Memoize[Int, String] = Memoize {
        case 0 => ""
        case n => tabs(n - 1) + tab
    }

    def tabify(n : Int, s : String) = List(tabs(n) + s)

    def braces(n : Int, name : String, e : Expr) =
        tabify(n, name)  :::
            apply(e, n + 1)

    def braces(n : Int, name : String, e1 : Expr, e2 : Expr) =
        tabify(n, name)  :::
            apply(e1, n + 1)   :::
            apply(e2, n + 1)

    def apply(e : Expr, n : Int = 0) : List[String] = e match {
        case Var(s) => tabify(n, s)
        case Const(x) => tabify(n, x.toString)
        case Neg(x) => braces(n,"Neg", x)
        case Add(x,y) => braces(n,"Add", x, y)
        case Sub(x,y) => braces(n,"Sub", x, y)
        case Mul(x,y) => braces(n,"Mul", x, y)
        case Div(x,y) => braces(n,"Div", x, y)
    }

}

object Parser extends JavaTokenParsers {
    def expr : Parser[Expr] = factor ~ rep(("+" | "-") ~ factor) ^^ {
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
                val parsed = parseAll(expr, line)
                val pretty_printed = PrettyPrinter(parsed.get, 3).mkString("\n")
                output.println(s"$pretty_printed\n\n")
            }
        }
    }
}

