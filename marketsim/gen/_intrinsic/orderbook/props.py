class BestPrice_Impl(object):

    def bind(self, ctx):
        from marketsim import event, _, context
        event.subscribe(self.queue.bestPrice, _(self).fire, self)
        context.bind(self._subscriptions, ctx)

    @property
    def __call__(self):
        return self.queue.bestPrice


class TickSize_Impl(object):

    def __call__(self):
        return self.book.tickSize
