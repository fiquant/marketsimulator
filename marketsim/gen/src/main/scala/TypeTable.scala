case class TypeTable(types : Map[String, Types.Function] = Map.empty) {

    override def toString = types mkString "\r\n"

    def updated(key : String, value : Types.Function) = TypeTable(types updated (key, value))

    def contains(name : String) = types contains name

    def lookup(name : AST.QualifiedName) =
        types.get(name.toString) match {
            case Some(t) => t
            case _ => throw new Exception(s"cannot lookup type for $name")
        }
}
