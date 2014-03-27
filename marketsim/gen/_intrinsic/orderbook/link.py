import random
from marketsim import scheduler

class Link_Impl(object):
    """ Represents latency in information propagation from one agent to another one
        (normally between a trader and a market).
        Ensures that sending packets via a link preserves their order.

        Parameters:

        **latency**
            function called for each packet in order to determine
            when it will appear at the destination point
    """

    def __init__(self):
        """ Initializes the link with a latency function
        """
        self._scheduler = scheduler.current()
        self.reset()

    def reset(self):
        self._lastT = 0

    def send(self, func):
        """ "Sends" data via link.
        After latency() moments of time 'func' will be called
        If there is another function that is scheduled for later time
        we adjust action time of 'func' in order to preserve their order
        """
        t = self._scheduler.currentTime + self.latency()
        if t < self._lastT:
            t = self._lastT
        self._lastT = t
        self._scheduler.schedule(t, func)

class TwoWayLink_Impl(object):
    """ Represents latency in information propagation between two agents
        (normally between a trader and a market).
        Ensures that sending packets via links preserves their order.
        Holds two one-way links in opposite directions.

        Parameters:

        **up**
            Forward link (normally from a trader to a market)

        **down**
            Backward link (normally from a market to a trader)
    """

