import java.io.{PrintWriter, File}
import resource._
import scala.util.matching.Regex
import sext._

object Runner extends syntax.scala.Parser {

    def parse(file : File) : Option[AST.Definitions] = {

        def parsedPath(file : File) = ".parsed/" + file

        val target_dir = parsedPath(file.getParentFile)

        mkdir(target_dir)

        val path = parsedPath(file)

        //println("parsing " + file.getPath)

        def printerFor(ext : String) = new PrintWriter(path.replace(".sc", ext))

        (managed(io.Source fromFile file) and
         managed(printerFor(".pretty-printed.sc")) and
         managed(printerFor(".raw")) map {

            case ((input, pp_output), raw_output) => Nil
                val in = input.mkString

                parseAll(definitions, in) match {
                    case Success(result, _) => {
                        val pp = result.toString
                        pp_output.println(pp)
                        parseAll(definitions, pp) match {
                            case Success(result2, _) => {
                                if (result != result2) {
                                    println(s"input: in")
                                    println(s"parsed: $result")
                                    println(s"re-parsed: $result2")
                                    managed(printerFor(".re-parsed.sc")) map
                                            { _.println(pp) }
                                }
                            }
                            case x => println(x)
                        }
                        raw_output.println(result.treeString)
                        Some(result)
                    }
                    case x =>
                        raw_output.println(x)
                        println(x)
                        None
                }
        }).either match {
            case Left(exceptions) => throw new Exception(exceptions map { _.toString } mkString predef.crlf)
            case Right(result)    => result
        }
    }


    def unused(a : Any) {}

    def getFileTree(f : File) : Stream[File] =
            f #:: (if (f.isDirectory) f.listFiles.toStream flatMap getFileTree
                                 else Stream.empty)

    def cleanUp(path : String) {
        getFileTree(new File(path)) foreach { _.delete() }
        mkdir(path)
    }

    def mkdir(name : String) {
        mkdir(new File(name))
    }


    def mkdir(dir: File) {
        if (!dir.exists()) {
            dir.mkdirs()
            if (!dir.exists())
                throw new Exception("cannot create directory " + dir.getName)
        }
    }

    case class Config(sources : List[File] = Nil)

    def main(args: Array[String]) {

        val parser = new scopt.OptionParser[Config]("gen") {
        head("FiQuant Strategy Definition Language compiler", "0.8")
        help("help") text "prints this usage text"
        arg[File]("<dir>...") unbounded() optional() action { (x, c) =>
            c.copy(sources = c.sources :+ x) } text "directories to process"
        }
        parser.parse(args, Config()) map { config =>
            unused(generator.python.gen.Annotations)

            cleanUp(".output")
            cleanUp(".parsed")
            cleanUp("_out")
            cleanUp("../_pub")

            Typed.withNewTopLevel({
                print(s"parsing...")

                val parsed = (config.sources flatMap   getFileTree)
                                            .filter  {  _.getName endsWith ".sc" }
                                            .flatMap {  parse }.toList

                println("done")

                val names = buildNames(parsed)

                val typed = buildTyped(names)

                generatePython(typed)
            })
        } getOrElse {
          // arguments are bad, error message will have been displayed
        }


    }


    def generatePython(typed: Typed.Package)
    {
        print("generating python code...")
        generator.python.gen.apply(typed, "_out", "../_pub")
        println("done")
    }

    def buildNames(parsed: List[AST.Definitions]) =
    {
        print("building name tables...")

        val names = NameTable.apply(parsed)

        val names_file = ".output/names.sc"
        val names_failed_file = ".output/names.failed.sc"

        for (output <- managed(new PrintWriter(names_file))) {
            output.println(names)
        }

        val names_2 = Typed.withNewTopLevel({
            NameTable.apply(parse(new File(names_file)).get :: Nil)
        })

        if (names_2 != names) {
            for (output <- managed(new PrintWriter(names_failed_file))) {
                output.println(names_2)
            }
            println(s"Re-parsed names differ from original ones. Compare files '$names_file' and '$names_failed_file'")
        }

        println("done")

        names
    }


    def buildTyped(names: NameTable.Scope)  = {
        print("typing...")

        val typed = Typer.apply(names)

        Typed.AfterTyping()

        val typed_file = ".output/typed.sc"
        val typed_failed_file = ".output/typed.failed.sc"

        for (output <- managed(new PrintWriter(typed_file))) {
            output.println(typed)
        }

        val typed_2 = Typed.withNewTopLevel({
            Typer.apply(NameTable.apply(parse(new File(typed_file)).get :: Nil))
        })

        if (typed != typed_2) {
            for (output <- managed(new PrintWriter(typed_failed_file))) {
                output.println(typed_2)
            }
            println(s"Re-parsed names differ from original ones. Compare files '$typed_file' and '$typed_failed_file'")
        }

        println("done")

        typed
    }
}
