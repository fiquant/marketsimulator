import java.io.{PrintWriter, File, FileInputStream, InputStreamReader}
import resource._
import scala.util.matching.Regex
import scala.util.parsing.input.{CharArrayReader, Reader, StreamReader}
import sext._

object Runner extends syntax.scala.Parser {

    var _currentFile : Option[String] = None

    protected def currentFile = _currentFile.get

    def parseAll[T](p: Parser[T], in: Reader[Char], filename : String): ParseResult[T] = {
        _currentFile = Some(filename)
        val ret = super.parseAll(p, in)
        _currentFile = None
        ret
    }



    def parse(file : File) : Option[AST.Definitions] = {

        if (config.verbose)
            println("\t" + file)

        def parsedPath(file : File) = ".parsed/" + file

        val target_dir = parsedPath(file.getParentFile)

        mkdir(target_dir)

        val path = parsedPath(file)

        //println("parsing " + file.getPath)

        def printerFor(ext : String) = new PrintWriter(path.replace(".sc", ext))

        (managed(new InputStreamReader(new FileInputStream(file))) and
         managed(printerFor(".pretty-printed.sc")) and
         managed(printerFor(".raw")) map {

            case ((input, pp_output), raw_output) => Nil

                parseAll(definitions, StreamReader(input), file.getPath) match {
                    case Success(result, _) => {
                        val pp = result.toString
                        pp_output.println(pp)
                        if (config.reparse)
                            parseAll(definitions, new CharArrayReader(pp.toArray, 0), "") match {
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

    def main(args: Array[String]) {

        config.With(args) {
            unused(generator.python.gen.Annotations)

            cleanUp("_out")
            cleanUp("../_pub")

            Typed.withNewTopLevel({
                print(s"parsing...")

                val parsed = (config.sources flatMap   getFileTree)
                                            .filter  {  _.getName endsWith ".sc" }
                                            .flatMap {  parse }.toList

                println("done")

                buildNames(parsed) map {
                    buildTyped(_) map generatePython
                }
            })
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

        NameTable.create(parsed) map { names =>
            val names_file = ".output/names.sc"
            val names_failed_file = ".output/names.failed.sc"

            for (output <- managed(new PrintWriter(names_file))) {
                output.println(names)
            }

            if (config.check_names)
            {
                Typed.withNewTopLevel({
                    NameTable.create(parse(new File(names_file)).get :: Nil)
                }) map { names_2 =>
                    if (names_2 != names) {
                        for (output <- managed(new PrintWriter(names_failed_file))) {
                            output.println(names_2)
                        }
                        println(s"Re-parsed names differ from original ones. Compare files '$names_file' and '$names_failed_file'")
                    }
                }
            }

            println("done")

            names
        }
    }


    def buildTyped(names: NameTable.Scope)  = {
        print("typing...")

        Typer.run(names) map { typed =>

            Typed.AfterTyping()

            val typed_file = ".output/typed.sc"
            val typed_failed_file = ".output/typed.failed.sc"

            for (output <- managed(new PrintWriter(typed_file))) {
                output.println(typed)
            }

            if (config.check_typed)
            {
                NameTable.create(parse(new File(typed_file)).get :: Nil) map { names_2 =>
                    Typed.withNewTopLevel({
                        Typer.run(names_2)
                    }) map { typed_2 =>
                        if (typed != typed_2) {
                            for (output <- managed(new PrintWriter(typed_failed_file))) {
                                output.println(typed_2)
                            }
                            println(s"Re-parsed names differ from original ones. Compare files '$typed_file' and '$typed_failed_file'")
                        }

                    }
                }
            }


            println("done")

            typed
        }

    }
}
