Discrete event simulation components
====================================

Main class for every discrete event simulation system is a scheduler
that maintains a set of actions to fulfill in future and launches them
according their action times: from older ones to newer. Normally
schedulers are implemented as some kind of a heap data structure in
order to perform frequent operations very fast. Classical heap allows
inserts into at O(logN), extracting the best element at O(logN) and
accessing to the best element at O(1).

Scheduler
---------

Scheduler class provides following interface:

::

    class Scheduler(object):
        def reset(self)
        def currentTime(self)
        def schedule(self, actionTime, handler)
        def scheduleAfter(self, dt, handler)
        def workTill(self, limitTime)
        def advance(self, dt)

In order to schedule an event a user should use or methods passing there
an event handler which should be given as a callable object (a function,
a method, lambda expression or a object exposing method). These
functions return a callable object which can be called in order to
cancel the scheduled event.

Methods and advance model time calling event handlers in order of their
action times. If two events have same action time it is garanteed that
the event scheduled first will be executed first. These methods must not
be called from an event handler. In such a case an exception will be
issued.

Since a scheduler is supposed to be single for non-parallel simulations,
for convenient use from other parts of the library static class is
introduced which grants access to , and methods of the unique scheduler.
This scheduler should be initialized by creating an instance of class in
client code ( method) and it gives right to manage simulation by calling
and methods.

Timer
-----

It is a convenience class designed to represent some repeating action.
It has following interface:

::

    class Timer(object):
        def __init__(self, intervalFunc):
            self.on_timer = Event()
            ...
        def advise(self, listener):
            self.on_timer += listener

It is initialized by a function defining interval of time to the next
event invocation. Event handler to be invoked should be passed to method
(there can be multiple listeners).

For example, sample path a Poisson process with :math:`\lambda`\ =1 can
be obtained in the following way:

::

    import random
    from marketsim.scheduler import Timer, world

    def F(timer):
        print world.currentTime
        
    Timer(lambda: random.expovariate(1.)).advise(F)

    world.advance(20)

will print

::

    0.313908407622
    0.795173273046
    1.50151801647
    3.52280681834
    6.30719707516
    8.48277712333

Note that is designed to be an event source and for previous example
there is a more convenient shortcut:

::

    world.process(lambda: random.expovariate(1.), F)
