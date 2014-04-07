package object predef {

    def pars(s : Any, condition : Boolean) : String =
        if (condition) "(" + s + ")" else s.toString

    def pars(s : Any) : String = pars(s, condition = true)
    def pars(s : Code) : Code = pars(s, condition = true)

    def pars(s : Code, condition : Boolean) : Code =
        if (condition) toLazy("(") ||| s ||| toLazy(")") else s

    def ifSome[A](p : Option[A], prefix : String = "", postfix : String = "") =
        if (p.nonEmpty) prefix + p.get + postfix else ""

    class Indent() {
        var x : Int = 0
        var spaces = Map[Int, String]()

        def get = at(x)

        def at(i : Int) = {
            if (!(spaces contains i)) {
                spaces = spaces updated (i, " " * i)
            }
            spaces(i)
        }

        def apply(increment : Int = 4)(f : => Any) = {
            x += increment
            val e = f.toString
            x -= increment
            e
        }

        def apply(f : => Any) : String = apply()(f)
    }

    val indent = new Indent()

    def crlf = "\n" + indent.get



    abstract class Code
    {
        def toString : String

        def imports : Stream[Importable] = Nil.toStream

        def ||| (t : Code) : Code = new Combine(this, t)
        def ||| (t : => String) : Code = new Combine(this, new LazyString(t))
        def |   (t : Code) : Code = this ||| nl ||| t
        def |>  (t : Code) : Code = this ||| new Block(t)
    }

    trait Importable extends Code {
        def repr: String
    }


    case class Import(what: String) extends Code with Importable {
        override def imports = Stream(this)
        override def toString = ""
        def repr = s"import ${what.toLowerCase}"
    }
    case class ImportFrom(what: String, from: String) extends Code with Importable {
        override def imports = Stream(this)
        override def toString = ""
        def repr = s"from ${from.toLowerCase} import $what"
        def as(a : String) = ImportFromAs(what, from, a)
    }
    case class ImportFromAs(what: String, from: String, as : String) extends Code with Importable {
        override def imports = Stream(this)
        override def toString = ""
        def repr = s"from ${from.toLowerCase} import $what as $as"
    }

    object Code
    {
        def from(lst : List[Code], sep : Code = nl, default : Code = stop) : Code = lst match {
            case Nil => default
            case x :: Nil => x
            case x :: tl => new Combine(new Combine(x, sep), from(tl, sep))
        }
    }

    class NewLine extends Code
    {
        override def toString = crlf
    }

    class Stop extends Code
    {
        override def toString = ""
    }

    class Block(inner : Code) extends Code
    {
        override def toString = indent(crlf + inner)

        override def imports = inner.imports
    }

    class WithoutImports(inner : => Code) extends Code
    {
        override def toString = inner.toString
    }

    val nl = new NewLine
    val stop = new Stop

    def makeCodeString(xs : List[Code], sep : Code) : Code =  xs match {
        case Nil => stop
        case x :: Nil => x
        case x :: y => x ||| sep ||| makeCodeString(y, sep)
    }

    def makeCodeString(xs : List[Code], start : Code, sep : Code, stop : Code) : Code =
        start ||| makeCodeString(xs, sep) ||| stop


    class Combine(x : Code, y : Code) extends Code
    {
        override def toString = x.toString + y.toString

        override def imports = x.imports ++ y.imports
    }

    class LazyString(s : => String) extends Code {

        override def toString = s
    }

    implicit def toLazy(s : => String) = new LazyString(s)

    class Memoize1[-T, +R](f: T => R) extends (T => R) {
      import scala.collection.mutable
      private[this] val vals = mutable.Map.empty[T, R]

      def apply(x: T): R = {
        if (vals.contains(x)) {
          vals(x)
        }
        else {
          val y = f(x)
          vals += ((x, y))
          y
        }
      }
    }

    object Memoize1 {
      def apply[T, R](f: T => R) = new Memoize1(f)

        def Y[T, R](f: (T, T => R) => R) = {
           var yf: T => R = null
           yf = Memoize1(f(_, yf(_)))
           yf
         }
    }

    trait ScPrintable
    {
        protected def toScala : String
        override def toString = toScala
    }

    trait PyPrintable
    {
        def asCode : Code
    }

    trait ScPyPrintable extends ScPrintable with PyPrintable
    {
        def asScala = toScala
    }

}

