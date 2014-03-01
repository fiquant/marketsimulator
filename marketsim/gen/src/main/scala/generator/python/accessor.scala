package generator.python

object accessor extends gen.PythonGenerator
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

        val fieldName = f.name.head.toLower + f.name.tail

        def dereference = base.Prop("dereference", "return self.x." + fieldName)

        override def body = super.body | dereference
    }


    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.accessor"
}
