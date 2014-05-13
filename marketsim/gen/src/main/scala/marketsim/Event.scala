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
