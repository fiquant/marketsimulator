import java.io.File

package object config
{
    case class Config(sources : List[File] = Nil,
                      reparse : Boolean = false,
                      check_names : Boolean = false,
                      check_typed : Boolean = false,
                      skip_errors : Boolean = false)

    private var instance : Option[Config] = None

    def sources = instance.get.sources
    def reparse = instance.get.reparse
    def check_names = instance.get.check_names
    def check_typed = instance.get.check_typed
    def catch_errors = !instance.get.skip_errors

    def With(args: Array[String])(f : => Unit)
    {
        val parser = new scopt.OptionParser[Config]("gen")
        {
            head("FiQuant Strategy Definition Language compiler", "0.8")

            help("help") text "prints this usage text"

            opt[Unit]("reparse") action { (_, c) =>
                c.copy(reparse = true) } text "reparse pretty printed parsed files"

            opt[Unit]("check_names") action { (_, c) =>
                c.copy(check_names = true) } text "check that re-parsed names are equal to the original names"

            opt[Unit]("check_typed") action { (_, c) =>
                c.copy(check_typed = true) } text "check that re-parsed typed representation is equal to the original one"

            opt[Unit]("skip_errors") action { (_, c) =>
                c.copy(skip_errors = true) } text "for debug purpose don't catch exceptions"

            arg[File]("<dir>...") unbounded() optional() action { (x, c) =>
                c.copy(sources = c.sources :+ x) } text "directories to process"
        }
        parser.parse(args, Config()) map { config =>

            instance = Some(config)

            f

            instance = None
        }
    }
}
