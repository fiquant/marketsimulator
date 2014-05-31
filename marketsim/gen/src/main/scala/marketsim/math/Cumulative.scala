package marketsim.math

import marketsim.OptObservable
import Ordering.Implicits._

object Cumulative {

    case class Min[T : Ordering](x : OptObservable[T]) extends OptObservable[T]
    {
        x += {
            case None =>
            case Some(value) =>
                if (_value.isEmpty || value < _value.get)
                    update(Some(value))
        }
    }

    case class Max[T : Ordering](x : OptObservable[T]) extends OptObservable[T]
    {
        x += {
            case None =>
            case Some(value) =>
                if (_value.isEmpty || value > _value.get)
                    update(Some(value))
        }
    }
}
