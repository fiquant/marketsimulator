import syntax.scala.Printer.typed
import TypesUnbound.{Function, TypeMapper}

package object Types
{
    import AST.{ScPyPrintable, ScPrintable}
    import syntax.scala.Printer.{types => sc}
    import generator.python.Printer.{types => py}

    type Unbound = TypesUnbound.Unbound
    type Bound = TypesBound.Bound
    type TypeMapper = TypesUnbound.TypeMapper
    val EmptyTypeMapper = TypesUnbound.EmptyTypeMapper

    def genType(name : String, bases : Unbound*) = {
        val scalar  = TypesUnbound.makeScalar(name, bases : _*)
        val func    = TypesUnbound.functionOf(scalar)
        val obs     = TypesUnbound.observableOf(scalar)
        val m = Types.EmptyTypeMapper
        (scalar, scalar bind m, func bind m, obs bind m)
    }


    val (unbound_float,     float_, floatFunc, floatObservable) = genType("Float")
    val (unbound_string,    string_, stringFunc, stringObservable) = genType("String")
    val (unbound_int,       int_, intFunc, intObservable) = genType("Int", unbound_float)
    val (unbound_boolean,   boolean_, booleanFunc, booleanObservable) = genType("Boolean")
}
