import heapq, threading, collections, time
from marketsim import _
import datetime

class stat(collections.namedtuple('stat', ['events_processed', 'events_rate', 'processing_time'])):
    
    def __repr__(self):
        return str(self.events_processed) + ' events processed in ' + str(self.processing_time) + \
             's with rate ' + str(self.events_rate) + ' event/s'

# Scheduler singleton. Initialized once Scheduler instance is created
_instance = None
_lock = threading.Lock()

from marketsim.gen._out._intrinsic_base.scheduler import Scheduler_Base

class Scheduler_Impl(Scheduler_Base):
    """ Keeps a set of events to be launched in the future
    """

    def __init__(self, currentTime=0.0, startTime=None, timeScale='seconds'):
        self._reset(currentTime, startTime)
        self._timeScale = timeScale
        from marketsim.gen._intrinsic.event import Event
        self.on_clock = Event()

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
        
    def _reset(self, currentTime=0.0, startTime=None):
        """ Resets scheduler to the initial state: empty event set and T=0
        """
        self._elements = []
        self.currentTime = currentTime
        self._startTime = datetime.datetime.now() if startTime is None else startTime
        self._counter = 0
        self.currentId = None
        self._working = False

    def reset(self):
        self._reset()

    def __repr__(self):
        return "(t=" + str(self.currentTime) + ": " + repr(self._elements) + ")"

    @property
    def startTime(self):
        """ DateTime object containing the time of the beginning of the simulation
        """
        return self._startTime

    def timeToOffset(self, abstractTime, timescale='seconds'):
        """ converts an abstract simulation time to a datetime.timedelta object
        """
        return datetime.timedelta(**{timescale: abstractTime})

    @property
    def now(self):
        """ Returns a datetime object containing the "real world" time
        """
        return self._startTime + self.timeToOffset(self.currentTime, self._timeScale)

    
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
            ((actionTime,eid), eh) = heapq.heappop(self._elements)
            self.currentId = eid
            self.currentTime = actionTime
            self.on_clock.fire(self)
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
        self.currentTime = limitTime
        self._working = False
        
        dt = time.clock() - t0
        
        return stat(steps, steps / dt if dt > 0 else -1, dt)

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
        
from marketsim.gen._out._intrinsic_base.scheduler import Scheduler_Base

class currentScheduler_Impl(Scheduler_Base):

    def bind_impl(self, ctx):
        self._scheduler = ctx.world

    def __getattr__(self, item):
        if item[0:2] != '__':
            return getattr(self._scheduler, item)
        else:
            raise AttributeError
