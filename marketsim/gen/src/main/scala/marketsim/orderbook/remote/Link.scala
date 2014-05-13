package marketsim.orderbook.remote

import marketsim.Time

class Link(latency : () => Time)
{
    private var readyAt = -1.0

    def send(x : => Unit)
    {
        import marketsim.Scheduler._
        val t = currentTime + latency() max readyAt
        readyAt = t
        schedule(t, x)
    }
}

class TwoWayLink(upLatency   : () => Time = () => 0.001,
                 downLatency : () => Time = () => 0.001)
{
    val up = new Link(upLatency)
    val down = new Link(downLatency)
}
