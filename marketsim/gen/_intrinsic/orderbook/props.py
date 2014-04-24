from marketsim.gen._out._intrinsic_base.orderbook.props import BestPrice_Base, TickSize_Base

class BestPrice_Impl(BestPrice_Base):

    def bind(self, ctx):
        from marketsim import event, _, context
        if not hasattr(self, '_subscriptions'):
            event.subscribe(self.queue.bestPrice, _(self).fire, self)
            context.bind(self._subscriptions, ctx)

    def bind_impl(self, ctx):
        from marketsim import event, _, context
        if not hasattr(self, '_subscriptions'):
            event.subscribe(self.queue.bestPrice, _(self).fire, self)

    @property
    def __call__(self):
        return self.queue.bestPrice


class TickSize_Impl(TickSize_Base):

    def __call__(self):
        return self.book.tickSize
