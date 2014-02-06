package generator.python

import predef._
import predef.ImportFrom
import scala.Some
import order_factory.curriedTypesAsList

object curried
        extends Typed.BeforeTyping
{
    trait IFunction extends base.Printer
    {
        def original : Typed.Function
        def curried : List[Typed.Parameter]

        def ifunction_base =  s"IFunction["||| original.ret_type.asCode |||
                ", "||| curriedTypesAsList(curried) |||"]" ||| ImportFrom("IFunction", "marketsim")
        override def base_class_list = ifunction_base :: Nil
    }

    object after_typing
        extends gen.PythonGenerator
    {
        import order_factory_curried.{FactoryParameter, lookupOriginal}

        case class Curried(args   : List[String],
                           f  : Typed.Function)
                extends base.Printer
                with    base.DocString
                with    base.Alias
                with    base.DecoratedName
                with    IFunction
        {
            val original = lookupOriginal(args, f)

            override type Parameter = FactoryParameter
            def mkParam(p : Typed.Parameter) = FactoryParameter(p)

            val curried = original.parameters filter { p => !(f.parameters contains p) }
            val curried_parameters =  curried map mkParam

            def call_body_assignments = join_fields({ _.call_body_assign }, crlf)
            def call_body_assign_args = join_fields({ _.call_body_assign_arg }, crlf, curried_parameters)

            override def call_body = call_body_assign_args |
                    call_body_assignments |
                    s"""return ${original.name}(${original.parameters map { _.name} mkString ","})""" |||
                    Printer.importsOf(original)

            override def call_args = join_fields({ _.call_arg }, ",", curried_parameters)

            override def body = super.body | call
        }

        def generatePython(/** arguments of the annotation */ args  : List[String])
                          (/** function to process         */ f     : Typed.Function) =
        {
            new Curried(args, f)
        }

        val name = "python.curried"
    }


    import order_factory.{extract , locate}

    def beforeTyping(/** arguments of the annotation */ args  : List[String])
                    (/** function to process         */ f     : AST.FunDef,
                                                        scope : NameTable.Scope)
    {
        def partialFactory(curried  : String,
                           base_    : AST.FunDef = f) =
        {
            //println(s"partial factory $curried for $base_")
            val base = base_
            val prefix = curried + "_"
            val prefixed = prefix + base.name

            val orig_path = base.name split "_"
            val (orig_scope, brief_name_arr) = orig_path.splitAt(orig_path.length - 1)
            val u_prefix = curried
            val alias = u_prefix :: orig_scope.toList
            val brief_name = brief_name_arr(0)

            (extract(curried :: Nil, base.parameters) match {
                case Some((cr, rest)) =>
                    val ty = Some(AST.FunctionType(cr map { _.ty.get }, base.ty.get))
                    Some(base.copy(
                        name = prefixed,
                        parameters = rest,
                        body = None,
                        decorators =
                                AST.Annotation(
                                    AST.QualifiedName(
                                        after_typing.name.split('.').toList),
                                    base.name :: Nil) :: Nil,
                        ty = ty map scope.fullyQualifyType))
                case _ =>
                    throw new Exception("cannot happen")
            }) map  { fc =>
                val curried = locate(alias, scope)

                if (!(curried.members contains fc.name))
                    curried add fc

                fc
            }
        }

        args map { partialFactory(_, f) }

    }

    val name = "curried"
}
