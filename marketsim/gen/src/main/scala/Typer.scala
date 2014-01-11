package object Typer
{
    trait TypingExprCtx
    {
        def lookupFunction(name : AST.QualifiedName) : Typed.Function
        def lookupVar(name : String) : Typed.Parameter
        def toTyped(t : AST.Type) : TypesBound.Base
    }

    private val visited = new {
        var grey_set = List[String]()

        def enter[T](name : AST.QualifiedName)(f : => T) =
        {
            // checking that there are no recursive calls
            if (grey_set contains name)
                throw new Exception("Cycle detected in function definitions: " + grey_set.mkString("->"))

            grey_set = name.toString :: grey_set

            val ty = f

            grey_set = grey_set.tail
            ty
        }
    }

    def apply(source : NameTable.Scope) =
    {
        source.toTyped(Typed.topLevel)
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
                            case a : AST.FunAlias => getTyped(a)
                            case f : AST.FunDef => getTyped(f)
                            case t : AST.TypeDeclaration => getTyped(t)
                            case _ => throw new Exception("cannot type a member: " + definition)
                        }
                    }
                    catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '${source qualifyName definition.name}':\r\n" + ex.getMessage, ex)
                    }
                }
                (source.packages.values ++ source.anonymous) foreach { Processor(_).run() }
            }
            catch {
                case e : Exception =>
                    println("An error occurred during typing:")
                    println(e.getMessage)
            }
        }

        private def getTyped(definition : AST.FunAlias) : Typed.FunctionAlias = {
            source.typed.get.getOrElseUpdateFunctionAlias(definition.name, {
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }
            })
        }

        private def getTyped(definition : AST.FunDef) : Typed.Function = {
            source.typed.get.getOrElseUpdateFunction(definition.name, {
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }
            })
        }

        private def getTyped(definition : AST.TypeDeclaration) : Typed.TypeDeclaration = {
            source.typed.get getOrElseUpdateType (definition.name, {
                    visited.enter(source qualifyName definition.name) {
                        definition match {
                            case t : AST.Interface => toTyped(t)
                            case t : AST.Alias => toTyped(t)
                        }
                    }
            })
        }

        private def lookupFunction(name : AST.QualifiedName) : Typed.Function =
            source lookupFunction name.names match {
                case Some((scope, definition)) => Processor(scope).getTyped(definition)
                case None =>
                    source lookupFunctionAlias name.names match {
                        case Some((scope, definition)) => lookupFunction(definition.target)
                        case None => throw new Exception(s"cannot find name $name")
                    }
            }

        private def lookupType(name : AST.QualifiedName) : Typed.TypeDeclaration =
            source lookupType name.names match {
                case Some((scope, definition)) => Processor(scope).getTyped(definition)
                case None => Typed.topLevel.types get name.toString match {
                    case Some(t) => t
                    case None => throw new Exception(s"Unknown type $name")
                }

            }




        private def toTyped(definition  : AST.Interface) : Typed.InterfaceDecl =
        {
            Typed.InterfaceDecl(definition.name,
                            source.typed.get,
                            definition.bases map { toUnbound(definition.generics) },
                            definition.generics.elems map { TypesUnbound.Parameter })
        }

        private def toTyped(definition  : AST.Alias) : Typed.AliasDecl =
        {
            Typed.AliasDecl(definition.name,
                        source.typed.get,
                        toUnbound(definition.generics)(definition.target),
                        definition.generics.elems map { TypesUnbound.Parameter })
        }


        private def toUnbound(g : AST.Generics)(t : AST.Type) : TypesUnbound.Base = t match {

            case AST.SimpleType(name, genericArgs) =>
                if (name.names.length == 1 && (g.elems contains name.names(0)))
                    TypesUnbound.Parameter(name.names(0))
                else
                    lookupType(name).resolveGenerics(genericArgs map { toUnbound(g) })

            case AST.UnitType => TypesUnbound.Unit
            case AST.TupleType(types) => TypesUnbound.Tuple(types map toUnbound(g))
            case AST.FunctionType(arg_types, ret_type) => TypesUnbound.Function(arg_types map toUnbound(g), toUnbound(g)(ret_type))
        }

        private def toBound(t : AST.Type) : TypesBound.Base = t match {
            case x : AST.SimpleType =>
                val unbound = toUnbound(AST.Generics(Nil))(x).asInstanceOf[TypesUnbound.UserDefined]
                unbound.bind(TypesUnbound.TypeMapper(unbound.decl, x.genericArgs map { toBound }))
            case x =>
                toUnbound(AST.Generics(Nil))(x).bind(TypesUnbound.EmptyTypeMapper_Bound)
        }

        private def toTyped(definition  : AST.FunDef): Typed.Function =
        {
            val target = source.typed.get

            def inferType(locals: List[Typed.Parameter])(e: AST.Expr) = {
                val ctx = new TypingExprCtx {
                    def toTyped(t : AST.Type) = self.toBound(t)

                    def lookupFunction(name: AST.QualifiedName) = self.lookupFunction(name)

                    def lookupVar(name: String) = locals.find({
                        _.name == name
                    }) match {
                        case Some(p) => p
                        case None => throw new Exception(s"Cannot lookup parameter $name")
                    }
                }
                TypeChecker(ctx).asArith(e)
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
            val body_type = body map { _.ty }

            // inferring type of the function from type of its body or using explicit specification
            val ty = definition.ty map toBound match {
                case Some(decl_type) =>
                    body_type match {
                                case Some(b) if b cannotCastTo decl_type =>
                                    throw new Exception(s"Inferred return type"
                                            + s" '$b' doesn't match to declared return type '$decl_type'")
                                case _ =>
                            }
                    decl_type

                case None =>
                    def deref[A](x: Option[A], fail_msg: => Exception): A =
                        if (x.nonEmpty) x.get else throw fail_msg
                    deref(body_type, new Exception(s"Return type for $definition should be given explicitly"))
            }
            Typed.Function(target, definition.name, locals, ty, body,
                definition.docstring, annotationsOf(definition), attributesOf(definition))
        }

        private def toTyped(f : AST.FunAlias) : Typed.FunctionAlias =
            Typed.FunctionAlias(source.typed.get, f.name, lookupFunction(f.target))


        private def toTyped(p: AST.Parameter, inferType : AST.Expr => Typed.Expr) : Typed.Parameter = {
            try {
                p.initializer match {
                    case Some(e) =>
                        val initializer = inferType(e)
                        val ty = if (p.ty.nonEmpty) {
                            val decl_type = toBound(p.ty.get)
                            if (initializer.ty cannotCastTo decl_type) {
                                throw new Exception(s"Inferred type of '$initializer': '${initializer.ty}' "
                                        + s"doesn't match to the declared type '$decl_type'")
                            }
                            decl_type
                        } else {
                            TypesBound.Optional(initializer.ty)
                        }
                        Typed.Parameter(p.name, ty, Some(initializer), p.comment)
                    case None =>
                        if (p.ty.nonEmpty)
                            Typed.Parameter(p.name, toBound(p.ty.get), None, p.comment)
                        else
                            throw new Exception(s"parameter ${p.name} has undefined type")
                }
            }
            catch {
                case e: Exception =>
                    throw new Exception(s"When typing parameter '${p.name}'\r\n" + e.toString, e)
            }
        }

    }

    def annotationsOf(definition : AST.FunDef) = definition.decorators collect toTypedAnnotation

    def attributesOf(definition : AST.FunDef) = Typed.Attributes((definition.decorators collect toTypedAttribute).toMap)

    private val toTypedAnnotation : PartialFunction[AST.Decorator, Typed.Annotation] = {
        case a :  AST.Annotation => Typed.Annotation(Typed.Annotations.lookup(a.name.toString), a.parameters)
    }

    private val toTypedAttribute : PartialFunction[AST.Decorator, (String,String)] = {
        case AST.Attribute(name, value) => (name, value)
    }

    case class TypeChecker(ctx : TypingExprCtx)
    {
        def asBoolean(e : AST.BooleanExpr) : Typed.Expr = e match {
            case AST.And(x, y) => Typed.And(asBoolean(x), asBoolean(y))
            case AST.Or(x, y) => Typed.Or(asBoolean(x), asBoolean(y))
            case AST.Not(x) => Typed.Not(asBoolean(x))
            case AST.Condition(symbol, x, y) =>
                promote_opt(Typed.Condition(symbol, asArith(x), asArith(y)))
        }

        def promote_literal(e : Typed.Expr) =
            if (e.ty == Typed.topLevel.float_) {
                val f = ctx.lookupFunction(AST.QualifiedName("const" :: Nil))
                Typed.FunctionCall(Typed.FunctionRef(f), (f.parameters(0), e) :: Nil)
            } else e

        def promote_opt(e : Typed.Expr) =
            if (e.ty canCastTo Typed.topLevel.floatFunc) e match {
                case Typed.BinOp(c, x, y) => Typed.BinOp(c, promote_literal(x), promote_literal(y))
                case Typed.IfThenElse(cond, x, y) => Typed.IfThenElse(cond, promote_literal(x), promote_literal(y))
                case x => x
            } else e match {
                case Typed.Condition(symbol, x, y) =>
                    Typed.Condition(symbol, promote_literal(x), promote_literal(y))
                case x => x
            }



        def asArith(e : AST.Expr) : Typed.Expr = e match {
            case AST.BinOp(c, x, y) =>
                promote_opt(Typed.BinOp(c, asArith(x), asArith(y)))

            case AST.Neg(x) => Typed.Neg(asArith(x))

            case AST.Cast(x, ty) => Typed.Cast(asArith(x), ctx toTyped ty)

            case AST.IfThenElse(cond, x, y) =>
                promote_opt(Typed.IfThenElse(asBoolean(cond), asArith(x), asArith(y)))

            case AST.FloatLit(d) => Typed.FloatLit(d)
            case AST.StringLit(x) => Typed.StringLit(x)
            case AST.IntLit(x) => Typed.IntLit(x)
            case AST.Var(name) => Typed.ParamRef(ctx.lookupVar(name))

            case AST.FunCall(name, arg_lists) =>
                val args = arg_lists(0)
                val fun_type = ctx lookupFunction name
                if (args.length < fun_type.ty.mandatory_arg_count)
                    throw new Exception(s"Function $name is called with $args but it" +
                            s"should be called with at least ${fun_type.ty.mandatory_arg_count} arguments")
                val actual_args = args zip fun_type.parameters map {
                    case (actual, declared) =>
                        val typed = asArith(actual)
                        if (typed.ty cannotCastTo declared.ty)
                            throw new Exception(s"Function '$name' is called with wrong argument of"+
                                                s" type '${typed.ty}' when type '${declared.ty}' is expected")
                        (declared, typed)
                }
                Typed.FunctionCall(Typed.FunctionRef(fun_type), actual_args)
        }

    }

}
