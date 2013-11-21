package predef {

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

        def enter(increment : Int = 4)(f : => Any) = {
            x += increment
            val e = f.toString
            x -= increment
            e
        }
    }

}

