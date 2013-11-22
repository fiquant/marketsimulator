package object predef {

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

    class NewLine

    val nl = new NewLine

    class LazyString(s : => String) {

        def | (t : => String) = new LazyString(s + crlf + t)
        def | (t : => NewLine) = s + "\r\n"
        def |> (t : => Any) = new LazyString(s + indent(t))

        override def toString = s
    }

    implicit def toLazy(s : String) = new LazyString(s)
    implicit def fromLazy(s : LazyString) = s.toString
}

