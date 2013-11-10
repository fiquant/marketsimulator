case class Typer(n : NameTable.Impl)
{
    def get = {
        val ret = n.names.foldLeft(Map[String, Types.Function]())({
            case (acc, (name, definition)) =>
                if (acc.contains(name)) {
                    throw new Exception(s"Function $name is already typed")
                } else {
                    acc.updated(name, definition.ret_type match {
                        case Some(t) => {
                            val arg_types = definition.parameters map { _.ty.get } map Types.fromAST
                            val checker = TypeChecker(TypeTable(acc), Map[String, Types.Base]())
                            val inis = definition.parameters map { _.initializer.get } map { checker(_) }
                            Types.Function(arg_types, Types.fromAST(t))
                        }
                        case None => throw new Exception(s"Return type for function $name should be given explicitly")
                    })
                }
        })


        TypeTable(ret)
    }
}
