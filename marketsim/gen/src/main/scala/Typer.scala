object Typer
{
    private val visited = new {
        var grey_set = List[String]()

        def enter[T](name : String)(f : => T) =
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

    def apply(source : NameTable.Scope) =
    {
        source.typePackages
        Processor(source).run()
        source.typed.get
    }

    case class Processor(source : NameTable.Scope)
    {
        self =>
        // TODO: introduce fully qualified names in form .pkg1.pkgA.func
        //       in order to solve problem of hiding of top-level names by local ones

        def run() {
            try {
                source.members.values foreach { definition =>
                    try {
                        definition match {
                            case f : AST.FunDef => getTyped(f)
                            case t : AST.TypeDeclaration => getTyped(t)
                            case a : AST.TypeAlias => getTyped(a)
                        }
                    } catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '${definition.name}':\r\n" + ex.getMessage)
                    }
                }
                source.packages.values  foreach { Processor(_).run() }
            } catch {
                case e : Exception =>
                    println("An error occurred during typing:")
                    println(e.getMessage)
            }
        }

        private def getTyped(definition : AST.FunDef) = {
            source.typed.get.getOrElseUpdateFunction(definition.name, {
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }
            })
        }

        private def getTyped(definition : AST.TypeDeclaration) = {
            source.typed.get.getOrElseUpdateType(definition.name, {
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }
            })
        }

        private def getTyped(definition : AST.TypeAlias) = {
            source.typed.get.getOrElseUpdateType(definition.name, {
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }
            })
        }

        private def lookupFunction(name : AST.QualifiedName) : Typed.Function =
            source.lookupFunction(name.names) match {
                case Some((scope, definition)) => Processor(scope).getTyped(definition)
                case None => throw new Exception(s"cannot find name $name")
            }

        private def lookupType(name : AST.QualifiedName) : Types.UserDefined =
            source.lookupType(name.names) match {
                case Some((scope, definition)) => Processor(scope).getTyped(definition).ty
                case _ => throw new Exception(s"Unknown type $name")
            }




        private def toTyped(definition  : AST.TypeDeclaration) : Typed.TypeDeclaration =
        {
            val bases = definition.bases map toTyped
            val ty = Types.Interface(definition.name, source.typed.get, bases)
            Typed.TypeDeclaration(ty)
        }

        private def toTyped(definition  : AST.TypeAlias) : Typed.TypeDeclaration =
        {
            val ty = Types.Alias(definition.name, source.typed.get, toTyped(definition.target))
            Typed.TypeDeclaration(ty)
        }


        private def toTyped(t : AST.Type) : Types.Base = t match {
            case AST.SimpleType(AST.QualifiedName("Float" :: Nil)) => Types.`Float`
            case AST.SimpleType(AST.QualifiedName("Boolean" :: Nil)) => Types.`Boolean`
            case AST.SimpleType(name) => lookupType(name)
            case AST.UnitType => Types.Unit
            case AST.TupleType(types) => Types.Tuple(types map toTyped)
            case AST.FunctionType(arg_types, ret_type) => Types.Function(arg_types map toTyped, toTyped(ret_type))
        }

        private def toTyped(definition  : AST.FunDef): Typed.Function =
        {
            val target = source.typed.get

            def inferType(locals: List[Typed.Parameter])(e: AST.Expr) = {
                val ctx = new TypingExprCtx {
                    def lookupFunction(name: AST.QualifiedName) = self.lookupFunction(name)

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
            val ret_type = definition.ret_type map toTyped match {
                case Some(ret_type) =>
                    body_type match {
                        case Some(b) if b cannotCastTo ret_type =>
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

        private def toTyped(p: AST.Parameter, inferType : AST.Expr => Typed.ArithExpr) : Typed.Parameter = {
            try {
                p.initializer match {
                    case Some(e) =>
                        val initializer = inferType(e)
                        if (p.ty.nonEmpty) {
                            val decl_type = toTyped(p.ty.get)
                            if (initializer.ty cannotCastTo decl_type) {
                                throw new Exception(s"Inferred type of '$initializer': '${initializer.ty}' "
                                        + s"doesn't match to the declared type '$decl_type'")
                            } // TODO: support casts
                            Typed.Parameter(p.name, decl_type, Some(initializer), p.comment)
                        } else {
                            Typed.Parameter(p.name, initializer.ty, Some(initializer), p.comment)
                        }
                    case None =>
                        if (p.ty.nonEmpty)
                            Typed.Parameter(p.name, toTyped(p.ty.get), None, p.comment)
                        else
                            throw new Exception(s"parameter ${p.name} has undefined type")
                }
            } catch {
                case e: Exception =>
                    throw new Exception(s"When typing parameter '${p.name}'\r\n" + e.getMessage)
            }
        }

        private def toTyped(a : AST.Annotation) : Typed.Annotation =
            Typed.Annotation(Typed.Annotations.lookup(a.name.toString), a.parameters)

    }

}
