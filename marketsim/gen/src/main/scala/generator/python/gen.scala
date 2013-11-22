package generator.python

import java.io.{File, PrintWriter}
import resource._

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

        def pyFile(f : Typed.Function) = new PrintWriter(new File(dir, "_" + f.name + ".py"))

        p.functions.values foreach { f =>
            f.annotations collect { case Typed.Annotation(g : PythonGenerator, args) => g(args)_ } match {
                case Nil =>
                    // an exception should be thrown here if function body is empty

                case g :: Nil =>
                    for (out <- managed(pyFile(f))) {
                        out.println(g(f))
                    }

                case _ => throw new Exception("Multiple python generators are given for function " + f)
            }

        }
    }

    trait PythonGenerator extends Typed.AnnotationHandler
    {
        def apply(/** arguments of the annotation */ args  : List[String])
                 (/** function to process         */ f     : Typed.Function) : String

    }


}
