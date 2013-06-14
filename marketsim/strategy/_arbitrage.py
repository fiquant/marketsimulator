from marketsim import order, Side, scheduler, types
from blist import sorteddict

from _basic import Strategy
from _wrap import wrapper2

# NB! obsolete for the moment

class _Arbitrage_Impl(Strategy):

    def __init__(self):
        """ Initializes trader by order books for the asset from different markets
        """
        Strategy.__init__(self)
        
        # order queues ordered by their best asks and bids
        # something like std::map<Ticks, OrderQueue>[2]
        self._bests = [sorteddict(), sorteddict()]
        self._oldBests = {}
        
    def bind(self, context):
        self._books = self._trader.orderBooks
        
        def onBestChanged(side):
            """ Returns a function to be called when best order in a queue changed
            """
            
            # ordered set of queues on my side
            myQueues = self._bests[side.id]
            oppositeSide = side.opposite
            # ordered set of queues on the opposite side
            oppositeQueues = self._bests[oppositeSide.id]
            
            def inner(myQueue):
                """Called when in some queue a new best order appeared"""
                
                if self._suspended:
                    return
                
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
                            
                            self._scheduler.scheduleAfter(0, lambda: \
                                self._trader.send(myQueue.book, 
                                          order.LimitMarket(oppositeSide, myPrice, volumeToTrade)))
                            
                            self._scheduler.scheduleAfter(0, lambda: \
                                self._trader.send(oppositeQueue.book,
                                          order.LimitMarket(side, oppositePrice, volumeToTrade)))
    
            return lambda queue: self._scheduler.scheduleAfter(0, lambda: inner(queue))
                        
        def regSide(side):
            for book in self._books:
                queue = book.queue(side) 
                queue.on_best_changed += onBestChanged(side)
                if not queue.empty:
                    self._bests[side.id][queue.best.signedPrice] = queue
                    self._oldBests[queue] = queue.best.signedPrice
                    
        regSide(Side.Buy)
        regSide(Side.Sell)

exec wrapper2("Arbitrage", "", [], register=False)