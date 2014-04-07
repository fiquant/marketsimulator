
type Optional[T]

type List[T]

type Any

type String

type Boolean

type Float

type Int : Float

type Volume = Int

type Price = Float

type IFunction[T] = () => T

type Function[T] : IFunction[T]

type IEvent

type IObservable[U] : IFunction[U], IEvent

type Observable[U] : IObservable[U]

type IOrderQueue

type IOrderBook

type ILink

type ITwoWayLink

type IOrder

type IOrderGenerator = IObservable[IOrder]

type ITrader

type IAccount

type ISingleAssetTrader : IAccount, ITrader

type IDifferentiable : IFunction[Float]

type ICandleStick

type IVolumeLevels

type ISingleAssetStrategy

type IMultiAssetStrategy

type IGraph

type ITimeSerie
