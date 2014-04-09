package generator.python

import predef.PyPrintable
import predef._
import predef.Import
import predef.ImportFrom
import scala.Some

package object base {

    val tab = "    "
    val comma = ","

    abstract class Class extends gen.GenerationUnit
    {
        def name : String
        def body : Code
        def registration : Code

        private def base_classes : Code =
            if (base_class_list.isEmpty)
                TypesBound.Any_.asCode
            else
                (base_class_list map {_.asCode}).reduceLeft[Code]({ case (b, acc) => acc ||| "," ||| b })

        def base_class_list : List[TypesBound.Base] = Nil

        def code = withImports(registration | s"class $name(" ||| base_classes ||| "):" |> body)
    }

    def withImports(code: => predef.Code) : Code =
        new WithoutImports((code.imports.toSet[Importable] map { _.repr + crlf } mkString "") + code)

    def bold(s : String) = "**" + s + "**"

    abstract class Parameter {

        val p : Typed.Parameter

        def name = p.name
        def ty = p.ty.asCode
        def initializer = p.initializer
        def s_initializer = if (initializer.nonEmpty) "= None" else ""

        def init = s"$name $s_initializer"
        def init_raw = name
        def assign =  s"self.$name = $name" ||| assign_if_none

        def assign_if_none: predef.Code =
            initializer match {
                case Some(x) => s" if $name is not None else " ||| x.asCode
                case None => ""
            }

        def comment = "" :: bold(p.name) :: (p.comment map { "\t" + _ })

        def property = s"\'$name\' : " ||| ty
        def repr = s"%($name)s"
        def call = s"self.$name"

        def setter : Code = stop
        def getter : Code = stop

        def accessors = getter | setter
    }

    def Def(name : String, args : Code, body : Code) = {
        val a = if (args.toString == "") "" else ", " + args
        s"def $name(self$a):" |>
                (if (body.isInstanceOf[predef.Stop]) "pass" else withImports(body)) |
        ""
    }

    def Prop(name : String, body : Code) =
        "@property" |
        s"def $name(self):" |> withImports(body) | ""

    def Getter(name : String, body : Code) = Def("get_" + name, "", body)

    def Setter(name : String, body : Code) = Def("set_" + name, "value", body)

    def Property(name : String, getter_body : Code, setter_body : Code) =
        Getter(name, getter_body) |
        Setter(name, setter_body) |
        s"$name = property(get_$name, set_$name)"

    abstract class Printer extends Class {
        type Parameter <: base.Parameter
        def args        : List[String]
        def f           : Typed.Function
        def name        : String
        def docstring   : List[String]
        def alias       : String
        def category    = f.getAttribute("category")
        def registration =
            if (parameters exists { _.p.initializer.isEmpty })
                ""
            else
                s"""@registry.expose(["$category", "$alias"])""" ||| ImportFrom("registry", "marketsim")

        def join_fields(p           : Parameter => Code,
                        sep         : Code = ", ",
                        elements    : List[Parameter] = parameters) : Code
            =   Code.from(elements map p, sep)

        def mkParam(p : Typed.Parameter) : Parameter

        lazy val parameters  = f.parameters map mkParam

        def init_fields = join_fields({ _.init })
        def init_raw_fields = join_fields({ _.init_raw })
        def assign_fields = join_fields({ _.assign }, nl)
        def property_fields = join_fields({ _.property }, comma + nl)
        def repr_fields = join_fields({ _.repr })
        def call_fields = join_fields({ _.call })
        def accessors = join_fields({ _.accessors }, nl)

        def doc = s"""\"\"\" ${docstring.mkString(crlf)}$crlf\"\"\" """

        def init_body = assign_fields | "rtti.check_fields(self)" ||| ImportFrom("rtti", "marketsim")

        def init = Def("__init__", init_fields, init_body)

        def label = Prop("label", "return repr(self)")

        def label_tmpl : Code = f.tryGetAttribute("label") match {
            case Some(x) => x
            case None => alias ||| (if (parameters.isEmpty) "" else s"($repr_fields)")
        }


        def properties = "_properties = {" |> property_fields | "}"

        def repr_body : Code = s"""return "$label_tmpl" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])"""

        def repr = Def("__repr__", "", repr_body)

        def call_body : Code = ""
        def call_args : Code = "*args, **kwargs"
        def call = Def("__call__", call_args, call_body)

        def body = doc | init | label | properties | accessors | repr
    }

    trait DocString extends Printer {
        def docstring  = f.docstring match {
            case Some(d) =>
                (bold(d.brief)  :: "" :: d.detailed) ++ ("" :: "Parameters are:" :: (parameters flatMap { _.comment }))
            case None => Nil
        }
    }

    trait Alias extends Printer {
        def alias = f.name
    }

    trait DecoratedName extends Printer {
        def name = Printer.decoratedName(f)
    }

    trait BaseClass_Function extends Printer {

        def functionBase = {
            // here should be a check that ret_type casts to some function
            if (f.ret_type canCastTo Typed.topLevel.float_) TypesBound.Nothing else f.ret_type
        }

        override def base_class_list =
            if (functionBase != TypesBound.Nothing)
                functionBase :: super.base_class_list
            else
                super.base_class_list
    }

    trait BaseClass_Observable extends Printer {

        def ty = f.ret_type.returnTypeIfFunction.get

        def trivialObservable = false

        def observableBase : TypesBound.Base =
            if (trivialObservable)
                Typed.topLevel.observableOf(ty)
            else
                Typed.topLevel.observableImplOf(ty)

        override def base_class_list = observableBase :: super.base_class_list

        override def init_body =
            observableBase.asCode ||| ".__init__(self)" |
            super.init_body
    }

    trait Intrinsic extends Printer
    {
        def impl_module : String
        def impl_function = f.name

        override def call_body : Code = s"""return $impl_module.$impl_function($call_fields)""" ||| Import(impl_module)
    }

    trait IntrinsicEx extends Printer
    {
        if (args.length != 1)
            throw new Exception(s"Annotation $name should have 1 arguments in" +
                    " form (implementation_class)" + crlf + "In function " + f)

        val last_dot_idx = args(0).lastIndexOf(".")
        val implementation_module =args(0).substring(0, last_dot_idx)
        val implementation_class  =args(0).substring(last_dot_idx + 1)
    }

    trait Bind extends Printer
    {
        def bind = Def("bind", "ctx", "self._ctx = ctx.clone()")

        override def body = super.body | bind
    }

    trait HasImpl extends Printer
    {
        def getImpl = Def("getImpl", "", "return " ||| f.body.get.asCode)

        def internals = "_internals = ['impl']"

        override def body = super.body | internals | call | reset | getImpl | getattr

        override def call_body = "return self.impl()"

        override def init_body =
            super.init_body |
            "self.impl = self.getImpl()"

        def reset = Def("reset", "",
            "self.impl = self.getImpl()" |
            "ctx = getattr(self, '_ctx', None)" |
            "if ctx: context.bind(self.impl, ctx)") |||
            ImportFrom("context", "marketsim")

        def getattr = Def("__getattr__", "name",
            "if name[0:2] != '__' and self.impl:" |> "return getattr(self.impl, name)" |
            "else:" |> "raise AttributeError")
    }

    trait SubscribeParameter extends Parameter
    {
        def observe_args = true

        def intrinsic_base : String

        lazy val IEvent = Typed.topLevel.getScalarBound("IEvent")

        override def setter =
            super.setter | (
            if (observe_args)
                if (p.ty canCastTo TypesBound.Optional(IEvent)) {
                    base.Def(s"on_${name}_set", "value",
                                    s"event.subscribe_field(self, '$name', value)" |||
                                    ImportFrom("event", "marketsim"))
                } else ""
            else "")
    }

    trait IntrinsicBaseClass extends Printer
    {
        Typed.topLevel.addIntrinsic(args(0), parameters map { _.p })
    }


    object python extends gen.PythonGenerator
    {
        val name = "python"

        def generatePython(/** arguments of the annotation */ args  : List[String])
                          (/** function to process         */ f     : Typed.Function) =
        {
            (if (TypesBound.isObservable(f.ret_type)) observable
                else if (TypesBound.isStrategy(f.ret_type))
                    strategy
                else
                    function).generatePython(args)(f)
        }
    }

}
