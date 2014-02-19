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
    }

    def printWriter(dst_dir : File, filename : String) =
        new PrintWriter(
            new BufferedWriter(
                new OutputStreamWriter(
                    new FileOutputStream(
                        new File(dst_dir, filename.toLowerCase), true))),
        true)

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
                val names = fs map {
                    case f : Typed.Function =>
                        try {
                            generationUnit(f) map { g =>
                                //println(f.parent.qualifiedName, f.name)
                                for (out <- managed(printWriter(dir, s"_$base_name.py"))) {
                                    out.println(g.code)
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

                type Overload = (Typed.Function, Boolean)

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
                    case interface : Typed.InterfaceDecl =>
                            val name = interface.name
                            for (out <- managed(printWriter(dir, s"_$name.py")))
                            {
                                if (interface.generics.isEmpty) {

                                    val bases =
                                        if (interface.bases.nonEmpty)
                                                interface.bases map { _.asCode } reduce { _ ||| "," ||| _ }
                                            else
                                                if (name == "Side")
                                                    "Tag" ||| ImportFrom("Tag", "marketsim.side_")
                                                else
                                                    toLazy("object")

                                    val s = s"class $name("||| bases |||"): pass"

                                    out.println(base.withImports(s).toString)

                                } else {
                                    if (interface.name == "IObservable") {
                                        out.println("from marketsim import meta")
                                        out.println("from marketsim.gen._out._ievent import IEvent")
                                        out.println("IObservable = {}")

                                        val fs = interface.instances

                                        fs.toList sortBy { _.toString.length } foreach { f =>

                                            val rt = f.genericArgs(0).aliasesRemoved
                                            val name = Printer.mangle(f.asCode.toString)
                                            val s =
                                                s"class $name(IEvent, "||| TypesBound.Function(Nil, rt).asCode |||"):" |>
                                                        "pass" | nl |
                                                "IObservable[" ||| rt.asCode ||| "] = " ||| name | nl

                                            out.println(base.withImports(s).toString)
                                        }
                                    }
                                    if (interface.name == "Observable") {
                                        out.println("from marketsim.event import Conditional_Impl")
                                        out.println("Observable = {}")

                                        val fs = interface.instances

                                        fs.toList sortBy { _.toString.length } foreach { f =>

                                            val rt = f.genericArgs(0).aliasesRemoved
                                            val name = Printer.mangle(f.asCode.toString)
                                            val s =
                                                s"class $name(Conditional_Impl, "||| Typed.topLevel.observableOf(rt).asCode |||"):" |>
                                                        "pass" | nl |
                                                "Observable[" ||| rt.asCode ||| "] = " ||| name | nl

                                            out.println(base.withImports(s).toString)
                                        }

                                        out.println("from marketsim.gen._out._iobservable import IObservableobject")
                                        out.println("Observable[int]._types.append(IObservablefloat)")
                                        out.println("Observable[int]._types.append(IObservableobject)")
                                        out.println("Observable[float]._types.append(IObservableobject)")
                                    }
                                }
                            }

                        case alias : Typed.AliasDecl =>
                            for (out <- managed(printWriter(dir, s"_${alias.name}.py")))
                                if (alias.generics.isEmpty)
                                    out.println(base.withImports(alias.name + " = " ||| alias.target.asCode).toString)
                                else {
                                    if (alias.name == "IFunction") {
                                        out.println("from marketsim import meta")
                                        out.println("IFunction = {}")

                                        val fs =
                                            alias.instances map {
                                                case f : TypesBound.Function => f
                                                case f : TypesBound.Alias => f.target.asInstanceOf[TypesBound.Function]
                                                case _ =>
                                                    throw new Exception("IFunction instance may be only function or alias")
                                            }

                                        fs.toList sortBy { _.toString.length } foreach { f =>

                                            val name = f.asCode

                                            val args = TypesBound.Tuple(f.args).aliasesRemoved.asCode

                                            val b =
                                                if (f.args.isEmpty && (f.ret == Typed.topLevel.float_ || f.ret == Typed.topLevel.int_))
                                                    "Function_impl" ||| ImportFrom("Function_impl", "marketsim.types")
                                                else
                                                    TypesBound.Any_.asCode


                                            val s =
                                                s"class $name("||| b |||"):" |>
                                                        "_types = [meta.function("||| args ||| "," ||| f.ret.aliasesRemoved.asCode |||")]" | nl |
                                                "IFunction[" ||| f.ret.aliasesRemoved.asCode |||
                                                        (if (f.args.isEmpty) toLazy("") else "," ||| args )  ||| "] = " ||| name | nl

                                            def isMine(p : Importable) = p match {
                                                case ImportFrom(_, module) if module endsWith "._ifunction" => true
                                                case _ => false
                                            }

                                            out.println(importsWithout(s, isMine).toString)
                                        }

                                        out.println("IFunction[int]._types.append(IFunction[float])")
                                        out.println("IFunction[int]._types.append(IFunction[object])")
                                        out.println("IFunction[float]._types.append(IFunction[object])")
                                    }
                                }
                }
            }

            p.packages.values foreach { pkg =>
                idx_out.println(s"import " + pkg.name)
            }

            for (out <- managed(printWriter(dir, "__init__.py"))) {}

        }

    }


    def ensure_dir(dir: File) {
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
        register(order_factory)
        register(order_factory_curried)
        register(order_factory_on_proto)
    }
}
