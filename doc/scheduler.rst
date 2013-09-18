Discrete event simulation components
====================================

.. contents::
    :local:
    :depth: 2
    :backlinks: none

The main class for every discrete event simulation system is a scheduler that maintains a set of actions to fulfill in future and launches them according their action times: from the older ones to newer ones. The scheduler in the simulator is implemented as a heap data structure in order to perform frequent operations very fast. A classical heap allows inserts into at O(logN), extracting the best element at O(logN) and accessing to the best element at O(1). A bucket-based implementation may be introduced in order to improve performance provided that the distribution of event times should be known beforehand.

Scheduler
---------

``Scheduler`` class provides following interface:

.. code-block :: python

    class Scheduler(object):
    
        # cleans up event queue and resets simulation time to 0 
        def reset(self)         
        
        @property
        def currentTime(self)
        
        # schedules an event given by 'handler' to be launched at 'actionTime'
        def schedule(self, actionTime, handler)
        
        # schedules an event given by 'handler' to be launched after 'dt' from now
        def scheduleAfter(self, dt, handler):
            self.schedule(self.currentTime + dt, handler)
        
        # runs 'handler' asynchronously
        def async(self, handler): 
            self.scheduleAfter(0, handler)
            
        # Launches all events with action time in range [currentTime, limitTime)
        # in order of their action time and arrival order
        # Postcondition: currentTime == limitTime and not exists e: actionTime(e) < limitTime
        def workTill(self, limitTime)
        
        # Makes the scheduler work 'dt' moments of time more
        def advance(self, dt)
            self.workTill(self.currentTime + dt)

In order to schedule an event a user should use ``schedule`` or ``scheduleAfter`` methods passing there an event handler which should be given as a callable object (a function, a method, a lambda expression or an object exposing ``__call__`` method). 

Methods ``workTill`` and ``advance`` advance model time calling event handlers in order of their action times. If two events have same action time it is garanteed that the event scheduled first will be executed first. These methods must not be called from an event handler. In such a case an exception will be issued.

Components willing to have an access to the scheduler should acquire a reference to it at binding time:

.. code-block:: python

    def bind(self, ctx):
        self._scheduler = ctx.world

Convenience classes
-------------------

There are several classes granting convenient access to the scheduler and thus removing need for explicit binding against ``ctx.world``.

Current simulation time
~~~~~~~~~~~~~~~~~~~~~~~

.. |lambda| unicode:: U+003BB .. GREEK SMALL LETTER LAMDA

For example, 

.. code-block:: python  
    
    (observable.CurrentTime() < 200)[Side.Sell, Side.Buy]

returns ``Side.Sell`` if simulation time is less than 200 and ``Side.Buy`` otherwise

Generating events on regular basis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``event.Every`` represents some repeating action. It is initialized by a function defining interval of time to the next event invocation. 

For example, sample path for a Poisson process with |lambda| =1 can
be obtained in the following way:

.. code-block:: python

    from marketsim import mathutils, event, observable, _, ops
    
    class CurrentTimePrinter(object):
    
        def __init__(self):
            self._currentTime = observable.CurrentTime()
            event.subscribe(event.Every(mathutils.rnd.expovariate(1.)), 
                            _(self)._print, self)
            
        _internals = ['_currentTime']
        
        def _print(self, _):
            print self._currentTime()

when added to a simulation will print

::

    0.313908407622
    0.795173273046
    1.50151801647
    3.52280681834
    6.30719707516
    8.48277712333

Generating a single event
~~~~~~~~~~~~~~~~~~~~~~~~~

``event.After`` generates a single event at some time in the future.
