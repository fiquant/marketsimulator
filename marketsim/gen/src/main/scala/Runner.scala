import java.io.PrintWriter
import resource._
import sext._

object Runner extends syntax.scala.Parser {

    def parse(path : String) : Option[AST.Definitions] = {

        def printerFor(ext : String) = new PrintWriter(path.replace(".sc", ext).replace("defs", ".output"))

        (managed(io.Source fromFile path) and
         managed(printerFor(".raw")) and
         managed(printerFor(".pp")) map {

            case ((input, raw_output), pp_output) => Nil
                val in = input.mkString

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
    }



    def main(args: Array[String]) {

        println(generator.python.base.Annotations)

        ExprTest.run()

        val files = "random" :: "mathops" :: "misc" :: Nil

        val parsed = files.flatMap({ file => parse(s"defs/$file.sc") })

        val names = buildNames(parsed)

        val typed = buildTyped(names)

        generator.python.gen.apply(typed, "_out")


//        val python_definitions =fromAST(parsed)
//
//        for ((filename, definitions) <- python_definitions.groupBy({ _.filename }))
//        {
//            managed(new PrintWriter(filename)) map { py_output =>
//                py_output.print(definitions.head.prologue)
//                py_output.println(definitions.mkString("\r\n"))
//            }
//        }
    }

    def buildNames(parsed: List[AST.Definitions]) =
    {
        val names = NameTable.apply(parsed)

        for (output <- managed(new PrintWriter(".output/names.sc"))) {
            output.println(names)
        }

        val names_2 = NameTable(parse(".output/names.sc").get :: Nil)

        if (names_2 != names)
            throw new Exception("re-parsed names differ from original ones.")

        names
    }


    def buildTyped(names: NameTable.Scope)  = {
        val typed = Typer(names)

        for (output <- managed(new PrintWriter(".output/typed.sc"))) {
            output.println(typed)
        }

        val typed_2 = Typer(NameTable(parse(".output/typed.sc").get :: Nil))

        if (typed != typed_2)
            throw new Exception("re-parsed typed representation differs from the original one")

        typed
    }
}
