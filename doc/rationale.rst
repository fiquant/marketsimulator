Modular design
~~~~~~~~~~~~~~

Modules provide some functionality that can be reused. Their behaviour can be customized by changing their parameter values.
	
Simple modules 
	provide functionality which is considered elementary (so there is no reason to reuse part of it to implement other modules).

Compound modules 
	combine together other modules in some way and define their parameters based on its own parameters.

Simple modules are implemented as functions or classes in a general purpose language like Python or C++ while compound modules can be described in a domain specific language (currently it is a Python subset but a dedicated language can be developed).
	
Structural vs procedural representation of complex behaviour
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Representing complex functionality as functions (or class methods) is natural for software engineers since it allows to use all power of a general purpose language and doesn't require studying new concepts.

Problems arise when we allow to a user to write an arbitrary code at the Web interface, since it would take a lot of effort to make sure that it cannot cause any damage to the server. (At .NET platform this code might be executed in an isolated AppDomain but our simulator is supposed to be cross-platform).

Representing a simulation model as a composition of predefined blocks (we will refer to it as an object graph) allows to solve this safety problem.

The object graph of a simulation can be represented for viewing and editing by a user as a property tree (current implementation) or as a block diagram (to be implemented).

A domain specific language to manipulate the object graph may be introduced.

Moreover, this structural representation facilitates high-level model optimisations since it is expressed in an easy-to-process way.
	
Performance considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

A simulation library must have a very modular design in order to provide a high level of flexibility to the user. This requirement comes from the original purpose of a simulation as a testbed for experiments with different models and parameters. 

In object-oriented languages various sorts of dynamic method invocation (virtual functions or dispatch methods) are used for module parametrisation. The dynamic nature of the calls hinders the compiler in performing many
useful optimisations. Finer grain modularity leads to smaller objects, and thus to a higher overhead, something known as abstraction penalty.

The C++ provides a solution to avoid this abstraction penalty while keeping modularity at high level: static polymorphism via class and function templates. However, such methods require expertise in C++ programming thus limiting the potential user base.

In order to achieve high performance (comparable with hand written C code), C++ template instantiations can be generated automatically from the abstract simulation model representation via an object graph. Only simple modules need to be reimplemented in C++; compound modules are represented already in an abstract way and C++ code for them can be generated automatically.
	
	
