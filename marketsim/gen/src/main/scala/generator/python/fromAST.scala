package generator.python
import PyGen._

case class fromAST(f : AST.FunDef)
{
    case class ParameterConverter(p : AST.Parameter)
    {
        def assertTypeIsFloat() = p.ty match {
            case None => throw new Exception("functions imported from mathops should have explicitly specified types")
            case Some(AST.SimpleType("Float")) => ()
            case _ => throw new Exception("functions imported from mathops should have Float type")
        }

        def getFloatInitializer = p.initializer match {
            case None => throw new Exception("initializer for parameter should be specified")
            case Some(AST.Const(d)) => d
            case _ => throw new Exception("functions imported from mathops may have only float parameters")
        }

        def mathops = {
            assertTypeIsFloat()
            ParameterOfMathops(p.name, getFloatInitializer)
        }

        def random = {
            assertTypeIsFloat()
            ParameterOfRandom(p.name, getFloatInitializer)
        }
    }

    lazy val (label, comment) = f.docstring match {
        case Some(AST.DocString(brief, detailed)) => (brief, detailed)
        case _ => ("","")
    }

    def create = {
        f.annotations.find({ _.name.toString == "python.random" }) match {
            case Some(_) => Some(ImportRandom(f.name, f.parameters map { ParameterConverter(_).random }, label, comment))
            case None => f.annotations.find({ _.name.toString == "python.mathops" }) match {
                case Some(AST.Annotation(_, category :: impl :: label_tmpl :: Nil)) => {
                    Some(ImportMathops(f.name, category, impl, Some(label_tmpl), f.parameters map { ParameterConverter(_).mathops }, comment))
                }
                case _ => None
            }
        }
    }
}

object fromAST {

    def apply(p : AST.Definitions) : List[Printer] = {
        p.definitions.flatMap({ fromAST(_).create })
    }

}
