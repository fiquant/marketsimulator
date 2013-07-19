import heapq, threading, collections, time, sys
from marketsim import types, Event, _, meta

class stat(collections.namedtuple('stat', ['events_processed', 'events_rate', 'processing_time'])):
    
    def __repr__(self):
        return str(self.events_processed) + ' events processed in ' + str(self.processing_time) + \
             's with rate ' + str(self.events_rate) + ' event/s'

""" Module for managing discrete event simulation. 
"""

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
        # in order to keep the right order of events having same action time
        # we differentiate them by incrementing counter 
        event = ((actionTime, self._counter), handler)
        self._counter += 1
        heapq.heappush(self._elements, event)

    def scheduleAfter(self, dt, handler):
        """ Schedules an event given by 'handler' to be launched after 'dt' from now
        """
        self.schedule(self.currentTime + dt, handler)
        
    def async(self, handler):
        self.schedule(self.currentTime, handler)
        
    def step(self, limitTime):
        if (self._elements <> [] and self._elements[0][0][0] < limitTime):
            ((actionTime,_), eh) = heapq.heappop(self._elements)
            self._currentTime = actionTime
            #print 't = ', actionTime
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
        
        t0 = time.clock()
        steps = 0
        
        self._working = True
        while (self.step(limitTime)):
            steps += 1
        self._currentTime = limitTime
        self._working = False
        
        dt = time.clock() - t0
        
        return stat(steps, steps / dt, dt)

    def advance(self, dt):
        """ Makes the scheduler work 'dt' moments of time more
        """
        self.workTill(self.currentTime + dt)
        
    def _process_impl(self, intervalFunc, handler):
        handler()
        self.scheduleAfter(intervalFunc(), 
                           _(self, intervalFunc, handler)._process_impl)

    def process(self, intervalFunc, handler):
        """ 'intervalFunc' returns intervals of time between consequtive calls to handler
        """
        self.scheduleAfter(intervalFunc(), 
                           _(self, intervalFunc, handler)._process_impl)
        
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
        self.intervalFunc = intervalFunc
        self._cancelled = False
        
    def bind(self, context):
        self._scheduler = context.world
        self.schedule()
        
    _properties = { 'intervalFunc' : types.IFunction[float] }
        
    def schedule(self):
        self._scheduler.scheduleAfter(self.intervalFunc(), _(self)._wakeUp)
        
    def reset(self):
        self.schedule()
        
    def _wakeUp(self):
        if not self._cancelled:
            self.fire(self)
            self.schedule()

    def cancel(self):
        self._cancelled = True

