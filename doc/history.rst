Evolution of the simulator
--------------------------

.. _`Anton Kolotaev`: https://github.com/antonkolotaev
.. _`Karol Podkanski`: https://github.com/koalainparis

1. Initial `C++ version <http://sourceforge.net/p/marketsimulator/svn/HEAD/tree/Simulator/>`_ was developed in 2009-2011 by Riadh Zaatour.
2. In order to improve its extensibility and performance the simulator was `rewritten <https://github.com/antonkolotaev/v2>`_ using C++ template metaprogramming techniques by `Anton Kolotaev`_ in 2012. Python bindings to it were implemented using Boost.Python. Unfortunately the price for providing high extensibility with no overhead was quite high: in order to use it a proficiency in C++ template metaprogramming was required.
3. A new pure Python version was designed and developed in 2013 by `Anton Kolotaev`_. The main idea of its design is representation of a simulation model as a composition of simple and compound modules. You may read the `rationale <rationale.rst>`_ for the modular design and consult the `list of modules <modules.rst>`_ currently implemented in the simulator.
4. A web interface allowing to set up model parameters and launch the simulation was developed by `Anton Kolotaev`_ in JavaScript using `KnockoutJs <http://knockoutjs.com/>`_ as MVVM framework and `Highstock <http://www.highcharts.com/products/highstock>`_ as graph visualisation library.
5. `Karol Podkanski`_ has implemented number of trading strategies and indicators during his internship at summer 2013 (initial implementation for Relative Strength Index, Bollinger Bands, Market Data and Market Maker strategies, StopLoss meta order, statistical indicators and adaptors for existing statistics packages: `pandas <http://pandas.pydata.org/>`_ and `ta-lib <http://ta-lib.org/>`_)

A dedicated language for module abstract description is been developed. A compiler from this language will generate Python implementations for compound modules and also all meta information about available modules needed for the Web interface. It will be possible to edit code in this dedicated language online thus making the Web interface powerful as the offline version. An optimized C++ implementation for compound modules will be generated automatically.
