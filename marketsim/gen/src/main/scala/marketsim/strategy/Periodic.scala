package marketsim.strategy

import marketsim.{Account, OrderFactory, IEvent}

class Periodic(account : Account, activation : IEvent, factory : OrderFactory)
{
    private def wakeUp()
    {
        account send factory.create
    }

    activation advise wakeUp
}
