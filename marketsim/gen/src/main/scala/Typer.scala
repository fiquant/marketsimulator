object Typer
{
    private val visited = new {
        var grey_set = List[String]()

        def enter(name : String)(f : => Typed.Function) =
        {
            // checking that there are no recursive calls
            if (grey_set contains name)
                throw new Exception("Cycle detected in function definitions: " + grey_set.mkString("->"))

            grey_set = name :: grey_set

            val ty = f

            grey_set = grey_set.tail
            ty
        }
    }

    private def getTyped(source : NameTable.Scope, definition : AST.FunDef) = {
        source.typed.get.getOrElseUpdateFunction(definition.name, {
            try {
                visited.enter(definition.name) { toTyped(definition, source.typed.get, lookup(source) _ ) }
            } catch {
                case ex : Exception =>
                    throw new Exception(s"\r\nWhen typing function '${definition.name}':\r\n" + ex.getMessage)
            }
        })
    }

    private def lookup(source : NameTable.Scope)(name : AST.QualifiedName) : Typed.Function =
        source.lookupFunction(name.names) match {
            case Some((scope, definition)) => getTyped(scope, definition)
            case None => throw new Exception(s"cannot find name $name")
        }

    private def process(source : NameTable.Scope)
    {
        try {
            source.functions foreach { case (name, definition) => getTyped(source, definition) }
            source.packages  foreach { case (name, subpackage) => process(subpackage) }
        } catch {
            case e : Exception =>
                println("An error occurred during typing:")
                println(e.getMessage)
        }
    }

    def apply(source : NameTable.Scope) =
    {
        source.typePackages
        process(source)
        source.typed.get
    }


    private def toTyped(definition  : AST.FunDef,
                        target      : Typed.Package,
                        lookup      : AST.QualifiedName => Typed.Function): Typed.Function =
    {
        def inferType(locals: List[Typed.Parameter])(e: AST.Expr) = {
            val ctx = new TypingExprCtx {
                def lookupFunction(name: AST.QualifiedName) = lookup(name)

                def lookupVar(name: String) = locals.find({
                    _.name == name
                }) match {
                    case Some(p) => p
                    case None => throw new Exception(s"Cannot lookup parameter $name")
                }
            }
            TypeChecker(ctx)(e)
        }

        val emptyLocals = List[Typed.Parameter]()

        // inferring function parameter types and getting a typed representation for parameters
        val locals = definition.parameters.foldLeft(emptyLocals) {
            (locals, p) =>
                if (locals contains p.name)
                    throw new Exception(s"Duplicate parameter ${p.name}")
                locals :+ toTyped(p, inferType(locals) _)
        }

        // getting a typed representation for function body if any
        val body = definition.body map inferType(locals)
        val body_type = body map {
            _.ty match {
                case Types.Function(_, rt) => rt
                case x => throw new Exception(s"don't know for the moment what to do with expr of type '$x'\r\n" +
                        "Locals are: " + locals.mkString("[", ", ", "]"))
            }
        }

        // inferring type of the function from type of its body or using explicit specification
        val ret_type = definition.ret_type map Types.fromAST match {
            case Some(ret_type) =>
                body_type match {
                    case Some(b) if b != ret_type =>
                        throw new Exception(s"Inferred return type"
                                + s" '$b' doesn't match to declared return type '$ret_type'")
                    case _ =>
                }
                ret_type

            case None =>
                def deref[A](x: Option[A], fail_msg: => Exception): A =
                    if (x.nonEmpty) x.get else throw fail_msg
                deref(body_type, new Exception(s"Return type for should be given explicitly"))
        }
        Typed.Function(target, definition.name, locals, ret_type, body,
            definition.docstring, definition.annotations map toTyped)
    }

    private def toTyped(p: AST.Parameter, inferType : AST.Expr => Typed.Expr)= {
        try {
            p.initializer match {
                case Some(e) =>
                    val initializer = inferType(e)
                    if (p.ty.nonEmpty) {
                        val decl_type = Types.fromAST(p.ty.get)
                        if (decl_type != initializer.ty) {
                            throw new Exception(s"Inferred type of '$initializer': '${initializer.ty}' "
                                    + s"doesn't match to the declared type '$decl_type'")
                        } // TODO: support casts
                        Typed.Parameter(p.name, decl_type, Some(initializer))
                    } else {
                        Typed.Parameter(p.name, initializer.ty, Some(initializer))
                    }
                case None =>
                    if (p.ty.nonEmpty)
                        Typed.Parameter(p.name, Types.fromAST(p.ty.get), None)
                    else
                        throw new Exception(s"parameter ${p.name} has undefined type")
            }
        } catch {
            case e: Exception =>
                throw new Exception(s"When typing parameter '${p.name}'\r\n" + e.getMessage)
        }
    }

    private def toTyped(a : AST.Annotation)  =
        Typed.Annotation(Typed.Annotations.lookup(a.name.toString), a.parameters)
}
