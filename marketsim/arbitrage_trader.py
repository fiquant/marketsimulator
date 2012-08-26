from marketsim.trader import SingleAssetTrader
from marketsim.order import MarketOrderT
from blist import sorteddict
from marketsim import Side
from marketsim.scheduler import world


class ArbitrageTrader(SingleAssetTrader):
    """ A trader that make use of arbitrage trading the same asset on several markets
    """
    
    def __init__(self, *books):
        """ Initializes trader by order books for the asset from different markets
        """
        
        SingleAssetTrader.__init__(self)
        
        # order queues ordered by their best asks and bids
        # something like std::map<Ticks, OrderQueue>[2]
        bests = [sorteddict(), sorteddict()]
        oldBests = {}
        
        def onBestChanged(side):
            """ Returns a function to be called when best order in a queue changed
            """
            
            # ordered set of queues on my side
            myQueues = bests[side]
            oppositeSide = Side.opposite(side)
            # ordered set of queues on the opposite side
            oppositeQueues = bests[oppositeSide]
            
            def inner(myQueue):
                """Called when in some queue a new best order appeared"""
                
                bestOrder = myQueue.best if not myQueue.empty else None
                
                # since the price of the best order changed,
                # we remove its queue from the set of all queues
                if myQueue in oldBests:
                    try:
                        myQueues.pop(oldBests[myQueue])
                    except Exception, e:
                        pass
                
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
    
                        # calculate volume of orders from opposite side that can be matched
                        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(bestOrder.price)

                        # is there some sense to trade                    
                        if oppositeVolume > 0:
                            
                            volumeToTrade = min(oppositeVolume, bestOrder.volume)
                            
                            # make two complimentary trades
                            self.send(myQueue.book, MarketOrderT(oppositeSide)(volumeToTrade))
                            self.send(oppositeQueue.book, MarketOrderT(side)(volumeToTrade))
                    
            return lambda queue: world.scheduleAfter(0, lambda: inner(queue))
                        
        def regSide(side):
            for book in books:
                queue = book.queue(side) 
                queue.on_best_changed += onBestChanged(side)
                if not queue.empty:
                    bests[side][queue.best.signedPrice] = queue
                    oldBests[queue] = queue.best.signedPrice
                    
        regSide(Side.Buy)
        regSide(Side.Sell)
