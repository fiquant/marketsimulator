import generator.python.fromAST
import java.io.PrintWriter
import resource._
import sext._

object Runner extends Parser {

    def parse(path : String) : Option[AST.Definitions] =
        (managed(io.Source.fromFile(path)) and
         managed(new PrintWriter(path.replace(".sc", ".raw"))) and
         managed(new PrintWriter(path.replace(".sc", ".pp"))) map {

            case ((input, raw_output), pp_output) => Nil
                val in = input.mkString
                raw_output.println(s"$in ->")
                pp_output.println(s"$in ->")

                parseAll(definitions, in) match {
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
                        raw_output.println(result.treeString)
                        pp_output.println(pp)
                        Some(result)
                    }
                    case x =>
                        raw_output.println(x)
                        pp_output.println(x)
                        println(x)
                        None
                }
        }).opt.get

    def main(args: Array[String]) {

        ExprTest.run()

        val files = "random" :: "mathops" :: Nil

        val parsed = files.flatMap({ file => parse(s"defs/$file.sc") })

        val names = Names.create(parsed)

        println(names)

        val python_definitions =fromAST(parsed)

        for ((filename, definitions) <- python_definitions.groupBy({ _.filename }))
        {
            managed(new PrintWriter(filename)) map { py_output =>
                py_output.print(definitions.head.prologue)
                py_output.println(definitions.mkString("\r\n"))
            }
        }
    }

}
