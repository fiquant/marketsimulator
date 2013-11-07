package syntax.scala

import Types._

class Printer() extends PrettyPrinter.Base {

    def apply(x : Type) = x match {
        case _ : `Float` => "Float"
        case _ : Unit => "()"
        case Tuple(lst) => "(" + lst.mkString(",") + ")"
        case Function(args, ret) => s"$args => $ret"
    }

}
