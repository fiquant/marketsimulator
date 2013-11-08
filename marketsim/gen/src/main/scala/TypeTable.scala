package object TypeTable
{
    case class Impl(types : Map[String, Types.Base]) {

        override def toString = types mkString "\r\n"
    }

    def create(n : NameTable.Impl) : Impl =
    {
        val ret = n.names.foldLeft(Map[String, Types.Base]())({
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


         Impl(ret)
    }
}
