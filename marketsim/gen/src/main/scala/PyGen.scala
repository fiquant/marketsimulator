package object PyGen {

    case class ParameterFloat(name : String, initializer : Double)

    case class ImportRandom(name        : String,
                            parameters  : List[ParameterFloat],
                            label       : String,
                            docstring   : String)
}
