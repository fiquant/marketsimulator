package marketsim

import scala.collection.mutable

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

case class OnEveryDt_[T](dt : Time, f : () => Option[T]) extends Observable[T]
{
    import Scheduler.process
    process(const(dt), { () => update(f()) })

    override def toString() = s"OnEveryDt($dt, $f)"
}

object OnEveryDt
{
    private val cache = collection.mutable.HashMap.empty[Any, Any]

    def apply[T](dt : Time, f : () => Option[T]) =
        (cache getOrElseUpdate ((dt, f), new OnEveryDt_[T](dt, f))).asInstanceOf[OnEveryDt_[T]]
}

case class OnceGreaterThan_[T <% Ordered[T]](source : Observable[T])
{
    type Element = (T, () => Unit)

    implicit object Ord extends Ordering[Element] {
        def compare(x: Element, y: Element) =
            -(x._1 compare y._1)
    }

    private val handlers = collection.mutable.PriorityQueue.empty[(T, () => Unit)]

    def += (trigger : T, handler : => Unit)
    {
        if (source.value.nonEmpty && source.value.get > trigger)
            handler
        else
            handlers enqueue ((trigger, () => handler))
    }

    source += {
        case None =>
        case Some(x) =>
            while (handlers.nonEmpty && handlers.head._1 < x)
                handlers.dequeue()._2()
    }
}

object OnceGreaterThan
{
    private val cache = mutable.HashMap.empty[Any,Any]

    def apply[T <% Ordered[T]](source : Observable[T]) =
        (cache getOrElseUpdate (source, new OnceGreaterThan_[T](source))).asInstanceOf[OnceGreaterThan_[T]]
}

case class OnceLessThan_[T <% Ordered[T]](source : Observable[T])
{
    type Element = (T, () => Unit)

    implicit object Ord extends Ordering[Element] {
        def compare(x: Element, y: Element) =
            +(x._1 compare y._1)
    }

    private val handlers = collection.mutable.PriorityQueue.empty[(T, () => Unit)]

    def += (trigger : T, handler : => Unit)
    {
        if (source.value.nonEmpty && source.value.get < trigger)
            handler
        else
            handlers enqueue ((trigger, () => handler))
    }

    source += {
        case None =>
        case Some(x) =>
            while (handlers.nonEmpty && handlers.head._1 > x)
                handlers.dequeue()._2()
    }
}

object OnceLessThan
{
    private val cache = mutable.HashMap.empty[Any,Any]

    def apply[T <% Ordered[T]](source : Observable[T]) =
        (cache getOrElseUpdate (source, new OnceLessThan_[T](source))).asInstanceOf[OnceLessThan_[T]]
}
