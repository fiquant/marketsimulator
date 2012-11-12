
def TwoSides(trader, orderFactoryT, eventGen, orderFunc):                
        """ Runs generic two side strategy 
        trader - single asset single market trader
        orderFactoryT - function to create orders: side -> *orderParams -> Order
        eventGen - event generator to be listened - we'll use its advise method to subscribe to
        orderFunc - function to calculate order parameters: Trader -> None | (side,*orderParams) 
        """        

        def wakeUp(signal):
            # determine side and parameters of an order to create
            res = orderFunc(trader)
            if res <> None:
                (side, params) = res
                # create order given side and parameters
                order = orderFactoryT(side)(*params)
                # send order to the order book
                trader.send(order)

        # start listening calls from eventGen
        eventGen.advise(wakeUp)
        return trader
