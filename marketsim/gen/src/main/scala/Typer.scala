case class Typer(n : NameTable.Impl)
{
    var globals = TypeTable()

    n.names.foreach({ case (name, definition) => update(name, definition) })

    def get(name : String) =
        globals.types.getOrElse(name,
            update(name, n getFunDef name))

    def get(name : AST.QualifiedName) : Types.Function = get(name.toString)


    def update(name : String, definition : AST.FunDef) : Types.Function = {
        globals.types get name match {
            case Some(ty) => ty
            case None =>
                val ty = definition.ret_type match {
                    case Some(t) => {
                        val arg_types = definition.parameters.foldLeft(List[(String, Types.Base)]()) {
                            (locals, p) =>
                                if (locals contains p.name)
                                    throw new Exception(s"In function ${definition.name} duplicate parameter ${p.name}")
                                locals :+ (p.name, p.initializer match {
                                    case Some(e) =>
                                        val ini_type = TypeChecker(get, locals.toMap)(e)
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
                }
                globals = globals.updated(name,ty)
                ty
        }
    }
}
