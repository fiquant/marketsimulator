package generator.python

import java.io._
import resource._
import scala.Some

package object gen
{
    def apply(p : Typed.Package, dst_dir : String) { apply(p, new File(dst_dir)) }

    def apply(p : Typed.Package, dir : File)
    {
        if (!dir.exists()) {
            dir.mkdirs()
            if (!dir.exists())
                throw new Exception("cannot create directory " + dir.getName)
        }

        p.packages.values foreach { sub => apply(sub, new File(dir, sub.name) ) }
        p.anonymous       foreach {        apply(_, dir) }

        def printWriter(filename : String) =
            new PrintWriter(
                new BufferedWriter(
                    new OutputStreamWriter(
                        new FileOutputStream(
                            new File(dir, filename)))),
                    true)

        val names = p.functions.values flatMap { f =>
            f.annotations collect { case Typed.Annotation(g : PythonGenerator, args) => g.generatePython(args)_ } match {
                case Nil =>
                    None
                    // an exception should be thrown here if function body is empty

                case g :: Nil =>
                    val generated = g(f)
                    for (out <- managed(printWriter(s"_${generated.target}.py"))) {
                        out.println(generated)
                    }
                    Some(generated.name)

                case _ => throw new Exception("Multiple python generators are given for function " + f)
            }

        }

        for (out <- managed(printWriter("__init__.py"))) {}
    }

    trait GenerationUnit
    {
        def name : String
        def target = name
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
        register(base.python)
        register(observable)
        register(function)
        register(intrinsic)
        register(intrinsic_function)
        register(intrinsic_observable)
        register(order_factory)
    }
}
