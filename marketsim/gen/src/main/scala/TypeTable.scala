case class TypeTable(types : Map[String, Types.Function]) {

    override def toString = types mkString "\r\n"

    def lookup(name : AST.QualifiedName) =
        types.get(name.toString) match {
            case Some(t) => t
            case _ => throw new Exception(s"cannot lookup type for $name")
        }
}
