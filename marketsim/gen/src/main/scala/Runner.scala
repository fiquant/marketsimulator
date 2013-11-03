import java.io.PrintWriter
import PyGen.ImportRandom
import resource._
import sext._

object Runner extends Parser {
    
    def getPythonDefinitions(path : String) : List[PyGen.Printer] = 
    {
        var ret : List[PyGen.Printer] = Nil
        
        for (input <- managed(io.Source.fromFile(path));
             raw_output <- managed(new PrintWriter(path.replace(".sc", ".raw")));
             pp_output <- managed(new PrintWriter(path.replace(".sc", ".pp")));
             raw_py_output <- managed(new PrintWriter(path.replace(".sc", ".py.raw"))))
        {
            val in = input.mkString
            raw_output.println(s"$in ->")
            pp_output.println(s"$in ->")

            val (raw, pp, raw_py, python_definitions) = parseAll(definitions, in) match {
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
                    val randoms = PyGen.getRandoms(python)
                    (result.treeString, pp, randoms.treeString, randoms)
                }
                case x => (x.toString, x.toString, x.toString, List())
            }

            raw_output.println(raw)
            pp_output.println(pp)
            raw_py_output.println(raw_py)
            ret = python_definitions
        }
        ret
    }

    def main(args: Array[String]) {

        ExprTest.run()

        val python_definitions = getPythonDefinitions("defs/random.sc")

        for (py_output <- managed(new PrintWriter("defs/random.py")))
        {
            py_output.println(python_definitions.mkString("\r\n"))
        }
    }

}
