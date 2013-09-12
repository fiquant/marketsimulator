Events
======

Events in the simultator are conceptually close to events in C# or boost::signal in C++. Number of listeners can be subscribed for event notification using += operator and unsubscribed with -= operator. A listener should be a callable object that accepts a single argument - the source of the event (it allows not to store an event source in the listener and also use a single listener for several event sources at the same time). 

Since event subscription is often done at binding time and unadvising should be done at dispose time ``event.subscribe`` helper function was introduced to manage event subscription declaratively:  

.. code-block:: python

  class ProgressPrinter(object):
  
    def __init__(self):
      event.subscribe(event.Every(ops.constant(10)), # event source to subscribe to
                      _(self)._wakeUp,               # event listener
                      self)                          
      
    def _wakeUp(self, _):
      print '.'
      
``event.After`` and ``event.Every`` are used to represent a `single <scheduler.rst#generating-a-single-event>`_ and a `repeating  <scheduler.rst#generating-events-on-regular-basis>`_ action
