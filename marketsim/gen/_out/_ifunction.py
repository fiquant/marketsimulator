from marketsim import meta
IFunction = {}
class IFunctionobject(object):
    _types = [meta.function((),object)]


IFunction[object] = IFunctionobject


from marketsim.types import Function_impl
class IFunctionint(Function_impl):
    _types = [meta.function((),int)]


IFunction[int] = IFunctionint


from marketsim.gen._out._side import Side
class IFunctionSide(object):
    _types = [meta.function((),Side)]


IFunction[Side] = IFunctionSide


from marketsim.types import Function_impl
class IFunctionfloat(Function_impl):
    _types = [meta.function((),float)]


IFunction[float] = IFunctionfloat


class IFunctionstr(object):
    _types = [meta.function((),str)]


IFunction[str] = IFunctionstr


from marketsim.gen._out._iorder import IOrder
class IFunctionIOrder(object):
    _types = [meta.function((),IOrder)]


IFunction[IOrder] = IFunctionIOrder


class IFunctionbool(object):
    _types = [meta.function((),bool)]


IFunction[bool] = IFunctionbool


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIOrderBook(object):
    _types = [meta.function((),IOrderBook)]


IFunction[IOrderBook] = IFunctionIOrderBook


class IFunctionIFunctionint(object):
    _types = [meta.function((),IFunctionint)]


IFunction[IFunctionint] = IFunctionIFunctionint


from marketsim import listOf
class IFunctionlistOffloat(object):
    _types = [meta.function((),listOf(float))]


IFunction[listOf(float)] = IFunctionlistOffloat


from marketsim.gen._out._icandlestick import ICandleStick
class IFunctionICandleStick(object):
    _types = [meta.function((),ICandleStick)]


IFunction[ICandleStick] = IFunctionICandleStick


class IFunctionIFunctionSide(object):
    _types = [meta.function((),IFunctionSide)]


IFunction[IFunctionSide] = IFunctionIFunctionSide


class IFunctionIFunctionfloat(object):
    _types = [meta.function((),IFunctionfloat)]


IFunction[IFunctionfloat] = IFunctionIFunctionfloat


from marketsim.gen._out._test.types._r import R
class IFunctionR(object):
    _types = [meta.function((),R)]


IFunction[R] = IFunctionR


from marketsim.gen._out._test.types._u import U
class IFunctionU(object):
    _types = [meta.function((),U)]


IFunction[U] = IFunctionU


from marketsim.gen._out._test.types._t import T
class IFunctionT(object):
    _types = [meta.function((),T)]


IFunction[T] = IFunctionT


from marketsim.gen._out._ivolumelevels import IVolumeLevels
class IFunctionIVolumeLevels(object):
    _types = [meta.function((),IVolumeLevels)]


IFunction[IVolumeLevels] = IFunctionIVolumeLevels


class IFunctionIFunctionbool(object):
    _types = [meta.function((),IFunctionbool)]


IFunction[IFunctionbool] = IFunctionIFunctionbool


class IFunctionstr(object):
    _types = [meta.function((),str)]


IFunction[str] = IFunctionstr


from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableint(object):
    _types = [meta.function((),IObservableint)]


IFunction[IObservableint] = IFunctionIObservableint


from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionISingleAssetTrader(object):
    _types = [meta.function((),ISingleAssetTrader)]


IFunction[ISingleAssetTrader] = IFunctionISingleAssetTrader


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSide(object):
    _types = [meta.function((),IObservableSide)]


IFunction[IObservableSide] = IFunctionIObservableSide


from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
class IFunctionIMultiAssetStrategy(object):
    _types = [meta.function((),IMultiAssetStrategy)]


IFunction[IMultiAssetStrategy] = IFunctionIMultiAssetStrategy


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategy(object):
    _types = [meta.function((),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy] = IFunctionISingleAssetStrategy


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((IAccount,),IFunctionfloat)]


IFunction[IFunctionfloat,(IAccount,)] = IFunctionIFunctionfloatIAccount


class IFunctionstrstr(object):
    _types = [meta.function((str,),str)]


IFunction[str,(str,)] = IFunctionstrstr


from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservablebool(object):
    _types = [meta.function((),IObservablebool)]


IFunction[IObservablebool] = IFunctionIObservablebool


from marketsim.gen._out._igraph import IGraph
class IFunctionIGraphstr(object):
    _types = [meta.function((str,),IGraph)]


IFunction[IGraph,(str,)] = IFunctionIGraphstr


class IFunctionIFunctionintIFunctionint(object):
    _types = [meta.function((IFunctionint,),IFunctionint)]


IFunction[IFunctionint,(IFunctionint,)] = IFunctionIFunctionintIFunctionint


class IFunctionIFunctionintint(object):
    _types = [meta.function((int,),IFunctionint)]


IFunction[IFunctionint,(int,)] = IFunctionIFunctionintint


class IFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]


IFunction[IFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
class IFunctionIEventIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IEvent)]


IFunction[IEvent,(IFunctionfloat,)] = IFunctionIEventIFunctionfloat


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIOrderBookIAccount(object):
    _types = [meta.function((IAccount,),IOrderBook)]


IFunction[IOrderBook,(IAccount,)] = IFunctionIOrderBookIAccount


class IFunctionIFunctionfloatfloat(object):
    _types = [meta.function((float,),IFunctionfloat)]


IFunction[IFunctionfloat,(float,)] = IFunctionIFunctionfloatfloat


class IFunctionIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((),IFunctionIFunctionfloatIAccount)]


IFunction[IFunctionIFunctionfloatIAccount] = IFunctionIFunctionIFunctionfloatIAccount


from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintint(object):
    _types = [meta.function((int,),IObservableint)]


IFunction[IObservableint,(int,)] = IFunctionIObservableintint


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIOrderQueueIOrderBook(object):
    _types = [meta.function((IOrderBook,),IOrderQueue)]


IFunction[IOrderQueue,(IOrderBook,)] = IFunctionIOrderQueueIOrderBook


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionSide,)] = IFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IFunctionfloat)]


IFunction[IFunctionfloat,(IOrderBook,)] = IFunctionIFunctionfloatIOrderBook


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionSide)]


IFunction[IFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._ilink import ILink
class IFunctionILinkIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),ILink)]


IFunction[ILink,(IObservablefloat,)] = IFunctionILinkIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatfloat(object):
    _types = [meta.function((float,),IObservablefloat)]


IFunction[IObservablefloat,(float,)] = IFunctionIObservablefloatfloat


class IFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]


IFunction[IFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloat


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIAccount(object):
    _types = [meta.function((IAccount,),IObservableint)]


IFunction[IObservableint,(IAccount,)] = IFunctionIObservableintIAccount


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservableint)]


IFunction[IObservableint,(IOrderBook,)] = IFunctionIObservableintIOrderBook


from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIAccount(object):
    _types = [meta.function((IAccount,),IObservablefloat)]


IFunction[IObservablefloat,(IAccount,)] = IFunctionIObservablefloatIAccount


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iaccount import IAccount
class IFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,),IAccount)]


IFunction[IAccount,(ISingleAssetStrategy,)] = IFunctionIAccountISingleAssetStrategy


from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIFunctionfloatIDifferentiable(object):
    _types = [meta.function((IDifferentiable,),IFunctionfloat)]


IFunction[IFunctionfloat,(IDifferentiable,)] = IFunctionIFunctionfloatIDifferentiable


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservableint
class IFunctionIObservableintIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservableint)]


IFunction[IObservableint,(IOrderQueue,)] = IFunctionIObservableintIOrderQueue


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservablefloat)]


IFunction[IObservablefloat,(IOrderBook,)] = IFunctionIObservablefloatIOrderBook


from marketsim import listOf
class IFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionlistOffloat)]


IFunction[IFunctionlistOffloat,(listOf(float),)] = IFunctionIFunctionlistOffloatlistOffloat


class IFunctionintIFunctionICandleStickint(object):
    _types = [meta.function((IFunctionICandleStick,int,),int)]


IFunction[int,(IFunctionICandleStick,int,)] = IFunctionintIFunctionICandleStickint


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservablefloat)]


IFunction[IObservablefloat,(IOrderQueue,)] = IFunctionIObservablefloatIOrderQueue


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IAccount,float,)] = IFunctionIFunctionfloatIAccountfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionSide,)] = IFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IFunctionfloat,)] = IFunctionISingleAssetStrategyIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat] = IFunctionIFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IFunctionfloat)]


IFunction[IFunctionfloat,(IObservablefloat,)] = IFunctionIFunctionfloatIObservablefloat


class IFunctionIFunctionUIFunctionT(object):
    _types = [meta.function((IFunctionT,),IFunctionU)]


IFunction[IFunctionU,(IFunctionT,)] = IFunctionIFunctionUIFunctionT


class IFunctionIFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((),IFunctionIFunctionfloatIFunctionfloat)]


IFunction[IFunctionIFunctionfloatIFunctionfloat] = IFunctionIFunctionIFunctionfloatIFunctionfloat


class IFunctionIFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((float,),IFunctionIFunctionfloatIAccount)]


IFunction[IFunctionIFunctionfloatIAccount,(float,)] = IFunctionIFunctionIFunctionfloatIAccountfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IDifferentiable)]


IFunction[IDifferentiable,(IObservablefloat,)] = IFunctionIDifferentiableIObservablefloat


from marketsim.gen._out._ilink import ILink
from marketsim.gen._out._itwowaylink import ITwoWayLink
class IFunctionITwoWayLinkILinkILink(object):
    _types = [meta.function((ILink,ILink,),ITwoWayLink)]


IFunction[ITwoWayLink,(ILink,ILink,)] = IFunctionITwoWayLinkILinkILink


class IFunctionIFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((),IFunctionIAccountISingleAssetStrategy)]


IFunction[IFunctionIAccountISingleAssetStrategy] = IFunctionIFunctionIAccountISingleAssetStrategy


class IFunctionIFunctionfloatfloatfloat(object):
    _types = [meta.function((float,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(float,float,)] = IFunctionIFunctionfloatfloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablefloat,)] = IFunctionIObservablefloatIObservablefloat


class IFunctionIFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((),IFunctionIFunctionlistOffloatlistOffloat)]


IFunction[IFunctionIFunctionlistOffloatlistOffloat] = IFunctionIFunctionIFunctionlistOffloatlistOffloat


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iaccount import IAccount
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IAccount,float,)] = IFunctionIFunctionfloatIAccountfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIObservableIOrder(object):
    _types = [meta.function((IObservableIOrder,),IObservableIOrder)]


IFunction[IObservableIOrder,(IObservableIOrder,)] = IFunctionIObservableIOrderIObservableIOrder


class IFunctionIFunctionRIFunctionT(object):
    _types = [meta.function((IFunctionT,),IFunctionR)]


IFunction[IFunctionR,(IFunctionT,)] = IFunctionIFunctionRIFunctionT


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBookfloat(object):
    _types = [meta.function((IOrderBook,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IOrderBook,float,)] = IFunctionIFunctionfloatIOrderBookfloat


class IFunctionIFunctionSideIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IFunctionSide)]


IFunction[IFunctionSide,(IFunctionfloat,float,)] = IFunctionIFunctionSideIFunctionfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


class IFunctionIFunctionfloatIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IFunctionfloat,float,)] = IFunctionIFunctionfloatIFunctionfloatfloat


from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIFunctionfloatIOrderQueuefloat(object):
    _types = [meta.function((IOrderQueue,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IOrderQueue,float,)] = IFunctionIFunctionfloatIOrderQueuefloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyfloatfloat(object):
    _types = [meta.function((float,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(float,float,)] = IFunctionISingleAssetStrategyfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iorderqueue import IOrderQueue
class IFunctionIOrderQueueIOrderBookIFunctionSide(object):
    _types = [meta.function((IOrderBook,IFunctionSide,),IOrderQueue)]


IFunction[IOrderQueue,(IOrderBook,IFunctionSide,)] = IFunctionIOrderQueueIOrderBookIFunctionSide


class IFunctionIFunctionIFunctionfloatIFunctionfloatfloat(object):
    _types = [meta.function((float,),IFunctionIFunctionfloatIFunctionfloat)]


IFunction[IFunctionIFunctionfloatIFunctionfloat,(float,)] = IFunctionIFunctionIFunctionfloatIFunctionfloatfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategy(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategy


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSidefloatIOrderBook(object):
    _types = [meta.function((float,IOrderBook,),IObservableSide)]


IFunction[IObservableSide,(float,IOrderBook,)] = IFunctionIObservableSidefloatIOrderBook


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionfloat,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionfloatIFunctionfloat


class IFunctionIFunctionfloatIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionfloat)]


IFunction[IFunctionfloat,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatfloatIFunctionfloat(object):
    _types = [meta.function((float,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(float,IFunctionfloat,)] = IFunctionIObservablefloatfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionbool)]


IFunction[IFunctionbool,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionboolIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IObservablefloat,float,)] = IFunctionIFunctionfloatIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IDifferentiable)]


IFunction[IDifferentiable,(IObservablefloat,float,)] = IFunctionIDifferentiableIObservablefloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionfloat,IOrderBook,),IObservableSide)]


IFunction[IObservableSide,(IFunctionfloat,IOrderBook,)] = IFunctionIObservableSideIFunctionfloatIOrderBook


class IFunctionIFunctionfloatfloatfloatfloat(object):
    _types = [meta.function((float,float,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(float,float,float,)] = IFunctionIFunctionfloatfloatfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBookIFunctionfloat(object):
    _types = [meta.function((IOrderBook,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(IOrderBook,IFunctionfloat,)] = IFunctionIObservablefloatIOrderBookIFunctionfloat


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueueIFunctionfloat(object):
    _types = [meta.function((IOrderQueue,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(IOrderQueue,IFunctionfloat,)] = IFunctionIObservablefloatIOrderQueueIFunctionfloat


class IFunctionIFunctionTIFunctionintIFunctionfloat(object):
    _types = [meta.function((IFunctionint,IFunctionfloat,),IFunctionT)]


IFunction[IFunctionT,(IFunctionint,IFunctionfloat,)] = IFunctionIFunctionTIFunctionintIFunctionfloat


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableSide)]


IFunction[IObservableSide,(IObservablefloat,float,)] = IFunctionIObservableSideIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablefloat,float,)] = IFunctionIObservablefloatIObservablefloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionSidefloatfloatIOrderBook(object):
    _types = [meta.function((float,float,IOrderBook,),IFunctionSide)]


IFunction[IFunctionSide,(float,float,IOrderBook,)] = IFunctionIFunctionSidefloatfloatIOrderBook


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIObservableIOrderIFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionfloatIOrderBookfloatfloat(object):
    _types = [meta.function((IOrderBook,float,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IOrderBook,float,float,)] = IFunctionIFunctionfloatIOrderBookfloatfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionISingleAssetStrategyIObservableIOrderIEvent(object):
    _types = [meta.function((IObservableIOrder,IEvent,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IObservableIOrder,IEvent,)] = IFunctionISingleAssetStrategyIObservableIOrderIEvent


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIObservablefloatIOrderBook(object):
    _types = [meta.function((IObservablefloat,IOrderBook,),IObservableSide)]


IFunction[IObservableSide,(IObservablefloat,IOrderBook,)] = IFunctionIObservableSideIObservablefloatIOrderBook


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderBookIObservablefloat(object):
    _types = [meta.function((IOrderBook,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IOrderBook,IObservablefloat,)] = IFunctionIObservablefloatIOrderBookIObservablefloat


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIOrderQueueIObservablefloat(object):
    _types = [meta.function((IOrderQueue,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IOrderQueue,IObservablefloat,)] = IFunctionIObservablefloatIOrderQueueIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionfloat,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionfloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatstrstrstr(object):
    _types = [meta.function((str,str,str,),IObservablefloat)]


IFunction[IObservablefloat,(str,str,str,)] = IFunctionIObservablefloatstrstrstr


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._iobservable import IObservableICandleStick
class IFunctionIObservableICandleStickIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableICandleStick)]


IFunction[IObservableICandleStick,(IObservablefloat,float,)] = IFunctionIObservableICandleStickIObservablefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablebool)]


IFunction[IObservablebool,(IObservablefloat,IFunctionfloat,)] = IFunctionIObservableboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class IFunctionIObservableIOrderIFunctionfloatIObservableIOrder(object):
    _types = [meta.function((IFunctionfloat,IObservableIOrder,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionfloat,IObservableIOrder,)] = IFunctionIObservableIOrderIFunctionfloatIObservableIOrder


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionfloat,IObservablefloat,),IObservablebool)]


IFunction[IObservablebool,(IFunctionfloat,IObservablefloat,)] = IFunctionIObservableboolIFunctionfloatIObservablefloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionbool(object):
    _types = [meta.function((ISingleAssetStrategy,IFunctionbool,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,IFunctionbool,)] = IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionbool


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IObservablefloat,float,float,)] = IFunctionIFunctionfloatIObservablefloatfloatfloat


from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIOrderBookfloatIOrderBook(object):
    _types = [meta.function((IOrderBook,float,IOrderBook,),IObservableSide)]


IFunction[IObservableSide,(IOrderBook,float,IOrderBook,)] = IFunctionIObservableSideIOrderBookfloatIOrderBook


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatIObservablefloatISingleAssetTrader(object):
    _types = [meta.function((IObservablefloat,ISingleAssetTrader,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablefloat,ISingleAssetTrader,)] = IFunctionIObservablefloatIObservablefloatISingleAssetTrader


class IFunctionIFunctionSideIFunctionboolIFunctionSideIFunctionSide(object):
    _types = [meta.function((IFunctionbool,IFunctionSide,IFunctionSide,),IFunctionSide)]


IFunction[IFunctionSide,(IFunctionbool,IFunctionSide,IFunctionSide,)] = IFunctionIFunctionSideIFunctionboolIFunctionSideIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIObservablefloatIObservablefloat


from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._ivolumelevels import IVolumeLevels
from marketsim.gen._out._iobservable import IObservableIVolumeLevels
class IFunctionIObservableIVolumeLevelsIOrderQueuefloatint(object):
    _types = [meta.function((IOrderQueue,float,int,),IObservableIVolumeLevels)]


IFunction[IObservableIVolumeLevels,(IOrderQueue,float,int,)] = IFunctionIObservableIVolumeLevelsIOrderQueuefloatint


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablefloat,IObservablefloat,),IObservablebool)]


IFunction[IObservablebool,(IObservablefloat,IObservablefloat,)] = IFunctionIObservableboolIObservablefloatIObservablefloat


from marketsim import listOf
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._itwowaylink import ITwoWayLink
class IFunctionIOrderBookIOrderBookITwoWayLinklistOfITimeSerie(object):
    _types = [meta.function((IOrderBook,ITwoWayLink,listOf(ITimeSerie),),IOrderBook)]


IFunction[IOrderBook,(IOrderBook,ITwoWayLink,listOf(ITimeSerie),)] = IFunctionIOrderBookIOrderBookITwoWayLinklistOfITimeSerie


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,ISingleAssetStrategy,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,ISingleAssetStrategy,)] = IFunctionISingleAssetStrategyISingleAssetStrategyISingleAssetStrategy


class IFunctionIFunctionfloatIFunctionboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionbool,IFunctionfloat,IFunctionfloat,),IFunctionfloat)]


IFunction[IFunctionfloat,(IFunctionbool,IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionfloatIFunctionboolIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIFunctionSidefloatfloatfloatIOrderBook(object):
    _types = [meta.function((float,float,float,IOrderBook,),IFunctionSide)]


IFunction[IFunctionSide,(float,float,float,IOrderBook,)] = IFunctionIFunctionSidefloatfloatfloatIOrderBook


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIObservableIOrderIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iobservable import IObservableobject
from marketsim.gen._out._igraph import IGraph
from marketsim.gen._out._itimeserie import ITimeSerie
class IFunctionITimeSerieIObservableobjectIGraphintint(object):
    _types = [meta.function((IObservableobject,IGraph,int,int,),ITimeSerie)]


IFunction[ITimeSerie,(IObservableobject,IGraph,int,int,)] = IFunctionITimeSerieIObservableobjectIGraphintint


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,IFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IFunctionSide,IFunctionfloat,IFunctionfloat,)] = IFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat


from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim import listOf
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIOrderBookstrfloatintlistOfITimeSerie(object):
    _types = [meta.function((str,float,int,listOf(ITimeSerie),),IOrderBook)]


IFunction[IOrderBook,(str,float,int,listOf(ITimeSerie),)] = IFunctionIOrderBookstrfloatintlistOfITimeSerie


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionSide,IFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIFunctionSideIFunctionSide(object):
    _types = [meta.function((IObservablebool,IFunctionSide,IFunctionSide,),IObservableSide)]


IFunction[IObservableSide,(IObservablebool,IFunctionSide,IFunctionSide,)] = IFunctionIObservableSideIObservableboolIFunctionSideIFunctionSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionboolIObservableSideIFunctionSide(object):
    _types = [meta.function((IFunctionbool,IObservableSide,IFunctionSide,),IObservableSide)]


IFunction[IObservableSide,(IFunctionbool,IObservableSide,IFunctionSide,)] = IFunctionIObservableSideIFunctionboolIObservableSideIFunctionSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
class IFunctionIObservableSideIFunctionboolIFunctionSideIObservableSide(object):
    _types = [meta.function((IFunctionbool,IFunctionSide,IObservableSide,),IObservableSide)]


IFunction[IObservableSide,(IFunctionbool,IFunctionSide,IObservableSide,)] = IFunctionIObservableSideIFunctionboolIFunctionSideIObservableSide


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatfloatIObservablefloatISingleAssetTrader(object):
    _types = [meta.function((float,IObservablefloat,ISingleAssetTrader,),IObservablefloat)]


IFunction[IObservablefloat,(float,IObservablefloat,ISingleAssetTrader,)] = IFunctionIObservablefloatfloatIObservablefloatISingleAssetTrader


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionbool,IFunctionfloat,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IFunctionbool,IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionboolIFunctionfloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IObservablebool,IFunctionfloat,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablebool,IFunctionfloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservableboolIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IFunctionbool,IObservablefloat,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(IFunctionbool,IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIFunctionboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatfloatIFunctionfloatIFunctionfloatstr(object):
    _types = [meta.function((float,IFunctionfloat,IFunctionfloat,str,),IObservablefloat)]


IFunction[IObservablefloat,(float,IFunctionfloat,IFunctionfloat,str,)] = IFunctionIObservablefloatfloatIFunctionfloatIFunctionfloatstr


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._iorder import IOrder
class IFunctionIObservableIOrderIObservablefloatIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionIObservableIOrderIFunctionfloat,),IObservableIOrder)]


IFunction[IObservableIOrder,(IObservablefloat,IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIObservableIOrderIObservablefloatIFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionSide,float,IFunctionfloat,IOrderBook,),IObservablefloat)]


IFunction[IObservablefloat,(IFunctionSide,float,IFunctionfloat,IOrderBook,)] = IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide(object):
    _types = [meta.function((IObservablebool,IFunctionSide,IObservableSide,),IObservableSide)]


IFunction[IObservableSide,(IObservablebool,IFunctionSide,IObservableSide,)] = IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIFunctionboolIObservableSideIObservableSide(object):
    _types = [meta.function((IFunctionbool,IObservableSide,IObservableSide,),IObservableSide)]


IFunction[IObservableSide,(IFunctionbool,IObservableSide,IObservableSide,)] = IFunctionIObservableSideIFunctionboolIObservableSideIObservableSide


from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservablebool
class IFunctionIObservableSideIObservableboolIObservableSideIFunctionSide(object):
    _types = [meta.function((IObservablebool,IObservableSide,IFunctionSide,),IObservableSide)]


IFunction[IObservableSide,(IObservablebool,IObservableSide,IFunctionSide,)] = IFunctionIObservableSideIObservableboolIObservableSideIFunctionSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IFunctionfloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablebool,IObservablefloat,IFunctionfloat,)] = IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IObservablebool,IFunctionfloat,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablebool,IFunctionfloat,IObservablefloat,)] = IFunctionIObservablefloatIObservableboolIFunctionfloatIObservablefloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IFunctionbool,IObservablefloat,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IFunctionbool,IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategystrstrstrfloatfloat(object):
    _types = [meta.function((str,str,str,float,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(str,str,str,float,float,)] = IFunctionISingleAssetStrategystrstrstrfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionfloat,IFunctionIObservableIOrderIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]


IFunction[IFunctionIObservableIOrderIFunctionSide,(IFunctionfloat,IFunctionIObservableIOrderIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSide


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class IFunctionIObservableSideIObservableboolIObservableSideIObservableSide(object):
    _types = [meta.function((IObservablebool,IObservableSide,IObservableSide,),IObservableSide)]


IFunction[IObservableSide,(IObservablebool,IObservableSide,IObservableSide,)] = IFunctionIObservableSideIObservableboolIObservableSideIObservableSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionfloatIObservablefloatfloatfloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,float,float,),IFunctionfloat)]


IFunction[IFunctionfloat,(IObservablefloat,float,float,float,float,)] = IFunctionIFunctionfloatIObservablefloatfloatfloatfloatfloat


class IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIObservableIOrderIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IFunctionfloat,IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,float,float,),IDifferentiable)]


IFunction[IDifferentiable,(IObservablefloat,float,float,float,float,)] = IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat


from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IObservablefloat,),IObservablefloat)]


IFunction[IObservablefloat,(IObservablebool,IObservablefloat,IObservablefloat,)] = IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
class IFunctionIObservablefloatfloatIObservablefloatfloatISingleAssetTrader(object):
    _types = [meta.function((float,IObservablefloat,float,ISingleAssetTrader,),IObservablefloat)]


IFunction[IObservablefloat,(float,IObservablefloat,float,ISingleAssetTrader,)] = IFunctionIObservablefloatfloatIObservablefloatfloatISingleAssetTrader


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,)] = IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloat


from marketsim import listOf
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._igraph import IGraph
class IFunctionITimeSerieIFunctionIVolumeLevelsIGraphintintlistOffloatint(object):
    _types = [meta.function((IFunctionIVolumeLevels,IGraph,int,int,listOf(float),int,),ITimeSerie)]


IFunction[ITimeSerie,(IFunctionIVolumeLevels,IGraph,int,int,listOf(float),int,)] = IFunctionITimeSerieIFunctionIVolumeLevelsIGraphintintlistOffloatint


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIObservableIOrderIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionfloatIObservablefloatIFunctionIObservableIOrderIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionIObservableIOrderIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IObservablefloat,IFunctionIObservableIOrderIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIObservablefloatIFunctionIObservableIOrderIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iorderbook import IOrderBook
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIOrderBookfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IOrderBook,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IOrderBook,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIOrderBookfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloatfloat(object):
    _types = [meta.function((IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IFunctionIObservableIOrderIFunctionfloat,float,IObservablefloat,float,)] = IFunctionISingleAssetStrategyIFunctionIObservableIOrderIFunctionfloatfloatIObservablefloatfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat


from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
from marketsim.gen._out._itrader import ITrader
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim import listOf
class IFunctionITraderlistOfISingleAssetTraderIMultiAssetStrategystrfloatlistOfITimeSerie(object):
    _types = [meta.function((listOf(ISingleAssetTrader),IMultiAssetStrategy,str,float,listOf(ITimeSerie),),ITrader)]


IFunction[ITrader,(listOf(ISingleAssetTrader),IMultiAssetStrategy,str,float,listOf(ITimeSerie),)] = IFunctionITraderlistOfISingleAssetTraderIMultiAssetStrategystrfloatlistOfITimeSerie


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,float,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSide,float,float,float,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSidefloatfloatfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionSideIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSide)]


IFunction[IFunctionIObservableIOrderIFunctionSide,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIObservableIOrderIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionfloat,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim import listOf
class IFunctionISingleAssetTraderIOrderBookISingleAssetStrategystrfloatfloatlistOfITimeSerie(object):
    _types = [meta.function((IOrderBook,ISingleAssetStrategy,str,float,float,listOf(ITimeSerie),),ISingleAssetTrader)]


IFunction[ISingleAssetTrader,(IOrderBook,ISingleAssetStrategy,str,float,float,listOf(ITimeSerie),)] = IFunctionISingleAssetTraderIOrderBookISingleAssetStrategystrfloatfloatlistOfITimeSerie


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloatIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,float,IFunctionfloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,float,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,)] = IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat


class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IFunctionfloat,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloatIFunctionIObservableIOrderIFunctionSideIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((ISingleAssetStrategy,IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(ISingleAssetStrategy,IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,)] = IFunctionISingleAssetStrategyISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSide


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSidefloatIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,float,IFunctionfloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,float,IFunctionfloat,)] = IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSidefloatIFunctionfloat


from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSide(object):
    _types = [meta.function((float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(float,IFunctionfloat,IEvent,IFunctionIObservableIOrderIFunctionSideIFunctionfloat,IFunctionSide,)] = IFunctionISingleAssetStrategyfloatIFunctionfloatIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionSide


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]


IFunction[IFunctionIObservableIOrderIFunctionSideIFunctionfloat,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IFunctionfloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIFunctionfloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._iobservable import IObservablefloat
class IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,),IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat)]


IFunction[IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,(IObservablefloat,IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat,)] = IFunctionIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloatIObservablefloatIFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionSideIFunctionfloat


from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccountIFunctionIFunctionfloatIFunctionfloatIFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,IFunctionIFunctionfloatIFunctionfloat,IFunctionIFunctionlistOffloatlistOffloat,),ISingleAssetStrategy)]


IFunction[ISingleAssetStrategy,(listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,IFunctionIFunctionfloatIFunctionfloat,IFunctionIFunctionlistOffloatlistOffloat,)] = IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccountIFunctionIFunctionfloatIFunctionfloatIFunctionIFunctionlistOffloatlistOffloat


IFunction[int]._types.append(IFunction[float])
IFunction[int]._types.append(IFunction[object])
IFunction[float]._types.append(IFunction[object])
