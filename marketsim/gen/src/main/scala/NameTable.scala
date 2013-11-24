import syntax.scala.Printer.{typed => pp}
import AST.ScPrintable

object NameTable {

    class Scope(val name : String = "_root_") extends pp.Scope with ScPrintable {

        var functions = Map[String, AST.FunDef]()
        var packages = Map[String, Scope]()
        var parent : Option[Scope] = None
        var typed : Option[Typed.Package] = None

        def add(f : AST.FunDef) {
            check_name_is_unique(f.name, f)
            functions = functions updated (f.name, f)
        }

        override def equals(o : Any) = true

        private def check_name_is_unique(name : String, e : Any) {
            if (functions contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + functions(name) + "\r\n" + e)
            if (packages contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + packages(name) + "\r\n" + e)
        }

        def add(p : AST.PackageDef) {
            val target = (p.name.names map (new Scope(_))).foldLeft(this) {
                case (x, y) =>
                    x.check_name_is_unique(y.name, y)
                    x.packages = x.packages updated (y.name, y)
                    y.parent = Some(x)
                    y
            }
            create(p.members, target)
        }

        def getFunDef(name : AST.QualifiedName) : AST.FunDef = getFunDef(name.toString)

        def getFunDef(name : String) : AST.FunDef = {
            functions get name match {
                case Some(x) => x
                case None => throw new Exception(s"Cannot find name $name")
            }
        }

        def lookupFunction(name : List[String]) : Option[(Scope, AST.FunDef)] = {
            name match {
                case Nil => throw new Exception("Qualified name cannot be empty")
                case x :: Nil =>
                    functions get x match {
                        case Some(f) => Some((this, f))
                        case None => parent flatMap { _ lookupFunction name }
                    }
                case x :: tl =>
                    packages get x map { _ lookupFunction tl } match {
                        case None => parent flatMap { _ lookupFunction name }
                        case y => y.get
                    }
            }
        }

        private def toTyped(target : Typed.Package) : Typed.Package =
        {
            typed = Some(target)
            packages.values foreach {
                p => p.toTyped(target.createChild(p.name))
            }
            target
        }

        def typePackages = toTyped(new Typed.Package())
    }

    private def create(p : AST.Definitions, impl : Scope) : Unit =
        p.definitions foreach {
            case fun_def : AST.FunDef => impl.add(fun_def)
            case package_def : AST.PackageDef => impl.add(package_def)
        }

    def apply(p : List[AST.Definitions], impl : Scope = new Scope) : Scope =
    {
        p foreach { create(_, impl) }

        impl
    }

}
