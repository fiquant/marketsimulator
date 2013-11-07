package object PrettyPrinter
{
    abstract class Base
    {
        def apply(x : Types.Type) : String
    }

    var instance : Base = null
    def print(x : Types.Type): String = instance.apply(x)
}

