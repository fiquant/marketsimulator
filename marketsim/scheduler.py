import heapq, threading
from marketsim import Event, bind, meta

""" Module for managing discrete event simulation. 
"""

class _EventHandler(object):
    """ Internal class appending to a user event handler ability to cancel the event
    (this feature hasn't been used so far. do we really need it?) 
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
    
# Scheduler singleton. Initialized once Scheduler instance is created
_instance = None
_lock = threading.Lock()

class Scheduler(object):
    """ Keeps a set of events to be launched in the future
    """

    def __init__(self, currentTime = 0):
        self._reset()

    def __enter__(self):
        global _instance
        _lock.acquire()
        assert _instance == None
        _instance = self
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        global _instance
        assert _instance==self
        _instance = None
        _lock.release()
        
    def _reset(self):
        """ Resets scheduler to the initial state: empty event set and T=0
        """
        self._elements = []
        self._currentTime = 0.
        self._counter = 0
        self._working = False

    def __repr__(self):
        return "(t=" + str(self.currentTime) + ": " + repr(self._elements) + ")"

    @property
    def currentTime(self):
        """ Current simulation time        
        """
        return self._currentTime
    
    @property
    def label(self):
        return "scheduler"
    
    _properties = {'currentTime' : float}

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
        
    def step(self, limitTime):
        if (self._elements <> [] and self._elements[0][0][0] < limitTime):
            ((actionTime,_), eh) = heapq.heappop(self._elements)
            self._currentTime = actionTime
            print 't = ', actionTime
            eh()
            return True
        else:
            return False
        
    def workTill(self, limitTime):
        """ Launches all events with action time in range [currentTime, limitTime)
        in order of their action time and arrival order
        Postcondition: currentTime == limitTime and not exists e: actionTime(e) < limitTime
        """
        if self._working:
            raise Exception("Scheduler is already working")
        
        self._working = True
        while (self.step(limitTime)):
            pass
        self._currentTime = limitTime
        self._working = False

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
        
def create():
    return Scheduler()

def current():
    return _instance

""" Global object representing simulation clock.
"""

class Timer(Event):
    """ Represents a repeating action. 
    
        Parameters:
        
        *intervalFunc*
            intervals of time between moments when subscribed listeners are to be called  
    """

    def __init__(self, intervalFunc):
        Event.__init__(self)
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        self.intervalFunc = intervalFunc
        self._cancelled = False
        
    def bind(self, context):
        self._scheduler = context.world
        self.schedule()
        
    _properties = { 'intervalFunc' : meta.function((), float) }
        
    def schedule(self):
        self._scheduler.scheduleAfter(self.intervalFunc(), self._wakeUp)
        
    def reset(self):
        self.schedule()
        
    def _wakeUp_impl(self):
        if not self._cancelled:
            self.fire(self)
            self.schedule()

    def cancel(self):
        self._cancelled = True

