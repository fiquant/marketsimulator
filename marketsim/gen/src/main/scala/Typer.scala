package object Typer
{
    trait TypingExprCtx
    {
        def lookupFunction(name : AST.QualifiedName)
            :   List[(TypesBound.Function, () => Typed.Expr)]

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

    def annotationsOf(definition : AST.Decorated) = definition.decorators collect toTypedAnnotation

    def attributesOf(definition : AST.Decorated) = Typed.Attributes((definition.decorators collect toTypedAttribute).toMap)

    private val toTypedAnnotation : PartialFunction[AST.Decorator, Typed.Annotation] = {
        case a :  AST.Annotation => Typed.Annotation(Typed.Annotations.lookup(a.name.toString), a.parameters)
    }

    private val toTypedAttribute : PartialFunction[AST.Decorator, (String,String)] = {
        case AST.Attribute(name, value) => (name, value)
    }

    def run(source : NameTable.Scope) =
    {
        source.toTyped(Typed.topLevel)
        Processor(source).processTypes()
        Typed.topLevel setMethods Processor(source).collectMethods()
        Processor(source).processFunctions()
        source.typed
    }

    case class Processor(source : NameTable.Scope)
    {
        self =>

        def collectMethods() : Stream[(TypesBound.Base, NameTable.Scope, AST.FunDef)] = {
            if (config.verbose)
                println("\t" + source.qualifiedName)

            try {

                val r =
                source.functions.toList flatMap { case (name, definitions) =>
                    try {
                        definitions flatMap {
                            case f : AST.FunDef if f.parameters.nonEmpty && f.parameters.head.initializer.nonEmpty =>
                                val typed = inferType(Nil)(f.parameters.head.initializer.get)
                                Stream((typed.ty, source, f))
                            case _ => Stream.empty
                        }

                    }
                    catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '$name' from ${source.qualifiedName}:\r\n" + ex.getMessage, ex)
                    }
                }
                val ps = source.packages.values flatMap { p => Processor(p).collectMethods() }

                r.toStream ++ ps
            } catch {
                case e : Exception =>
                    if (config.catch_errors) {
                        println(e.getMessage)
                        Stream.empty
                    }
                    else throw e
            }
        }
        
        def processTypes() {
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

                source.packages.values foreach { Processor(_).processTypes() }
            } catch {
                case e : Exception =>
                    if (config.catch_errors) {
                        println(e.getMessage)
                    }
                    else throw e
            }
        }
        

        def processFunctions() {
            if (config.verbose)
                println("\t" + source.qualifiedName)

            try {

                source.functions foreach { case (name, definitions) =>
                    try {
                        getTyped(definitions)
                    }
                    catch {
                        case ex : Exception =>
                            throw new Exception(s"\r\nWhen typing '$name' from ${source.qualifiedName}:\r\n" + ex.getMessage, ex)
                    }
                }

                source.packages.values foreach { Processor(_).processFunctions() }
            } catch {
                case e : Exception =>
                    if (config.catch_errors) {
                        println(e.getMessage)
                    }
                    else throw e
            }
        }

        val typed = source.typed.get

        def getTyped(definitions : List[AST.FunctionDeclaration]) = {
            val name = definitions.head.name

            if (!(typed.functions contains name))
                typed insert
                        visited.enter(source qualifyName name) {
                            val fs =
                                definitions flatMap {
                                    case f : AST.FunAlias => toTyped(f) map { (_, Option.empty) }
                                    case f : AST.FunDef => (toTyped(f), Some(f)) :: Nil
                                }
                                fs foreach { case (f, _) =>
                                    if (f.parameter_names != fs.head._1.parameter_names)
                                        throw new Exception(s"Overloads $f and ${fs.head} have different parameter names")
                                }

                            assert(fs forall { _._1.name == fs.head._1.name })

                            def reorder(overloads   : List[(Typed.FunctionDecl, Option[AST.FunDef])])
                                                    : List[(Typed.FunctionDecl, Option[AST.FunDef])] =
                                overloads match {
                                    // in fact it is a naive ad-hoc implementation of topological sort
                                    case Nil => Nil
                                    case _ =>
                                        overloads partition { y =>
                                            overloads exists  { x =>
                                                x != y && (x._1.target.ty betterThan y._1.target.ty) }
                                        } match {
                                            case (_, Nil) =>
                                                throw new Exception(s"there is no weakest overload between: "
                                                        + (overloads map { predef.crlf + _ } mkString ""))
                                            case (nonTerm, term) =>
                                                term ++ reorder(nonTerm)
                                        }
                                }

                            val reordered = reorder(fs)

                            val overload_signatures = (reordered map { _._1.target.ty.args }).toSet

                            def candidates(prefix : List[AST.Parameter],
                                           suffix : List[AST.Parameter]) : Stream[List[AST.Parameter]] =
                            {
                                suffix match {
                                    case Nil =>
                                        Stream(prefix)
                                    case x :: xs =>
                                        def corrected(name : List[String], args : List[AST.Expr]) =
                                            x.copy(initializer =
                                                    Some(AST.FunCall("" :: name, args)))

                                        candidates(prefix :+ x, xs) ++ (x.initializer match {
                                            case Some(AST.FunCall(c, d))
                                                if c.last == "constant" =>

                                                candidates(prefix, corrected("const" :: Nil, d) :: xs)

                                            case Some(AST.FunCall(c, d))
                                                if c.last == "true" =>

                                                candidates(prefix, corrected("observableTrue" :: Nil, d) :: xs)

                                            case Some(AST.FunCall(c, d))
                                                if c.last == "false" =>

                                                candidates(prefix, corrected("observableFalse" :: Nil, d) :: xs)

                                            case Some(AST.FunCall(c, d))
                                                if c.last == "Sell" =>

                                                candidates(prefix, corrected("side" :: "observableSell" :: Nil, d) :: xs)

                                            case Some(AST.FunCall(c, d))
                                                if c.last == "Buy" =>

                                                candidates(prefix, corrected("side" :: "observableBuy" :: Nil, d) :: xs)

                                            case Some(AST.FunCall(c, d))
                                                if c.last == "Nothing" =>

                                                candidates(prefix, corrected("side" :: "observableNothing" :: Nil, d) :: xs)

                                            case t =>
                                                Stream.empty
                                        })

                                }
                            }

                            val possibleOverloads = reordered flatMap {
                                case (typedOriginal, Some(original))
                                        if original.body.nonEmpty
                                    =>
                                        // head is guaranteed to be the original overload
                                        candidates(Nil, original.parameters).tail map { ps => original.copy(parameters = ps) }

                                case (typedOriginal, Some(original))
                                        if typedOriginal.target.qualifiedName.slice(0,2) == "" :: "ops" :: Nil
                                    =>
                                        original.ty match {
                                            case Some(AST.SimpleType(AST.QualifiedName("" :: "IFunction" :: Nil), args)) =>
                                                // head is guaranteed to be the original overload
                                                candidates(Nil, original.parameters).tail map { ps =>
                                                    original.copy(
                                                        parameters = ps,
                                                        ty = Some(AST.SimpleType("IObservable" :: Nil, args)))
                                                }
                                            case _ => Nil
                                        }

                                case _ => Nil
                            }

                            val typedOverloads =
                                possibleOverloads.distinct flatMap { f =>
                                    val f_typed = toTyped(f)
                                    if (overload_signatures contains f_typed.ty.args)
                                        None
                                    else
                                        Some(f_typed)
                                }

//                            if (typedOverloads.nonEmpty) {
//                                println(typedOverloads mkString predef.crlf)
//                            }

                            val withGenerated = reordered ++ (typedOverloads map { (_, None) })

                            reorder(withGenerated) map { _._1 }
                        }
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
            source lookupFunction name match {
                case Nil =>
                        throw new Exception(s"cannot find name $name")
                case overloads =>
                    val grouped = overloads groupBy { _._1 } mapValues { _ map { _._2 } }
                    (grouped flatMap {
                        case (scope, definitions) =>
                            Processor(scope) getTyped definitions
                    } map { _.target }).toList
                }

        private def lookupType(name : AST.QualifiedName) : Typed.TypeDeclaration =
            source lookupType name match {
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
                            definition.generics.elems map { TypesUnbound.Parameter },
                            annotationsOf(definition), attributesOf(definition))
        }

        private def toTyped(definition  : AST.Alias) : Typed.AliasDecl =
        {
            Typed.AliasDecl(definition.name,
                        typed,
                        toUnbound(definition.generics)(definition.target),
                        definition.generics.elems map { TypesUnbound.Parameter },
                        annotationsOf(definition), attributesOf(definition))
        }


        private def toUnbound(g : AST.Generics)(t : AST.Type) : TypesUnbound.Base = t match {

            case AST.SimpleType(name, genericArgs) =>
                if (name.length == 1 && (g.elems contains name(0)))
                    TypesUnbound.Parameter(name(0))
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

        class TypingCtxBase extends TypingExprCtx
        {
            def toTyped(t : AST.Type) = self.toBound(t)

            def asFunction(t : TypesBound.Base) : TypesBound.Function = t match {
                case f : TypesBound.Function => f
                case TypesBound.Optional(x) => asFunction(x)
                case _ => throw new Exception(t + " is expected to be a function-like type")
            }

            def lookupFunction(name: AST.QualifiedName) = {

                self lookupFunction name map { o => (asFunction(o.ty), () => Typed.FunctionRef(o) : Typed.Expr) }
            }

            def lookupVar(name: String) : Typed.Parameter
                = throw new Exception(s"We cannot refer to a variable in the first parameter")
        }


        private def inferType(locals: List[Typed.Parameter])(e: AST.Expr) =
        {
            class TypingCtx extends TypingCtxBase
            {
                override def lookupFunction(name : AST.QualifiedName) =
                {
                    lazy val nonLocal = super.lookupFunction(name)

                    if (name.length == 1) {
                        locals find { _.name == name(0) } match {
                            case Some(p) => (asFunction(p.ty), () => Typed.ParamRef(p)) :: Nil
                            case None    => nonLocal
                        }
                    } else
                        nonLocal
                }

                override def lookupVar(name: String) = locals.find({
                    _.name == name
                }) match {
                    case Some(p) => p
                    case None => throw new Exception(s"Cannot lookup parameter $name")
                }
            }

            TypeChecker(new TypingCtx).asArith(e)
        }

        private def toTyped(definition  : AST.FunDef): Typed.Function =
        {
            val target = typed

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

        private def toTyped(f : AST.FunAlias) : List[Typed.FunctionAlias] =
            lookupFunction(f.target) map { t => Typed.FunctionAlias(typed, f.name, t) }


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

    case class TypeChecker(ctx : TypingExprCtx)
    {
        def promote_literal(e : Typed.Expr) = typeFunction("" :: "constant" :: Nil, e :: Nil)

        def isScalar(e : Typed.Expr) = e.ty canCastTo Typed.topLevel.float_
        def isFloatFunc(e : Typed.Expr) = e.ty canCastTo Typed.topLevel.floatFunc
        def isSideFunc(e : Typed.Expr) = e.ty canCastTo Typed.topLevel.sideFunc
        
        def typeFunction(name : AST.QualifiedName, typed_args : List[Typed.Expr]) : Typed.Expr = {
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
                            Some(typeFunction(name, implicit_args))
                        } catch {
                            case _ : Exception => None
                        }
                    } match {
                        case Nil =>
                            throw new Exception(s"No suitable overload for call $name(${typed_args mkString ","}). Overloads are"
                                    + predef.crlf + (overloads map { _._1 } mkString predef.crlf) + predef.crlf +
                                    "Argument types are: " + (typed_args map { _.ty } mkString ("(",",",")") ))

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
                    lst filter { case (x, _) => lst forall { y => x betterThan y._1 } } match {
                        case Nil =>
                            throw new Exception("there is no the most concrete overload among: " +
                                    (lst mkString (predef.crlf, predef.crlf, predef.crlf)))

                        case (found, makeExpr) :: Nil =>
                            assert(found == lst.head._1)
                            Typed.FunctionCall(makeExpr(), typed_args)

                        case xs =>
                            throw new Exception(s"there are several dominating overloads $xs in $overloads and it is strange")
                    }

            }
        }
        

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
                    typeFunction("ops" :: name :: Nil, px :: py :: Nil)
                }

            case AST.Neg(x) =>

                asArith(x) match {
                    case ee if ee.ty canCastTo Typed.topLevel.floatFunc =>
                        typeFunction("ops" :: "Negate" :: Nil, ee :: Nil)
                    case ee => Typed.Neg(ee)
                }

            case AST.Cast(x, ty) => Typed.Cast(asArith(x), ctx toTyped ty)

            case AST.IfThenElse(cond, x, y) =>
                val px = asArith(x)
                val py = asArith(y)
                typeFunction("ops" :: "Condition" :: Nil, asArith(cond) :: px :: py :: Nil)

            case AST.FloatLit(d) => Typed.FloatLit(d)
            case AST.StringLit(x) => Typed.StringLit(x)
            case AST.IntLit(x) => Typed.IntLit(x)
            case AST.Var(name) => Typed.ParamRef(ctx.lookupVar(name))

            case AST.List_(xs) => Typed.List_(xs map asArith)

            case AST.FunCall(name, args) =>   typeFunction(name, args map asArith)

            case AST.MemberAccess(base, name, args) => typeFunction(name :: Nil, (base :: args) map asArith)

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
                    typeFunction("ops" :: name :: Nil, px :: py :: Nil)
                }

        }

    }

}
