import java.io.PrintWriter
import resource._
import sext._

object Runner extends Parser {

    def main(args: Array[String]) {

        ExprTest.run()

        for (input <- managed(io.Source.fromFile("defs/random.sc"));
             raw_output <- managed(new PrintWriter("defs/random.raw"));
             pp_output <- managed(new PrintWriter("defs/random.pp")))
        {
            val in = input.mkString
            raw_output.println(s"$in ->")
            pp_output.println(s"$in ->")

            val raw = parseAll(definitions, in) match {
                case Success(result, _) => result.treeString
                case x => x.toString
            }

            raw_output.println(raw)
            //pp_output.println(pp)
        }
    }

}
