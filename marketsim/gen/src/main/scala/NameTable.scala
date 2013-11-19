package object NameTable {

    class Impl {

        var functions = Map[String, AST.FunDef]()

        def add(f : AST.FunDef) {
            if (functions contains f.name)
                throw new Exception(s"Duplicate definition for ${f.name}:\r\n" + functions(f.name) + "\r\n" + f)
            functions = functions updated (f.name, f)
        }

        override def toString = functions mkString "\r\n"

        def getFunDef(name : AST.QualifiedName) : AST.FunDef = getFunDef(name.toString)

        def getFunDef(name : String) : AST.FunDef = {
            functions get name match {
                case Some(x) => x
                case None => throw new Exception(s"Cannot find name $name")
            }
        }
    }

    def create(p : List[AST.Definitions])  =
    {
        val impl = new Impl

        p foreach {
            case f : AST.FunDef => impl.add(f)
        }

        impl
    }

}
