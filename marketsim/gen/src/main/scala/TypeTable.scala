case class TypeTable(types : Map[String, Typed.Function] = Map.empty) {

    override def toString = types mkString "\r\n"

    def updated(f : Typed.Function) = TypeTable(types updated (f.name, f))

    def contains(name : String) = types contains name

    def lookup(name : AST.QualifiedName) =
        types.get(name.toString) match {
            case Some(t) => t
            case _ => throw new Exception(s"cannot lookup type for $name")
        }
}
