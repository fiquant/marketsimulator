from marketsim import _, types, order, Side

from _basic import Strategy
from _wrap import wrapper2

class _SingleOrder_Impl(Strategy):

    def bind(self, ctx):
        self._scheduler.async(_(self)._wakeUp)

    def _wakeUp(self):
        self.send(self.order)
        
exec wrapper2("SingleOrder", 
              """
              """, 
              [
                ('order', 'order.Limit(Side.Buy, 100, 1)', 'types.IOrder')
              ], register = False)

class _SingleOrder2_Impl(Strategy):

    def bind(self, ctx):
        self._scheduler.async(_(self)._wakeUp)

    def _wakeUp(self):
        self._trader.send(self.factory())
        
exec wrapper2("SingleOrder2", 
              """
              """, 
              [
                ('factory', 'None', 'types.IOrderGenerator')
              ], register = False)
