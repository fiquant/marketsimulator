case class Names(names : Map[String, AST.FunDef]) {

    override def toString = names mkString "\r\n"

}

object Names {

    def create(p : List[AST.Definitions]) : Names =
    {
        val grouped = p flatMap { _.definitions groupBy { _.name } }

        val res = (grouped flatMap {
            case (name, d :: Nil) => Some(name -> d)
            case (name, lst) =>
                println(s"Duplicate definitions for $name:")
                println(lst.mkString("\r\n"))
                None
        }).toMap

        Names(res)
    }

}
