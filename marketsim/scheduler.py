import heapq
from marketsim import Event

""" Module for managing discrete event simulation. 
"""

class _EventHandler(object):
    """ Internal class appending to a user event handler ability to cancel the event 
    """
    
    def __init__(self, handler):
        self._handler = handler
        self._cancelled = False

    def __call__(self):
        """ If the events is not cancelled, launches its handler
        """
        if not self._cancelled:
            self._handler()

    def cancel(self):
        """ Marks event as cancelled
        """
        self._cancelled = True

    @property
    def cancelled(self):
        """ Returns True iff the event is cancelled
        """
        return self._cancelled

    def __repr__(self):
        return "("+repr(self._handler) + ("-> Cancelled" if self.cancelled else "") + ")"

class Scheduler(object):
    """ Keeps a set of events to be launched in the future
    """

    def __init__(self):
        self.reset()

    def reset(self):
        """ Resets scheduler to the initial state: empty event set and T=0
        """
        self._elements = []
        self._currentTime = 0.
        self._counter = 0

    def __repr__(self):
        return "(t=" + str(self.currentTime) + ": " + repr(self._elements) + ")"

    @property
    def currentTime(self):
        """ Current simulation time        
        """
        return self._currentTime

    def schedule(self, actionTime, handler):
        """ Schedules an event given by 'handler' to be launched at 'actionTime'.
        Returns a function that can be called in order to cancel the event
        """
        assert actionTime >= self.currentTime
        eh = _EventHandler(handler)
        # in order to keep the right order of events having same action time
        # we differentiate them by incrementing counter 
        event = ((actionTime, self._counter), eh)
        self._counter += 1
        heapq.heappush(self._elements, event)
        return eh.cancel

    def scheduleAfter(self, dt, handler):
        """ Schedules an event given by 'handler' to be launched after 'dt' from now
        """
        self.schedule(self.currentTime + dt, handler)

    def workTill(self, limitTime):
        """ Launches all events with action time in range [currentTime, limitTime)
        in order of their action time and arrival order
        Postcondition: currentTime == limitTime and not exists e: actionTime(e) < limitTime
        """
        while (self._elements <> [] and self._elements[0][0][0] < limitTime):
            ((actionTime,_), eh) = heapq.heappop(self._elements)
            self._currentTime = actionTime
            eh()
        self._currentTime = limitTime

    def advance(self, dt):
        """ Makes the scheduler work 'dt' moments of time more
        """
        self.workTill(self.currentTime + dt)

    def process(self, intervalFunc, handler):
        """ 'intervalFunc' returns intervals of time between consequtive calls to handler
        """
        def h():
            handler()
            self.scheduleAfter(intervalFunc(), h)
        self.scheduleAfter(intervalFunc(), h)

world = Scheduler()
""" Global object representing simulation clock.
"""

class Timer(object):
    """ Event wrapper over Scheduler.process.
    'intervalFunc' defines intervals between moments of time 
    when subscribed listeners are to be called  
    """

    def __init__(self, intervalFunc):
        self.on_timer = Event()
        world.process(intervalFunc, lambda: self.on_timer.fire(self))

    def advise(self, listener):
        """ Subscribes 'listener' to be called when on_timer event occurs
        """
        self.on_timer += listener

