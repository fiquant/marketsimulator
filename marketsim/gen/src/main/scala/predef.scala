package object predef {

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

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

        def apply(f : => Any) : String = apply()("\r\n" + get + f)
    }

    val indent = new Indent()

    def crlf = "\r\n" + indent.get

    abstract class Code
    {
        def toString : String

        def | (t : Code) : Code = new Combine(new Combine(this, nl), t)
        def |>(t : Code) : Code = new Combine(this, new Block(t))
    }

    object Code
    {
        def from(lst : List[Code], sep : Code = nl) : Code = lst match {
            case Nil => stop
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
        override def toString = indent(inner)
    }

    val nl = new NewLine
    val stop = new Stop

    class Combine(x : Code, y : Code) extends Code
    {
        override def toString = x.toString + y.toString
    }

    class LazyString(s : => String) extends Code {

        override def toString = s
    }

    implicit def toLazy(s : => String) = new LazyString(s)
}

