package object NameTable {

    class Scope(val name : String = "_root_") {

        var functions = Map[String, AST.FunDef]()
        var packages = Map[String, Scope]()

        def add(f : AST.FunDef) {
            check_name_is_unique(f.name, f)
            functions = functions updated (f.name, f)
        }

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
                    y
            }
            create(p.members, target)
        }

        override def toString = s"\r\npackage $name {" +
                (packages.values mkString "\r\n") +
                (functions.values mkString "\r\n") + "\r\n}"

        def getFunDef(name : AST.QualifiedName) : AST.FunDef = getFunDef(name.toString)

        def getFunDef(name : String) : AST.FunDef = {
            functions get name match {
                case Some(x) => x
                case None => throw new Exception(s"Cannot find name $name")
            }
        }
    }

    def create(p : AST.Definitions, impl : Scope) : Unit =
        p.definitions foreach {
            case fun_def : AST.FunDef => impl.add(fun_def)
            case package_def : AST.PackageDef => impl.add(package_def)
        }

    def create(p : List[AST.Definitions], impl : Scope = new Scope) : Scope =
    {
        p foreach { create(_, impl) }

        impl
    }

}
