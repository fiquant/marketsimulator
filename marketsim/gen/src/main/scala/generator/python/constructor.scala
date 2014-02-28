package generator.python

object constructor extends gen.PythonGenerator
{
    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(args : List[String], f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
    {
        override type Parameter = constructor.Parameter
        def mkParam(p : Typed.Parameter) = constructor.Parameter(p)

        val type_declaration = f.parent.types(f.name).asInstanceOf[Typed.InterfaceDecl]
        val base_classes = type_declaration.bases map { _ bind TypesUnbound.EmptyTypeMapper_Bound }

        override def base_class_list = base_classes
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.constructor"
}
