import java.io.PrintWriter
import resource._
import sext._

object ExprTest {

    def main(args: Array[String]) {

        for (input <- managed(io.Source.fromFile("test/expressions.in"));
             output <- managed(new PrintWriter("test/expressions.raw"));
             pp_output <- managed(new PrintWriter("test/expressions.pp")))
        {
            for (line <- input.getLines()) {
                output.println(s"$line ->")
                pp_output.println(s"$line ->")
                val (raw, pp) = Parser.parseAll(Parser.expr, line) match {
                    case Parser.Success(result : Expr, _) =>  (s"${result.treeString}\n\n", s"${PrettyPrinter(result)}\n\n")
                    case x => (x.toString, x.toString)
                }
                output.println(raw)
                pp_output.println(pp)
            }

            val fd =
                """
                  | /**  Minimum
                  | */
                  | @ann("p1", "p2")
                  | @ann2("p")
                  | def min(@doc("X") x : float = 0,
                  |         @doc("Y") y : float = 0) =
                  |
                  |     if x < y then x else y
                  |
                  |/**  Maximum
                  | */
                  | def max(@doc("X") x : float = 0,
                  |         @doc("Y") y : float = 0) =
                  |
                  |     if x > y then x else y
                  |                """.stripMargin

            println(Parser.parseAll(Parser.definitions, fd))
        }
    }

}
