from marketsim.gen._out._intrinsic_base.observable.derivative import Derivative_Base

class Derivative_Impl(Derivative_Base):

    def __call__(self):
        return self.x.derivative()
