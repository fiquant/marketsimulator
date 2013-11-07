case class TypeTable(types : Map[String, Types.Type]) {

    override def toString = types mkString "\r\n"
}

object TypeTable
{
    def create(n : NameTable) : TypeTable =
    {
        val ret = n.names.foldLeft(Map[String, Types.Type]())({
            case (acc, (name, definition)) =>
                if (acc.contains(name)) {
                    throw new Exception(s"Function $name is already typed")
                } else {
                    acc.updated(name, definition.ret_type match {
                        case Some(t) => Types.fromAST(t)
                        case None => throw new Exception(s"Return type for function $name should be given explicitly")
                    })
                }
        })


         TypeTable(ret)
    }
}
