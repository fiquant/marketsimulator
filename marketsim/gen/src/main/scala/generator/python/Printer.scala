package generator.python

object Printer {

    trait Printable {
        def toPython : String
    }

    object types {

        trait Base

        trait Unit extends Printable {
            def toPython =
                throw new Exception("Unit types are not supported yet for python generation")
        }

        trait Tuple extends Printable {
            val elems : List[Base]
            def toPython = {
                throw new Exception("Tuple types are not supported yet for python generation")
                //elems.mkString("(", ",", ")")
            }

        }

        trait Function extends Printable {
            val args : List[Base]
            val ret : Base
            def toPython = {
                val a = args match {
                    case Nil => ""
                    case x :: Nil => "," + x
                    case _ => throw new Exception("Only unary and nullary functions are supported for python generation")
                }
                s"types.IFunction[$ret$a]"
                //(if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
            }
        }

        trait `Float`    extends Printable {  def toPython = "float"  }
        trait `Boolean`  extends Printable {  def toPython = "bool"   }

    }

}
