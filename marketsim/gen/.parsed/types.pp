
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

type IObservable[U] : IFunction[U]

type IOrderGenerator = IObservable[Order]

type ISingleAssetTrader

type IDifferentiable : IFunction[Float]

type CandleStick

type VolumeLevels

type Order
