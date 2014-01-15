
type Optional[T]

type List[T]

type Any

type Side

type String

type Boolean

type Float

type Int : Float

type Volume : Int

type Price : Float

type IOrderQueue

type IOrderBook

type IFunction[T] = () => T

type IEvent

type IObservable[U] : IFunction[U], IEvent

type IOrderGenerator = IObservable[Order]

type ITrader

type IAccount

type ISingleAssetTrader : IAccount, ITrader

type IDifferentiable : IFunction[Float]

type CandleStick

type VolumeLevels

type Order

type ISingleAssetStrategy

type IMultiAssetStrategy

type IGraph

type ITimeSerie
