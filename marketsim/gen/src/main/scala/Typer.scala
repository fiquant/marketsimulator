package object Typer
{
    trait TypingExprCtx
    {
        def lookupFunction(name : AST.QualifiedName) : List[(TypesBound.Base, () => Typed.Expr)]
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

    def run(source : NameTable.Scope) =
    {
        source.toTyped(Typed.topLevel)
        Processor(source).run()
        source.typed
    }

    case class Processor(source : NameTable.Scope)
    {
        self =>

        def run() {
            if (config.verbose)
                println("\t" + source.qualifiedName)

            try {
                source.types.values foreach { t =>
                    try {
                        getTyped(t)
                    }
                    catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '${source qualifyName t.name}':\r\n" + ex.getMessage, ex)
                    }

                }

                source.functions.values foreach { _ foreach { definition =>
                    try {
                        definition match {
                            case a : AST.FunAlias => getTyped(a)
                            case f : AST.FunDef => getTyped(f)
                        }
                    }
                    catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '${source qualifyName definition.name}':\r\n" + ex.getMessage, ex)
                    }
                } }

                source.packages.values foreach { Processor(_).run() }
            } catch {
                case e : Exception =>
                    if (config.catch_errors) {
                        println(e.getMessage)
                    }
                    else throw e
            }
        }

        private def getTyped(definition : AST.FunAlias) : List[Typed.FunctionDecl] = {
            source.typed.get insert
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }

            source.typed.get.getFunction(definition.name).get
        }

        private def getTyped(definition : AST.FunDef) : List[Typed.FunctionDecl] = {
            source.typed.get insert
                    visited.enter(source qualifyName definition.name) { toTyped(definition) }

            source.typed.get.getFunction(definition.name).get
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

        private def lookupFunction(name : AST.QualifiedName) : List[Typed.Function] =
            source lookupFunction name.names match {
                case Nil =>
                        throw new Exception(s"cannot find name $name")
                case overloads => overloads flatMap {
                    case (scope, definition) => Processor(scope).getTyped(definition) map { _.target }
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

                    def lookupFunction(name: AST.QualifiedName) = {
                        lazy val nonLocal =
                            self lookupFunction name map { o => (o.ty, () => Typed.FunctionRef(o)) }

                        if (name.names.length == 1) {
                            locals find { _.name == name.names(0) } match {
                                case Some(p) => (p.ty, () => Typed.ParamRef(p)) :: Nil
                                case None    => nonLocal
                            }
                        } else
                            nonLocal
                    }

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
                definition.docstring, annotationsOf(definition), attributesOf(definition)).copyPositionFrom(definition)
        }

        private def toTyped(f : AST.FunAlias) : Typed.FunctionAlias =
            Typed.FunctionAlias(source.typed.get, f.name, lookupFunction(f.target).head)


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
        def promote_literal(e : Typed.Expr) =
            if (e.ty canCastTo Typed.topLevel.float_) {
                val f = ctx.lookupFunction(AST.QualifiedName("const" :: Nil)).head._2()
                Typed.FunctionCall(f, e :: Nil)
            } else e

        def function(name : List[String]) =
            (ctx lookupFunction AST.QualifiedName(name.toList)).head._2()

        def promote_opt(e : Typed.Expr) =
            if (e.ty canCastTo Typed.topLevel.floatFunc) e match {
                case Typed.BinOp(c, x, y) =>
                    val name = c match {
                        case AST.Mul => "Mul"
                        case AST.Div => "Div"
                        case AST.Add => "Add"
                        case AST.Sub => "Sub"
                    }
                    Typed.FunctionCall(
                        function("ops" :: name :: Nil),
                        promote_literal(x) :: promote_literal(y) :: Nil)

                case Typed.IfThenElse(cond, x, y) =>
                    Typed.FunctionCall(
                        function("ops" :: "Condition_Float" :: Nil),
                        cond :: promote_literal(x) :: promote_literal(y) :: Nil)

                case x => x
            } else if (e.ty canCastTo Typed.topLevel.booleanFunc) e match {

                case Typed.Condition(symbol, x, y) =>
                    val name = symbol match {
                        case AST.Equal          => "Equal"
                        case AST.NotEqual       => "NotEqual"
                        case AST.Less           => "Less"
                        case AST.Greater        => "Greater"
                        case AST.LessEqual      => "LessEqual"
                        case AST.GreaterEqual   => "GreaterEqual"
                    }
                    Typed.FunctionCall(
                        function("ops" :: name :: Nil),
                        promote_literal(x) :: promote_literal(y) :: Nil)
                case x => x
            } else if (e.ty canCastTo Typed.topLevel.sideFunc) e match {
                case Typed.IfThenElse(cond, x, y) =>
                    Typed.FunctionCall(
                        function("ops" :: "Condition_Side" :: Nil),
                        cond :: x :: y :: Nil)
                case x => x
            } else e



        def asArith(e : AST.Expr) : Typed.Expr = e match {
            case AST.BinOp(c, x, y) =>
                promote_opt(Typed.BinOp(c, asArith(x), asArith(y)))

            case AST.Neg(x) =>

                asArith(x) match {
                    case e if e.ty canCastTo Typed.topLevel.floatFunc =>
                        Typed.FunctionCall(
                            function("ops" :: "Negate" :: Nil),
                            e :: Nil)
                    case e => Typed.Neg(e)
                }

            case AST.Cast(x, ty) => Typed.Cast(asArith(x), ctx toTyped ty)

            case AST.IfThenElse(cond, x, y) =>
                promote_opt(Typed.IfThenElse(asArith(cond), asArith(x), asArith(y)))

            case AST.FloatLit(d) => Typed.FloatLit(d)
            case AST.StringLit(x) => Typed.StringLit(x)
            case AST.IntLit(x) => Typed.IntLit(x)
            case AST.Var(name) => Typed.ParamRef(ctx.lookupVar(name))

            case AST.List_(xs) => Typed.List_(xs map asArith)

            case AST.FunCall(name, args) =>

                val typed_args = args map asArith

                def checkOverload(o : TypesBound.Base) : Boolean = {
                    o match {
                        case ty : TypesBound.Function =>
                            (typed_args.length >= ty.mandatory_arg_count) &&
                            (typed_args zip ty.args forall {
                                case (actual, declared) => actual.ty canCastTo declared
                            })
                        case TypesBound.Optional(t) => checkOverload(t)
                        case _ =>
                            throw new Exception(s"Overload $o for $name must have a function-like type")
                    }
                }

                val overloads = ctx lookupFunction name

                overloads filter { o => checkOverload(o._1) } match {
                    case Nil =>
                        throw new Exception(s"No suitable overload for call $name($args). Overloads are"
                                + predef.crlf + (overloads map { _._1 } mkString predef.crlf))
                    case (_, makeExpr) :: tl =>
                        Typed.FunctionCall(makeExpr(), typed_args)
                }


            case AST.And(x, y) => Typed.And(asArith(x), asArith(y))
            case AST.Or(x, y) => Typed.Or(asArith(x), asArith(y))
            case AST.Not(x) => Typed.Not(asArith(x))
            case AST.Condition(symbol, x, y) =>
                promote_opt(Typed.Condition(symbol, asArith(x), asArith(y)))


        }

    }

}
