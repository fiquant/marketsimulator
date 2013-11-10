import sun.reflect.annotation.ExceptionProxy

case class Typer(n : NameTable.Impl)
{
    def get = {
        val ret = n.names.foldLeft(TypeTable())({
            case (acc, (name, definition)) =>
                if (acc contains name) {
                    throw new Exception(s"Function $name is already typed")
                } else {
                    acc.updated(name, definition.ret_type match {
                        case Some(t) => {
                            val arg_types = definition.parameters.foldLeft(List[(String, Types.Base)]()) {
                                (locals, p) =>
                                    if (locals contains p.name)
                                        throw new Exception(s"In function ${definition.name} duplicate parameter ${p.name}")
                                    locals :+ (p.name, p.initializer match {
                                        case Some(e) =>
                                            val ini_type = TypeChecker(acc, locals.toMap)(e)
                                            if (p.ty.nonEmpty) {
                                                val decl_type = Types.fromAST(p.ty.get)
                                                if (decl_type != ini_type) {
                                                    throw new Exception(s"In function ${definition.name} inferred type $ini_type "
                                                                      + s"doesn't match to the declared type $decl_type")
                                                } // TODO: support casts
                                                decl_type
                                            } else {
                                                ini_type
                                            }
                                        case None =>
                                            if (p.ty.nonEmpty)
                                                Types.fromAST(p.ty.get)
                                            else
                                                throw new Exception(s"parameter ${p.name} of function ${definition.name} has undefined type")
                                    })
                            }
                            Types.Function(arg_types map {_._2}, Types.fromAST(t))
                        }
                        case None => throw new Exception(s"Return type for function $name should be given explicitly")
                    })
                }
        })


        ret
    }
}
