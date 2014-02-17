/**
 * Optional type is used internally to specify a type of a parameter having a default argument.
 * For any T: (T canBeCasted Optional[T])
 */
type Optional[T]

/**
 * List containing values of type T
 * For any T, U: (T canBeCasted U) => (List[T] canBeCasted List[U])
 * Constructor: [e1, e2, ... eN] construct a List[T]:
 *  if exists T: exists i: decltype(ei) is T and for any j: (decltype(ej) canBeCasted decltype(ei))
 * [] has type List[Nothing]
 * Nothing is a special internal type that can be casted to any type
 */
// TODO: find the bottommost type that all ei can be casted to
type List[T]

/**
 * Topmost type.
 * For any T: (T canBeCasted Any)
 */
type Any

/**
 *  String literal
 */
type String

/**
 *  Boolean value. 'true' and 'false' functions are used to construct literals of type () => Boolean
 */
type Boolean
type Float
type Int : Float

type Volume = Int
type Price = Float


// Alias for a nullary function returning value of type T
type IFunction[T] = () => T

type Function[T] : IFunction[T]

type IEvent
type IObservable[U] : IFunction[U], IEvent

type Observable[U] : IObservable[U]

type IOrderQueue
type IOrderBook

type ILink
type ITwoWayLink

type IOrderGenerator = IObservable[Order]

type ITrader
type IAccount
type ISingleAssetTrader : IAccount, ITrader

type IDifferentiable : IFunction[Float]

type CandleStick
type IVolumeLevels
type Order

type ISingleAssetStrategy
type IMultiAssetStrategy

type IGraph
type ITimeSerie

