case class Typer(n : NameTable.Impl)
{
    var globals = TypeTable()
    val grey_set = scala.collection.mutable.Stack[String]()

    n.names.foreach({ case (name, definition) => update(name, definition) })

    def get(name : String) =
        globals.types.getOrElse(name,
            update(name, n getFunDef name))

    def get(name : AST.QualifiedName) : Typed.Function = get(name.toString)

    def update(name : String, definition : AST.FunDef) : Typed.Function =
    {
        def toTyped(p: AST.Parameter, inferType : AST.Expr => Types.Base): Typed.Parameter = {
            p.initializer match {
                case Some(e) =>
                    val ini_type = inferType(e)
                    if (p.ty.nonEmpty) {
                        val decl_type = Types.fromAST(p.ty.get)
                        if (decl_type != ini_type) {
                            throw new Exception(s"In function ${definition.name} inferred type $ini_type "
                                    + s"doesn't match to the declared type $decl_type")
                        } // TODO: support casts
                        Typed.Parameter(p.name, decl_type, None)
                    } else {
                        Typed.Parameter(p.name, ini_type, None)
                    }
                case None =>
                    if (p.ty.nonEmpty)
                        Typed.Parameter(p.name, Types.fromAST(p.ty.get), None)
                    else
                        throw new Exception(s"parameter ${p.name} of function ${definition.name} has undefined type")
            }
        }
        def findParam(locals : List[Typed.Parameter], n : String) = locals.find({ _.name == n }) match {
            case Some(p) => p
            case None => throw new Exception(s"Cannot lookup parameter $n in function $name")
        }
        def inferType(locals : List[Typed.Parameter])(e : AST.Expr) =
            TypeChecker(get, findParam(locals, _))(e)

        val emptyLocals = List[Typed.Parameter]()
        globals.types get name match {
            case Some(ty) => ty
            case None =>
                if (grey_set contains name)
                    throw new Exception("Cycle detected in function definitions: " + grey_set.mkString("->"))
                grey_set.push(name)
                val locals = definition.parameters.foldLeft(emptyLocals) {
                    (locals, p) =>
                        if (locals contains p.name)
                            throw new Exception(s"In function ${definition.name} duplicate parameter ${p.name}")
                        locals :+ toTyped(p, inferType(locals))
                }
                val body_type = definition.body map inferType(locals)  map {
                    case Types.Function(_, rt) => rt
                    case x => throw new Exception("don't know for the moment what to do with expr of type " + x)
                }

                val ret_type = definition.ret_type match {
                    case Some(r) => {
                        val ret_type = Types.fromAST(r)
                        if (body_type.nonEmpty) {
                            if (body_type.get != ret_type)
                                throw new Exception(s"In function ${definition.name} inferred return type"
                                        + s" ${body_type.get} doesn't match to declared return type $ret_type")
                        }
                        ret_type
                    }
                    case None =>
                        if (body_type.nonEmpty) body_type.get else
                            throw new Exception(s"Return type for function $name should be given explicitly")
                }
                grey_set.pop()
                val ty = Typed.Function(name, locals, ret_type)
                globals = globals.updated(name,ty)
                ty
        }
    }
}
