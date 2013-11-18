case class Typer(n : NameTable.Impl)
{
    var globals = TypeTable()
    val grey_set = scala.collection.mutable.Stack[String]()

    def all =
        try {
            n.names.foreach({ case (name, definition) => get(name) })
            globals
        } catch {
            case e : Exception =>
                println("An error occurred during typing:")
                println(e.getMessage)
                globals
        }

    def get(name : String) = {
        val (f, g) = globals.getOrElseUpdated(name, {
            val definition = n getFunDef name

            try {
                // checking that there are no recursive calls
                if (grey_set contains definition.name)
                    throw new Exception("Cycle detected in function definitions: " + grey_set.mkString("->"))
                grey_set.push(definition.name)

                val ty = toTyped(definition)

                grey_set.pop()
                ty
            } catch {
                case ex : Exception =>
                    throw new Exception(s"\r\nWhen typing function '${definition.name}':\r\n" + ex.getMessage)
            }
        })
        globals = g
        f
    }

    def get(name : AST.QualifiedName) : Typed.Function = get(name.toString)

    def toTyped(definition: AST.FunDef): Typed.Function = {
        def inferType(locals: List[Typed.Parameter])(e: AST.Expr) = {
            val ctx = new TypingExprCtx {
                def lookupFunction(name: AST.QualifiedName) = get(name)

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
                locals :+ toTyped(p, inferType(locals))
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
                                + s" $b doesn't match to declared return type $ret_type")
                    case _ =>
                }
                ret_type

            case None =>
                def deref[A](x: Option[A], fail_msg: => Exception): A =
                    if (x.nonEmpty) x.get else throw fail_msg
                deref(body_type, new Exception(s"Return type for should be given explicitly"))
        }
        val ty = Typed.Function(Typed.globals, definition.name, locals, ret_type, body,
            definition.docstring, definition.annotations map toTyped)
        ty
    }

    def toTyped(p: AST.Parameter, inferType : AST.Expr => Typed.Expr)= {
        try {
            p.initializer match {
                case Some(e) =>
                    val initializer = inferType(e)
                    if (p.ty.nonEmpty) {
                        val decl_type = Types.fromAST(p.ty.get)
                        if (decl_type != initializer.ty) {
                            throw new Exception(s"Inferred type of $initializer "
                                    + s"doesn't match to the declared type $decl_type")
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

    def toTyped(a : AST.Annotation)  =
        Typed.Annotation(Typed.Annotations.lookup(a.name.toString), a.parameters)
}
