import java.io.PrintWriter
import resource._
import sext._
import AST._

object ExprTest extends Parser {

    def run() {

        for (input <- managed(io.Source.fromFile("test/expressions.in"));
             raw_output <- managed(new PrintWriter("test/expressions.raw"));
             pp_output <- managed(new PrintWriter("test/expressions.pp")))
        {
            for (line <- input.getLines()) {
                raw_output.println(s"$line ->")
                pp_output.println(s"$line ->")
                val (raw, pp) = parseAll(expr, line) match {
                    case Success(result : Expr, _) => {
                        val asTree = result.treeString
                        val pp = result.toString
                        parseAll(expr, line) match {
                            case Success(result2 : Expr, _) => {
                                if (result != result2) {
                                    println(s"input: $line")
                                    println(s"parsed: $result")
                                    println(s"re-parsed: $result2")
                                }
                            }
                            case x => println(x)
                        }
                        (s"$asTree\n\n", s"$pp\n\n")
                    }
                    case x => (x.toString, x.toString)
                }
                raw_output.println(raw)
                pp_output.println(pp)
            }

            val fd =
                """
                  | /**  Minimum
                  | */
                  | @ann("p1", "p2")
                  | @ann2("p")
                  | def min(@doc("X") x : (float,float) = 0,
                  |         @doc("Y") y : (float) = 0) =
                  |
                  |     if x < y then x else y
                  |
                  |/**  Maximum
                  | */
                  | def max(@doc("X") x : () = 0,
                  |         @doc("Y") y : float => () => (float) = 0) =
                  |
                  |     if x > y then x else y
                  |                """.stripMargin

            println(parseAll(definitions, fd))
        }
    }

}
