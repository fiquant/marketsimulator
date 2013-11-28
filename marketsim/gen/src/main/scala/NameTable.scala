import syntax.scala.Printer.{typed => pp}
import AST.ScPrintable

object NameTable {

    class Scope(val name : String = "_root_") extends pp.Scope with ScPrintable {

        var packages = Map[String, Scope]()
        var functions = Map[String, AST.FunDef]()
        var types = Map[String, AST.TypeDeclaration]()
        var members = Map[String, AST.Member]()
        var parent : Option[Scope] = None
        var typed : Option[Typed.Package] = None

        def add(m : AST.Member) {
            //check_name_is_unique(m.name, m)
            members = members updated (m.name, m)
        }

        def add(f : AST.FunDef) {
            check_name_is_unique(f.name, f)
            functions = functions updated (f.name, f)
            add(f.asInstanceOf[AST.Member])
        }

        def add(t : AST.TypeDeclaration) {
            check_name_is_unique(t.name, t)
            types = types updated (t.name, t)
            add(t.asInstanceOf[AST.Member])
        }

        def qualifyName(x : String) = typed.get qualifyName x

        override def equals(o : Any) = true

        private def check_name_is_unique(name : String, e : Any) {
            if (functions contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + functions(name) + "\r\n" + e)
            if (types contains name)
                throw new Exception(s"Duplicate definition for $name:\r\n" + types(name) + "\r\n" + e)
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
                        case Some(f) if f.isInstanceOf[T] => Some((this, f.asInstanceOf[T]))
                        case None => parent flatMap { _ lookup name }
                    }
                case x :: tl =>
                    packages get x map { _ lookup tl } match {
                        case None => parent flatMap { _ lookup name }
                        case y => y.get
                    }
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

        // TODO: factor out common implementation for lookupXXX

        def lookupType(name : List[String]) : Option[(Scope, AST.TypeDeclaration)] = {
            name match {
                case Nil => throw new Exception("Qualified name cannot be empty")
                case x :: Nil =>
                    types get x match {
                        case Some(f) => Some((this, f))
                        case None => parent flatMap { _ lookupType name }
                    }
                case x :: tl =>
                    packages get x map { _ lookupType tl } match {
                        case None => parent flatMap { _ lookupType name }
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
            case type_def : AST.TypeDeclaration => impl.add(type_def)
            case alias : AST.TypeAlias => throw new Exception("Not implemented")
            case package_def : AST.PackageDef => impl.add(package_def)
        }

    def apply(p : List[AST.Definitions], impl : Scope = new Scope) : Scope =
    {
        p foreach { create(_, impl) }

        impl
    }

}
