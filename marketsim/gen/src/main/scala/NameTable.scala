import syntax.scala.Printer.{typed => pp}
import AST.ScPrintable
import shapeless.syntax.typeable._

object NameTable {

    class Scope(val name : String = "_root_") extends pp.NamesScope with ScPrintable {

        var packages = Map[String, Scope]()
        var members = Map[String, AST.Member]()
        var parent : Option[Scope] = None
        var typed : Option[Typed.Package] = None

        def add(m : AST.Member) {
            check_name_is_unique(m.name, m)
            members = members updated (m.name, m)
        }

        def qualifyName(x : String) = typed.get qualifyName x

        override def equals(o : Any) = true

        private def check_name_is_unique(name : String, e : Any) {
            if (members contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + members(name) + "\r\n" + e)
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

        def lookup[T <: AST.Member](name : List[String])(implicit t : Manifest[T]) : Option[(Scope, T)] = {
            name match {
                case Nil => throw new Exception("Qualified name cannot be empty")
                case x :: Nil =>
                    members get x match {
                        case Some(f) if f.cast[T].nonEmpty => Some((this, f.asInstanceOf[T]))
                        case None => parent flatMap { _ lookup name }
                    }
                case x :: tl =>
                    packages get x map { _ lookup tl } match {
                        case None => parent flatMap { _ lookup name }
                        case y => y.get
                    }
            }
        }

        def lookupFunction(name : List[String]) : Option[(Scope, AST.FunDef)] = lookup[AST.FunDef](name)
        def lookupType(name : List[String]) : Option[(Scope, AST.TypeDeclaration)] = lookup[AST.TypeDeclaration](name)

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
            case m : AST.Member => impl.add(m)
            case package_def : AST.PackageDef => impl.add(package_def)
        }

    def apply(p : List[AST.Definitions], impl : Scope = new Scope) : Scope =
    {
        p foreach { create(_, impl) }

        impl
    }

}
