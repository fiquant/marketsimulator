from marketsim import order, Side, scheduler, types
from blist import sorteddict

from _basic import Strategy
from _wrap import wrapper

class _Arbitrage_Impl(Strategy):

    def __init__(self, trader, params):
        """ Initializes trader by order books for the asset from different markets
        """
        Strategy.__init__(self, trader)
        
        sched = scheduler.current() if params.sched is None else params.sched 
        
        books = trader.orderBooks
        
        # order queues ordered by their best asks and bids
        # something like std::map<Ticks, OrderQueue>[2]
        bests = [sorteddict(), sorteddict()]
        oldBests = {}
        
        def onBestChanged(side):
            """ Returns a function to be called when best order in a queue changed
            """
            
            # ordered set of queues on my side
            myQueues = bests[side.id]
            oppositeSide = side.opposite
            # ordered set of queues on the opposite side
            oppositeQueues = bests[oppositeSide.id]
            
            def inner(myQueue):
                """Called when in some queue a new best order appeared"""
                
                if self._suspended:
                    return
                
                bestOrder = myQueue.best if not myQueue.empty else None
                
                # since the price of the best order changed,
                # we remove its queue from the set of all queues
                if myQueue in oldBests:
                    try:
                        p = oldBests[myQueue]
                        myQueues.pop(p)
                    except Exception:    
                        pass # very strange things...
                
                # if the queue becomes empty 
                if bestOrder == None:
                    # just remove it from the set of all queues
                    if myQueue in oldBests:
                        oldBests.pop(myQueue)
                else:
                    # otherwise, update correspondance queue -> signedPrice -> queue
                    oldBests[myQueue] = bestOrder.signedPrice
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
                            
                            sched.scheduleAfter(0, lambda: \
                                trader.send(myQueue.book, 
                                          order.LimitMarket(oppositeSide, myPrice, volumeToTrade)))
                            
                            sched.scheduleAfter(0, lambda: \
                                trader.send(oppositeQueue.book,
                                          order.LimitMarket(side, oppositePrice, volumeToTrade)))
    
            return lambda queue: sched.scheduleAfter(0, lambda: inner(queue))
                        
        def regSide(side):
            for book in books:
                queue = book.queue(side) 
                queue.on_best_changed += onBestChanged(side)
                if not queue.empty:
                    bests[side.id][queue.best.signedPrice] = queue
                    oldBests[queue] = queue.best.signedPrice
                    
        regSide(Side.Buy)
        regSide(Side.Sell)

exec wrapper("Arbitrage", [('sched', 'None', 'None')], register=False)