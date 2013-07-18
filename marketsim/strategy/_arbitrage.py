from marketsim import order, Side, scheduler, types, event, _
from blist import sorteddict

from _basic import MultiAssetStrategy
from _wrap import wrapper2

# NB! obsolete for the moment

class _Arbitrage_Impl(MultiAssetStrategy):

    def __init__(self):
        """ Initializes trader by order books for the asset from different markets
        """
        MultiAssetStrategy.__init__(self)
        
        # order queues ordered by their best asks and bids
        # something like std::map<Ticks, OrderQueue>[2]
        self._bests = [sorteddict(), sorteddict()]
        self._oldBests = {}
        self._pending = set()
        
    def _onCancelled(self, order):
        self._pending.remove(order)
        #print len(self._pending)
        
    def inner(self, myQueue, side):
        """Called when in some queue a new best order appeared"""
        
        if self._suspended:
            return
        
        # ordered set of queues on my side
        myQueues = self._bests[side.id]
        oppositeSide = side.opposite
        # ordered set of queues on the opposite side
        oppositeQueues = self._bests[oppositeSide.id]

        bestOrder = myQueue.best if not myQueue.empty else None
        
        # since the price of the best order changed,
        # we remove its queue from the set of all queues
        if myQueue in self._oldBests:
            try:
                p = self._oldBests[myQueue]
                myQueues.pop(p)
            except Exception:    
                pass # very strange things...
        
        # if the queue becomes empty 
        if bestOrder == None:
            # just remove it from the set of all queues
            if myQueue in self._oldBests:
                self._oldBests.pop(myQueue)
        else:
            # otherwise, update correspondance queue -> signedPrice -> queue
            self._oldBests[myQueue] = bestOrder.signedPrice
            myQueues[bestOrder.signedPrice] = myQueue
        
            # if there are opposite queues    
            if len(oppositeQueues) > 0:
                # take the best price of the best one
                bestOppositeSignedPrice = oppositeQueues.viewkeys()[0]
                # and the queue itself
                oppositeQueue = oppositeQueues[bestOppositeSignedPrice] 

                if oppositeQueue.empty or oppositeQueue.best.price != abs(bestOppositeSignedPrice):
                    # it means that we haven't yet received event that another queue has changed 
                    return 
                
                oppositePrice = abs(bestOppositeSignedPrice)
                myPrice = bestOrder.price
                
                # is there some sense to trade                    
                if not side.better(oppositePrice, myPrice):
                    
                    volumeToTrade = min(bestOrder.volume, oppositeQueue.best.volume)

                    # make two complimentary trades
                    # for these trades we create limit orders 
                    # since price may change before orders will be processed
                    # but cancel them immediately in order to avoid storing these limit orders in the book
                    # this logic is implemented by LimitMarketOrder
                    
                    def send(o):
                        self._pending.add(o)
                        
                        o.on_cancelled += _(self)._onCancelled
                             
                        self._send(myQueue.book, o)
                        
                    send(order.LimitMarket(oppositeSide, 
                                           myPrice, 
                                           volumeToTrade))                               
                    
                    
                    send(order.LimitMarket(side, 
                                           oppositePrice, 
                                           volumeToTrade))                                    
                    
    def _send(self, orderbook, order):
        for t in self._traders:
            if t.orderBook == orderbook:
                t.send(order)
                    
    def _schedule(self, side, queue):
        self.inner(queue, side)
    
    def bind(self, context):
        self._traders = [t for t in self._trader.traders]
        self._books = [t.orderBook for t in self._trader.traders]        
                        
        def regSide(side):
            for book in self._books:
                queue = book.queue(side) 
                event.subscribe(queue.bestPrice, 
                                _(self, side)._schedule, 
                                self, {})
                if not queue.empty:
                    self._bests[side.id][queue.best.signedPrice] = queue
                    self._oldBests[queue] = queue.best.signedPrice
                    
        regSide(Side.Buy)
        regSide(Side.Sell)

exec wrapper2("Arbitrage", "", [], register=False)