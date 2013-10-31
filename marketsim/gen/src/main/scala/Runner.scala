import java.io.PrintWriter
import PyGen.ImportRandom
import resource._
import sext._

object Runner extends Parser {

    def main(args: Array[String]) {

        ExprTest.run()

        for (input <- managed(io.Source.fromFile("defs/random.sc"));
             raw_output <- managed(new PrintWriter("defs/random.raw"));
             pp_output <- managed(new PrintWriter("defs/random.pp"));
             raw_py_output <- managed(new PrintWriter("defs/random.py.raw")))
        {
            val in = input.mkString
            raw_output.println(s"$in ->")
            pp_output.println(s"$in ->")
            raw_py_output.println(s"$in ->")

            val (raw, pp, raw_py) = parseAll(definitions, in) match {
                case Success(result , _) => {
                    val pp = result.toString
                    parseAll(definitions, pp) match {
                        case Success(result2, _) => {
                            if (result != result2) {
                                println(s"input: in")
                                println(s"parsed: $result")
                                println(s"re-parsed: $result2")
                            }
                        }
                        case x => println(x)
                    }
                    val python = result.python
                    (result.treeString, pp, python.treeString)
                }
                case x => (x.toString, x.toString, x.toString)
            }

            raw_output.println(raw)
            pp_output.println(pp)
            raw_py_output.println(raw_py)
        }
    }

}
