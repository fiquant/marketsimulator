package generator.python

import java.io._
import resource._
import scala.Some
import predef._

package object gen
{
    // TODO: memoization
    def generationUnit(f : Typed.Function) = 
    {
        if (f.tryGetAttribute("python") == Some("no"))
            None
        else
            f.annotations collect {
                case Typed.Annotation(g : PythonGenerator, args) => g.generatePython(args)_
            } match {
                case Nil =>
                    Some(base.python.generatePython(Nil)(f))

                case g :: Nil =>
                    Some(g(f))

                case _ => throw new Exception("Multiple python generators are given for function " + f)
            }
    }
    
    def run(p : Typed.Package, dst_dir : String, idx_dir : String)
    {
        processFunctions(p, new File(dst_dir), new File(idx_dir))
        processTypes(p, new File(dst_dir), new File(idx_dir))

        processUsedTypes(new File(dst_dir))

        generateIntrinsicBases(new File(dst_dir, "_intrinsic_base"))
    }

    def createInit(dir : File) {
        for (out <- managed(printWriter(dir, "__init__.py"))) {}
    }

    def generateIntrinsicBases(dst_dir : File)
    {
        def fileFor(base : File, parts : List[String]) : File = {
            ensure_dir(base)
            createInit(base)
            parts match {
                case Nil => throw new Exception("intrinsic module name cannot be empty")
                case x :: Nil => new File(base, x.toLowerCase + ".py")
                case x :: tl => fileFor(new File(base, x), tl)
            }
        }

        Typed.topLevel.intrinsics foreach { case (name, parameters) =>

            val parts = name split "\\."
            val (moduleName, classNameArr) = parts.splitAt(parts.length - 1)
            val className = classNameArr(0) replace ("Impl", "Base")
            for (out <- managed(printWriterEx(fileFor(dst_dir, moduleName.toList))))
            {
                val s =
                    s"class $className(object):" |>
                        Code.from(parameters map { p =>
                            base.Property(p.name,
                                s"return self._back_${p.name}",
                                s"self._back_${p.name} = value" |
                                s"self.on_${p.name}_set(value)") |
                            base.Def(s"on_${p.name}_set", "value", "pass")
                        },
                        default = "pass")

                out.println(s)
            }
        }
    }

    def printWriterEx(file : File) =
        new PrintWriter(
            new BufferedWriter(
                new OutputStreamWriter(
                    new FileOutputStream(
                        file, true))),
        true)

    def printWriter(dst_dir : File, filename : String) =
        printWriterEx(new File(dst_dir.toString.toLowerCase, filename.toLowerCase))

    def processUsedTypes(out_dir : File)
    {
        var processedTypes = Set.empty[TypesBound.Base]

        def impl(typesToProcess : Set[TypesBound.Base])
        {
            if (typesToProcess.nonEmpty)
            {
                Typed.topLevel.clearUsedTypes()

                typesToProcess foreach {
                    case f : TypesBound.Interface if f.decl.name == "IObservable" =>
                        val rt = f.genericArgs(0)
                        val name = Printer.mangle(f.asCode.toString)
                        val methods = getMethods(f)
                        val casts = Code.from(
                            TypesBound.directCasts(f.genericArgs(0)).toList map {
                                t => "_types.append(" ||| Typed.topLevel.observableOf(t).asCode ||| ")"
                            },
                            predef.crlf)

                        for (ty_out <- managed(printWriter(new File(out_dir, "_iobservable"), s"_$name.py")))
                        {
                            val s =
                                s"class $name("||| Typed.topLevel.IEvent.asCode |||", "|||
                                                   TypesBound.Function(Nil, rt).asCode |||"):" |>
                                        ("_types = []" | casts | methods)

                            ty_out.println(base.withImports(s).toString)
                        }
                    case f : TypesBound.Interface if f.decl.name == "Observable" =>
                        val rt = f.genericArgs(0)
                        val name = Printer.mangle(f.asCode.toString)

                        val casts = Code.from(
                            TypesBound.directCasts(f.genericArgs(0)).toList map { t =>
                                "_types.append(" ||| Typed.topLevel.observableImplOf(t).asCode ||| ")" },
                            predef.crlf)

                        for (ty_out <- managed(printWriter(new File(out_dir, "_observable"), s"_$name.py")))
                        {
                            val s =
                                s"class $name(Conditional_Impl, "||| Typed.topLevel.observableOf(rt).asCode |||"):" |>
                                        ("_types = []" | casts) | nl | ImportFrom("Conditional_Impl", "marketsim.event")

                            ty_out.println(base.withImports(s).toString)
                        }
                    case f : TypesBound.Alias =>
                        Typed.topLevel addTypeUsage f.target

                    case f : TypesBound.Function =>

                        val name = f.asCode

                        val args = TypesBound.Tuple(f.args).asCode

                        val b =
                            if (f.args.isEmpty && (f.ret == Typed.topLevel.float_ || f.ret == Typed.topLevel.int_ || f.ret == Typed.topLevel.boolean_))
                                "Function_impl" ||| ImportFrom("Function_impl", "marketsim.types")
                            else
                                TypesBound.Any_.asCode

                        val methods = getMethods(f)

                        val casts = Code.from(
                            TypesBound.directCasts(f.ret).toList map { t =>
                                "_types.append(" ||| TypesBound.Function(f.args, t).asCode ||| ")" },
                            predef.crlf)

                        for (ty_out <- managed(printWriter(new File(out_dir, "_ifunction"), s"_$name.py")))
                        {
                            val s =
                                "#" ||| f.asScala |
                                s"class $name("||| b |||"):" |>
                                        ("_types = [meta.function("||| args ||| "," ||| f.ret.asCode |||")]"
                                                | casts | methods) | nl |
                                ImportFrom("meta", "marketsim")

                            ty_out.println(base.withImports(s).toString)
                        }



                    case _ =>

                }
                processedTypes = processedTypes ++ typesToProcess

                impl(Typed.topLevel.getUsedTypes -- processedTypes)
            }

        }

        impl(Typed.topLevel.getUsedTypes)
    }

    def processFunctions(p : Typed.Package, dir : File, idx_dir : File)
    {
        ensure_dir(dir)
        ensure_dir(idx_dir)

        p.packages.values foreach { sub => processFunctions(sub, new File(dir, sub.name), new File(idx_dir, sub.name) ) }

        if (config.verbose)
            println("\t" + p.qualifiedName)

        for (idx_out <- managed(printWriter(idx_dir, "__init__.py")))
        {
            p.functions foreach { case (base_name, fs) =>
                fs map {
                    case f : Typed.Function =>
                        try {
                            generationUnit(f) map { g =>
                                //println(base_name, f.parent.qualifiedName, f.name, g.code)
                                (managed(printWriter(dir, s"_$base_name.py")) map { out =>
                                    out.println(g.code)
                                }).either match {
                                    case Left(exceptions) => throw new Exception(exceptions map { _.toString } mkString predef.crlf)
                                    case Right(result)    => result
                                }
                            } getOrElse f.name
                        } catch {
                            case e : Exception =>
                                if (config.catch_errors) {
                                    println(s"An exception '${e.getMessage}' caught when generating python code for $f")
                                    println(e.getMessage)
                                }
                        }
                    case f : Typed.FunctionAlias =>
                }

                if (p.types contains base_name)
                {
                    val long_name = generationUnit(fs.head.asInstanceOf[Typed.Function]).get.name
                    val interface = p.types(base_name).asInstanceOf[Typed.InterfaceDecl]

                    (managed(printWriter(dir, s"_$base_name.py")) map { out =>
                        out.println("" |> getMethods(interface.instances.head))
                        out.println(s"$base_name = $long_name")
                    }).either match {
                        case Left(exceptions) => throw new Exception(exceptions map { _.toString } mkString predef.crlf)
                        case Right(result)    => result
                    }
                    idx_out.println(base.withImports(Printer.pubImportsOf(fs.head)))
                }
                else
                {
                    import predef._

                    def tryOverload(f : Typed.Function, local : Boolean) : Code =
                        generationUnit(f) map { g =>
                            val args_to_pass = f.parameters map { _.name } mkString ","

                            def typecheck(args : List[Typed.Parameter]) : Code = args match {
                                case Nil =>
                                    s"return "||| (if (local) toLazy(g.name) else Printer.qualifiedCall(f)) |||s"($args_to_pass)"
                                case x :: tl =>
                                    (s"if ${x.name} is None or rtti.can_be_casted(${x.name}, " ||| x.ty.asCode ||| "):"
                                        |> typecheck(tl))
                            }
                            typecheck(f.parameters)
                        } getOrElse ""

                    val overloads = fs map {
                        case f : Typed.Function      => (f, true)
                        case a : Typed.FunctionAlias => (a.target, false)
                    }

                    def calls = overloads map { p => tryOverload(p._1, p._2) } reduce { _ | _ }

                    val input_args = fs.head.parameter_names map { _ + " = None" } mkString ","

                    if (calls.toString != "")
                    {
                        idx_out.println(base.withImports(Printer.pubImportsOf(fs.head)))

                        val resolver =
                            s"def $base_name($input_args): " |> base.withImports(
                                    calls |||
                                    ImportFrom("rtti", "marketsim") |
                                    s"raise Exception('Cannot find suitable overload for $base_name("+
                                            (fs.head.parameter_names
                                                    map { p => "str(" + p + ") +':'+ str(type("+ p +"))"  }
                                                    mkString ("'+", "+','+", "+'"))+
                                            ")')")

                        for (out <- managed(printWriter(dir, s"_$base_name.py"))) {
                            out.println(resolver)
                        }
                    }
                }
            }
        }

    }
    def getMethods(t : TypesBound.Base) =
    {
        val methods = Typed.topLevel getMethods t

        if (methods.isEmpty)
            toLazy("pass")
        else {
            (methods map { case (method_name, fs) =>
                val args = fs.head.parameters.tail
                val target = fs.head.name ||| ImportFrom(fs.head.name, Printer.moduleName(fs.head))
                if (args.isEmpty) {
                    base.Prop(method_name, "return " ||| target ||| "(self)")
                } else {
                    val in_args = Code.from(args map { _.name ||| " = None" }, ",")
                    val pass_args = Code.from(args map { "," ||| _.name }, "")
                    base.Def(method_name,
                        in_args,
                        "return " ||| target |||
                                "(self" ||| pass_args ||| ")")
                }
            } reduce { _ | _ }) | "pass"
        }
    }

    def processTypes(p : Typed.Package, dir : File, idx_dir : File)
    {
        ensure_dir(dir)
        ensure_dir(idx_dir)

        p.packages.values foreach { sub => processTypes(sub, new File(dir, sub.name), new File(idx_dir, sub.name) ) }

        if (config.verbose)
            println("\t" + p.qualifiedName)

        def importsWithout(code: => predef.Code, exclude : Importable => Boolean) : Code =
            new WithoutImports((code.imports.toSet[Importable] filterNot exclude map { _.repr + crlf } mkString "") + code)

        for (idx_out <- managed(printWriter(idx_dir, "__init__.py")))
        {
            if (p.types.nonEmpty)
            {
                p.types.values foreach {
                    case interface : Typed.InterfaceDecl if p.functions contains interface.name =>
                    case interface : Typed.InterfaceDecl =>
                            val name = interface.name

                            val filename =
                                if (interface.generics.isEmpty)
                                    s"_$name.py"
                                else {
                                    ensure_dir(new File(s"$dir/_$name"))
                                    s"_$name/__init__.py"
                                }

                            for (out <- managed(printWriter(dir, filename)))
                            {
                                if (interface.generics.isEmpty) {

                                    val bases =
                                        if (p.functions contains name) {
                                            toLazy("object")
                                        } else
                                        if (interface.bases.nonEmpty)
                                                interface.bases map {
                                                    b => (b bind TypesUnbound.EmptyTypeMapper_Bound).asCode
                                                } reduce { _ ||| "," ||| _ }
                                            else
                                                if (name == "Side")
                                                    "Tag" ||| ImportFrom("Tag", "marketsim.side_")
                                                else
                                                    toLazy("object")

                                    val body =
                                        if (interface.instances.size == 1)
                                            getMethods(interface.instances.head)
                                        else
                                            toLazy("pass")

                                    val s = s"class $name("||| bases |||"):" |> body

                                    out.println(base.withImports(s).toString)

                                }
                            }

                        case alias : Typed.AliasDecl =>
                            val name = alias.name
                            val filename =
                                if (alias.generics.isEmpty)
                                    s"_$name.py"
                                else {
                                    ensure_dir(new File(s"$dir/_$name"))
                                    s"_$name/__init__.py"
                                }

                            for (out <- managed(printWriter(dir, filename)))
                                if (alias.generics.isEmpty)
                                    out.println(
                                        base.withImports(alias.name + " = " |||
                                                (alias.target bind TypesUnbound.EmptyTypeMapper_Bound).asCode).toString)
                }
            }

            p.packages.values foreach { pkg =>
                idx_out.println(s"import " + pkg.name.toLowerCase)
            }

            for (out <- managed(printWriter(dir, "__init__.py"))) {}

        }

    }


    def ensure_dir(d: File) {
        val dir = new File(d.toString.toLowerCase)
        if (!dir.exists()) {
            dir.mkdirs()
            if (!dir.exists())
                throw new Exception("cannot create directory " + dir.getName)
        }
    }

    trait GenerationUnit
    {
        def name : String
        def code : predef.Code
    }

    trait PythonGenerator extends Typed.AnnotationHandler
    {
        def generatePython(/** arguments of the annotation */ args  : List[String])
                          (/** function to process         */ f     : Typed.Function) : GenerationUnit
    }

    object Annotations {

        import Typed.Annotations._

        override def toString = registry.toString()

        // TODO: non-intrusive registration
        register(random)
        register(mathops)
        register(curried)
        register(curried.after_typing)
        register(base.python)
        register(observable)
        register(function)
        register(intrinsic)
        register(intrinsic_function)
        register(intrinsic_observable)
        register(constructor)
        register(accessor)
        register(order_factory)
        register(order_factory_curried)
        register(order_factory_on_proto)
    }
}
