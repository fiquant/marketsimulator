package syntax.scala

object TypedPP
{
    trait `Float` extends Types.`Float` {
        override def toString = "Float"
    }

    trait Unit extends Types.Unit {
        override def toString = "()"
    }

    trait Tuple extends Types.Tuple {
        override def toString = "(" + elems.mkString(",") + ")"
    }

    trait Function extends Types.Function {
        override def toString = s"$args => $ret"
    }
}
