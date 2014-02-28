
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

type IStatDomain

type Cumulative(source = .const(0.0)) : IStatDomain

@label = "EW_{%(alpha)s}(%(source)s)"
type EW(source = .const(0.0),alpha = 0.015) : IStatDomain

@label = "Moving_{%(timeframe)s}(%(source)s)"
type Moving(source = .const(0.0),timeframe = 100.0) : IStatDomain
