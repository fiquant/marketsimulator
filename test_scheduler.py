from marketsim.scheduler import Scheduler

S = Scheduler()

def F(actionTime):
   def inner():
      assert actionTime==S.currentTime
      print actionTime
   return inner

def schedule(actionTime):
   return S.schedule(actionTime, F(actionTime))

schedule(1.)
schedule(1.)
schedule(3.)
e2 = schedule(2.)

S.workTill(1.5)
e2()
S.workTill(2.5)
S.workTill(3.5)

