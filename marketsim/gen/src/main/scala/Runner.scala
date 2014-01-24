import java.io.{PrintWriter, File}
import resource._
import scala.util.matching.Regex
import sext._

object Runner extends syntax.scala.Parser {

    def parse(file : File) : Option[AST.Definitions] = {

        val target_dir = new File(file.getPath.replace("defs", ".parsed")).getParentFile

        mkdir(target_dir)

        val path = file.getPath

        //println("parsing " + file.getPath)

        def printerFor(ext : String) = new PrintWriter(path.replace(".sc", ext).replace("defs", ".parsed"))

        (managed(io.Source fromFile path) and
         managed(printerFor(".raw")) and
         managed(printerFor(".1.sc")) map {

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

        unused(generator.python.gen.Annotations)

        cleanUp(".output")
        cleanUp(".parsed")
        cleanUp("_out")
        cleanUp("../_pub")

        Typed.withNewTopLevel({
            print(s"parsing...")

            val parsed = (getFileTree(new File("defs"))
                            filter  { _.getName endsWith ".sc" }
                            flatMap { parse }
                    ).toList

            println("done")

            val names = buildNames(parsed)

            val typed = buildTyped(names)

            generatePython(typed)
        })

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

        for (output <- managed(new PrintWriter(".output/names.sc"))) {
            output.println(names)
        }

        val names_2 = Typed.withNewTopLevel({
            NameTable.apply(parse(new File(".output/names.sc")).get :: Nil)
        })

        if (names_2 != names)
            throw new Exception("re-parsed names differ from original ones.")

        println("done")

        names
    }


    def buildTyped(names: NameTable.Scope)  = {
        print("typing...")

        val typed = Typer.apply(names)

        Typed.AfterTyping()

        for (output <- managed(new PrintWriter(".output/typed.sc"))) {
            output.println(typed)
        }

//        val typed_2 = Typed.withNewTopLevel({
//            Typer.apply(NameTable.apply(parse(new File(".output/typed.sc")).get :: Nil))
//        })

//        if (typed != typed_2)
//            throw new Exception("re-parsed typed representation differs from the original one")

        println("done")

        typed
    }
}
