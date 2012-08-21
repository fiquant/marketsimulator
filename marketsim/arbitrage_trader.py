from marketsim.trader import TraderBase
from marketsim.order import MarketOrderT
from blist import sorteddict
from marketsim import Side
from marketsim.scheduler import world


class ArbitrageTrader(TraderBase):
    
    def __init__(self, *books):
        
        TraderBase.__init__(self)
        
        bests = [sorteddict(), sorteddict()]
        oldBests = {}
        
        def onBestChanged(side):
            
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
                    myQueues.pop(oldBests[myQueue])
                
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
    
                        # calculate volume of ordere from opposite side that can be matched
                        oppositeVolume = oppositeQueue.volumeWithPriceBetterThan(bestOrder.price)

                        # is there some sense to trade                    
                        if oppositeVolume > 0:
                            
                            volumeToTrade = min(oppositeVolume, bestOrder.volume)
                            
                            myOrder = self.makeSubscribedTo(MarketOrderT(oppositeSide)(volumeToTrade))
                            otherOrder = self.makeSubscribedTo(MarketOrderT(side)(volumeToTrade))
                            
                            # make two complimentary trades
                            myQueue.book.process(myOrder)
                            oppositeQueue.book.process(otherOrder)
                    
            return lambda queue: world.scheduleAfter(0, lambda: inner(queue))
                        
                
        
        def onBidsChanged(queue, bestOrder):
            pass
        
        def regSide(side):
            for book in books:
                queue = book.queue(side) 
                queue.on_best_changed += onBestChanged(side)
                if not queue.empty:
                    bests[side][queue.best.signedPrice] = queue
                    oldBests[queue] = queue.best.signedPrice
                    
        regSide(Side.Buy)
        regSide(Side.Sell)
            
        
