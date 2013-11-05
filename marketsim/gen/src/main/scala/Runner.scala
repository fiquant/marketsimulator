import java.io.PrintWriter
import resource._
import sext._

object Runner extends Parser {
    
    def getPythonDefinitions(path : String) : List[PyGen.Printer] =
        (managed(io.Source.fromFile(path)) and
         managed(new PrintWriter(path.replace(".sc", ".raw"))) and
         managed(new PrintWriter(path.replace(".sc", ".pp"))) and
         managed(new PrintWriter(path.replace(".sc", ".py.raw"))) map {

             case (((input, raw_output), pp_output), raw_py_output) => Nil
                 val in = input.mkString
                 raw_output.println(s"$in ->")
                 pp_output.println(s"$in ->")

                 val (raw, pp, raw_py, python_definitions) = parseAll(definitions, in) match {
                     case Success(result, _) => {
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
                 python_definitions

         }).opt.get

    def main(args: Array[String]) {

        ExprTest.run()

        val files = "random" :: "mathops" :: Nil

        val python_definitions = files.flatMap({ file => getPythonDefinitions(s"defs/$file.sc") })

        for ((filename, definitions) <- python_definitions.groupBy({ _.filename }))
        {
            managed(new PrintWriter(filename)) map { py_output =>
                py_output.print(definitions.head.prologue)
                py_output.println(definitions.mkString("\r\n"))
            }
        }
    }

}
