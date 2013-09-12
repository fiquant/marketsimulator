Events
======

.. contents::
    :local:
    :depth: 2
    :backlinks: none

Events in the simultator are conceptually close to events in C# or ``boost::signal`` in C++. Number of listeners can be subscribed for event notification using += operator and unsubscribed with -= operator. A listener should be a callable object that accepts a single argument - the source of the event (it allows not to store an event source in the listener and also use a single listener for several event sources at the same time). 

Event subscription
------------------

Since event subscription is often done at binding time and unadvising should be done at dispose time ``event.subscribe`` helper function was introduced to manage event subscription declaratively:  

.. code-block:: python

  class ProgressPrinter(object):
  
    def __init__(self):
      event.subscribe(event.Every(ops.constant(10)), # event source to subscribe to
                      _(self)._wakeUp,               # event listener
                      self)                          
      
    def _wakeUp(self, _):
      print '.'   # prints . every 10 units of time
      
Helpers
-------
      
``event.After`` and ``event.Every`` are used to represent a `single <scheduler.rst#generating-a-single-event>`_ and a `repeating  <scheduler.rst#generating-events-on-regular-basis>`_ action

``event.Array`` is used when several event sources are to be represented as a single event. For example,

.. code-block:: python

  event.Array([BestPrice(Asks(orderbook)), BestPrice(Bids(orderbook))])
  
fires an event once bid or ask of ``orderbook`` has changed.

Filtered events
---------------

Sometimes an event source (for example, price of an asset) has hundreds subscribers who check is the event source is less or greater than some value. In order to avoid excessive calls ``event.LessThan`` and ``event.GreaterThan`` classes are introduced. Event sources detect objects of these types and store them sorted in order to lookup relevant listeners very quickly. For example, 

.. code-block:: python 

  observable.MidPrice(orderbook) += event.LessThan(100, listener)
  
will call ``listener`` only if mid-price of the asset is less than 100.
