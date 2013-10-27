import java.io.PrintWriter
import resource._
import sext._

object ExprTest {

    def main(args: Array[String]) {

        for (input <- managed(io.Source.fromFile("test/expressions.in"));
             output <- managed(new PrintWriter("test/expressions.out")))
        {
            for (line <- input.getLines()) {
                output.println(s"$line ->")
                output.println(Parser.parseAll(Parser.expr, line) match {
                    case Parser.Success(result, _) =>  s"${result.treeString}\n\n"
                    case x => x.toString
                })
            }

            val fd =
                """
                  | /**  Minimum
                  | */
                  | def min(["X"] x : float = 0,
                  |         ["Y"] y : float = 0) =
                  |
                  |     if x < y then x else y
                """.stripMargin

            println(Parser.parseAll(Parser.fundef, fd))
        }
    }

}
