from marketsim.types import Function_impl
from marketsim import meta
class IFunctionfloat(Function_impl):
    _types = [meta.function((),float)]
    @property
    def Negate(self):
        from marketsim.gen._out.ops._negate import Negate
        return Negate(self)
    
    def OnEveryDt(self, dt = None):
        from marketsim.gen._out.observable._oneverydt import OnEveryDt
        return OnEveryDt(self,dt)
    
    def Min(self, y = None):
        from marketsim.gen._out.math._min import Min
        return Min(self,y)
    
    @property
    def side_FixedBudget(self):
        from marketsim.gen._out.order._curried._side_fixedbudget import side_FixedBudget
        return side_FixedBudget(self)
    
    @property
    def sideprice_Limit(self):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit
        return sideprice_Limit(self)
    
    def Signal(self, threshold = None):
        from marketsim.gen._out.strategy.side._signal import Signal
        return Signal(self,threshold)
    
    @property
    def signedVolume_LimitSigned(self):
        from marketsim.gen._out.order._curried._signedvolume_limitsigned import signedVolume_LimitSigned
        return signedVolume_LimitSigned(self)
    
    def Add(self, y = None):
        from marketsim.gen._out.ops._add import Add
        return Add(self,y)
    
    @property
    def Atan(self):
        from marketsim.gen._out.math._atan import Atan
        return Atan(self)
    
    def Less(self, y = None):
        from marketsim.gen._out.ops._less import Less
        return Less(self,y)
    
    def FundamentalValue(self, book = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
        return FundamentalValue(self,book)
    
    @property
    def MarketSigned(self):
        from marketsim.gen._out.order._marketsigned import MarketSigned
        return MarketSigned(self)
    
    def Mul(self, y = None):
        from marketsim.gen._out.ops._mul import Mul
        return Mul(self,y)
    
    def NotEqual(self, y = None):
        from marketsim.gen._out.ops._notequal import NotEqual
        return NotEqual(self,y)
    
    def Max(self, y = None):
        from marketsim.gen._out.math._max import Max
        return Max(self,y)
    
    @property
    def Sqr(self):
        from marketsim.gen._out.math._sqr import Sqr
        return Sqr(self)
    
    @property
    def Sqrt(self):
        from marketsim.gen._out.math._sqrt import Sqrt
        return Sqrt(self)
    
    def GreaterEqual(self, y = None):
        from marketsim.gen._out.ops._greaterequal import GreaterEqual
        return GreaterEqual(self,y)
    
    def side_Limit(self, volume = None):
        from marketsim.gen._out.order._curried._side_limit import side_Limit
        return side_Limit(self,volume)
    
    @property
    def Exp(self):
        from marketsim.gen._out.math._exp import Exp
        return Exp(self)
    
    @property
    def Log(self):
        from marketsim.gen._out.math._log import Log
        return Log(self)
    
    def getOrElse(self, elsePart = None):
        from marketsim.gen._out._ifdefined import IfDefined
        return IfDefined(self,elsePart)
    
    @property
    def side_price_Limit(self):
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit
        return side_price_Limit(self)
    
    @property
    def side_Market(self):
        from marketsim.gen._out.order._curried._side_market import side_Market
        return side_Market(self)
    
    @property
    def Clamp0(self):
        from marketsim.gen._out.strategy.weight._clamp0 import Clamp0
        return Clamp0(self)
    
    @property
    def Canceller(self):
        from marketsim.gen._out.strategy._canceller import Canceller
        return Canceller(self)
    
    def Sub(self, y = None):
        from marketsim.gen._out.ops._sub import Sub
        return Sub(self,y)
    
    def AtanPow(self, base = None):
        from marketsim.gen._out.strategy.weight._atanpow import AtanPow
        return AtanPow(self,base)
    
    def Pow(self, power = None):
        from marketsim.gen._out.math._pow import Pow
        return Pow(self,power)
    
    def LimitSigned(self, price = None):
        from marketsim.gen._out.order._limitsigned import LimitSigned
        return LimitSigned(self,price)
    
    @property
    def sidevolume_Limit(self):
        from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit
        return sidevolume_Limit(self)
    
    @property
    def Noise(self):
        from marketsim.gen._out.strategy.side._noise import Noise
        return Noise(self)
    
    @property
    def IdentityF(self):
        from marketsim.gen._out.strategy.weight._identityf import IdentityF
        return IdentityF(self)
    
    def Div(self, y = None):
        from marketsim.gen._out.ops._div import Div
        return Div(self,y)
    
    def LessEqual(self, y = None):
        from marketsim.gen._out.ops._lessequal import LessEqual
        return LessEqual(self,y)
    
    def Equal(self, y = None):
        from marketsim.gen._out.ops._equal import Equal
        return Equal(self,y)
    
    def Greater(self, y = None):
        from marketsim.gen._out.ops._greater import Greater
        return Greater(self,y)
    
    pass



