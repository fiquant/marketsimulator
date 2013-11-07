case class NameTable(names : Map[String, AST.FunDef]) {

    override def toString = names mkString "\r\n"

    def getFunDef(name : AST.QualifiedName) : AST.FunDef = {
        names get name.toString match {
            case Some(x) => x
            case None => throw new Exception(s"Cannot find name $name")
        }
    }
}

object NameTable {

    def create(p : List[AST.Definitions]) : NameTable =
    {
        val grouped = p flatMap { _.definitions groupBy { _.name } }

        val res = (grouped flatMap {
            case (name, d :: Nil) => Some(name -> d)
            case (name, lst) =>
                println(s"Duplicate definitions for $name:")
                println(lst.mkString("\r\n"))
                None
        }).toMap

        NameTable(res)
    }

}
