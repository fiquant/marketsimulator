package object Typer
{
    trait TypingExprCtx
    {
        def lookupFunction(name : AST.QualifiedName) : List[(TypesBound.Function, () => Typed.Expr)]
        def lookupVar(name : String) : Typed.Parameter
        def toTyped(t : AST.Type) : TypesBound.Base
    }

    private val visited = new {
        var grey_set = List.empty[Any]

        def enter[T](obj : Any)(f : => T) =
        {
            // checking that there are no recursive calls
            if (grey_set contains obj)
                throw new Exception("Cycle detected in function definitions: " + grey_set.mkString("->"))

            grey_set = obj :: grey_set

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

                source.functions foreach { case (name, definitions) =>
                    try {
                        getTyped(definitions)
                    }
                    catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '$name' from ${source.qualifiedName}:\r\n" + ex.getMessage, ex)
                    }
                }

                source.packages.values foreach { Processor(_).run() }
            } catch {
                case e : Exception =>
                    if (config.catch_errors) {
                        println(e.getMessage)
                    }
                    else throw e
            }
        }

        val typed = source.typed.get

        private def getTyped(definitions : List[AST.FunctionDeclaration]) = {
            val name = definitions.head.name
            if (!(typed.functions contains name))
                typed insert
                        visited.enter(source qualifyName name) {
                            definitions map {
                                case f : AST.FunAlias => toTyped(f)
                                case f : AST.FunDef => toTyped(f)
                            } }
            typed.functions(name)
        }

        private def getTyped(definition : AST.TypeDeclaration) : Typed.TypeDeclaration = {
            typed getOrElseUpdateType (definition.name, {
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
                case overloads =>
                    val grouped = overloads groupBy { _._1 } mapValues { _ map { _._2 } }
                    (grouped flatMap {
                        case (scope, definitions) =>
                            Processor(scope) getTyped definitions
                    } flatMap { _.targets }).toList
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
                            typed,
                            definition.bases map { toUnbound(definition.generics) },
                            definition.generics.elems map { TypesUnbound.Parameter })
        }

        private def toTyped(definition  : AST.Alias) : Typed.AliasDecl =
        {
            Typed.AliasDecl(definition.name,
                        typed,
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
            val target = typed

            def inferType(locals: List[Typed.Parameter])(e: AST.Expr) = {
                val ctx = new TypingExprCtx {
                    def toTyped(t : AST.Type) = self.toBound(t)

                    def lookupFunction(name: AST.QualifiedName) = {
                        lazy val nonLocal =
                            self lookupFunction name map { o => (asFunction(o.ty), () => Typed.FunctionRef(o)) }

                        def asFunction(t : TypesBound.Base) : TypesBound.Function = t match {
                            case f : TypesBound.Function => f
                            case TypesBound.Optional(x) => asFunction(x)
                            case _ => throw new Exception(t + " is expected to be a function-like type")
                        }

                        if (name.names.length == 1) {
                            locals find { _.name == name.names(0) } match {
                                case Some(p) => (asFunction(p.ty), () => Typed.ParamRef(p)) :: Nil
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
            Typed.FunctionAlias(typed, f.name, lookupFunction(f.target))


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
                val f = ctx.lookupFunction(AST.QualifiedName("constant" :: Nil)).head._2()
                Typed.FunctionCall(f, e :: Nil)
            } else e

        def function(name : List[String]) =
            (ctx lookupFunction AST.QualifiedName(name.toList)).head._2()

        def isScalar(e : Typed.Expr) = e.ty canCastTo Typed.topLevel.float_
        def isFloatFunc(e : Typed.Expr) = e.ty canCastTo Typed.topLevel.floatFunc
        def isSideFunc(e : Typed.Expr) = e.ty canCastTo Typed.topLevel.sideFunc

        def asArith(e : AST.Expr) : Typed.Expr = e match {
            case AST.BinOp(c, x, y) =>
                val px = asArith(x)
                val py = asArith(y)
                if (isScalar(px) && isScalar(py))
                    Typed.BinOp(c, px, py)
                else {
                    val name = c match {
                            case AST.Mul => "Mul"
                            case AST.Div => "Div"
                            case AST.Add => "Add"
                            case AST.Sub => "Sub"
                    }
                    asArith(AST.FunCall(AST.QualifiedName("ops" :: name :: Nil), x :: y :: Nil))
                }

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
                val px = asArith(x)
                val py = asArith(y)
                if (isFloatFunc(px) || isFloatFunc(py))
                    asArith(AST.FunCall(AST.QualifiedName("ops" :: "Condition_Float" :: Nil), cond :: x :: y :: Nil))
                else if (isSideFunc(px) || isSideFunc(py))
                    asArith(AST.FunCall(AST.QualifiedName("ops" :: "Condition_Side" :: Nil), cond :: x :: y :: Nil))
                else
                    Typed.IfThenElse(asArith(cond), asArith(x), asArith(y))

            case AST.FloatLit(d) => Typed.FloatLit(d)
            case AST.StringLit(x) => Typed.StringLit(x)
            case AST.IntLit(x) => Typed.IntLit(x)
            case AST.Var(name) => Typed.ParamRef(ctx.lookupVar(name))

            case AST.List_(xs) => Typed.List_(xs map asArith)

            case AST.FunCall(name, args) =>

                def impl(typed_args : List[Typed.Expr]) : Typed.Expr = {
                    def checkOverload(ty : TypesBound.Function) : Boolean = {
                        (typed_args.length >= ty.mandatory_arg_count) &&
                        (typed_args zip ty.args forall {
                            case (actual, declared) => actual.ty canCastTo declared
                        })
                    }

                    val overloads = ctx lookupFunction name

                    overloads filter { o => checkOverload(o._1) } match {
                        case Nil =>

                            def possibleCasts(prefix : List[Typed.Expr],
                                              rest   : List[Typed.Expr])
                                : Stream[List[Typed.Expr]] = rest match
                            {
                                case Nil => Stream.empty
                                case x :: tl =>
                                    possibleCasts(prefix :+ x, tl) ++ (
                                            if (x.ty canCastTo Typed.topLevel.float_)
                                                (prefix ++ (promote_literal(x) :: tl)) :: Nil
                                            else
                                                Stream.empty)
                            }

                            possibleCasts(Nil, typed_args).toList flatMap { implicit_args =>
                                try {
                                    Some(impl(implicit_args))
                                } catch {
                                    case _ : Exception => None
                                }
                            } match {
                                case Nil =>
                                    throw new Exception(s"No suitable overload for call $name(${args mkString ","}). Overloads are"
                                            + predef.crlf + (overloads map { _._1 } mkString predef.crlf))

                                case x :: Nil => x

                                case tl =>
                                    if (tl forall { _ == tl.head})
                                        tl.head
                                    else
                                        throw new Exception("Conflicting implicit casts gives " + tl)
                            }

                        case (_, makeExpr) :: Nil =>
                            Typed.FunctionCall(makeExpr(), typed_args)

                        case lst =>
                            def better(t : TypesBound.Function, u : TypesBound.Function) =
                                t.args zip u.args forall { case (a,b) => a canCastTo b }
                        
                            lst filter { case (x, _) => lst forall { y => better(x, y._1) } } match {
                                case Nil =>
                                    throw new Exception("there is no the most concrete overload among: " +
                                            (lst mkString (predef.crlf, predef.crlf, predef.crlf)))

                                case (_, makeExpr) :: Nil =>
                                    Typed.FunctionCall(makeExpr(), typed_args)

                                case xs =>
                                    throw new Exception(s"there are several dominating overloads $xs in $overloads and it is strange")
                            }

                    }
                }

                impl(args map asArith)



            case AST.And(x, y) => Typed.And(asArith(x), asArith(y))
            case AST.Or(x, y) => Typed.Or(asArith(x), asArith(y))
            case AST.Not(x) => Typed.Not(asArith(x))
            case AST.Condition(symbol, x, y) =>
                val px = asArith(x)
                val py = asArith(y)
                if (isScalar(px) && isScalar(py))
                    Typed.Condition(symbol, px, py)
                else {
                    val name = symbol match {
                        case AST.Equal          => "Equal"
                        case AST.NotEqual       => "NotEqual"
                        case AST.Less           => "Less"
                        case AST.Greater        => "Greater"
                        case AST.LessEqual      => "LessEqual"
                        case AST.GreaterEqual   => "GreaterEqual"
                    }
                    asArith(AST.FunCall(AST.QualifiedName("ops" :: name :: Nil), x :: y :: Nil))
                }

        }

    }

}
