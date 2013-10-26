import java.io.PrintWriter
import resource._
import sext._

object ExprTest {

    def main(args: Array[String]) {

        for (input <- managed(io.Source.fromFile("test/arithmetic.in"));
             output <- managed(new PrintWriter("test/arithmetic.out")))
        {
            for (line <- input.getLines) {
                output.println(s"$line ->")
                output.println(Parser.parseAll(Parser.expr, line) match {
                    case Parser.Success(result, _) =>  s"${result.treeString}\n\n"
                    case x => x.toString
                })
            }
        }
    }

}
