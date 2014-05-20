package marketsim

class Event[T] {

    var listeners = List.empty[T => Unit]

    def += (listener : T => Unit) {
        if ((listeners indexOf listener) == -1)
            listeners = listener :: listeners
    }

    def apply(x : T) {
        listeners foreach { _(x) }
    }
}

abstract class Observable[T] extends Event[Option[T]] with (() => Option[T])
{
    protected var _value = Option.empty[T]

    def value = _value

    def apply() = _value

    protected def update(x : Option[T]) {
        if (x != _value) {
            _value = x
            apply(_value)
        }
    }
}

case class OnEveryDt[T](dt : Time, f : () => Option[T]) extends Observable[T]
{
    import Scheduler.process
    process(const(dt), { () => update(f()) })

    override def toString = s"OnEveryDt($dt, $f)"
}
