from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """
    purpose:
    test:
    setup:
    expectation:
    observation:
    """
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("led")
        self.setattr_device("ttl_sma")

        self.setattr_device("sawg0")
        self.setattr_device("sawg1")

    @kernel
    def run(self):
        self.core.reset()
        delay(300*us)
        self.sawg0.reset()
        self.sawg1.reset()
        delay(10*ms)

        while(True):
            self.test()
            delay(1*ms)

    @kernel
    def test(self):
        f0 = 2*MHz
        t0 = 1*us
        a0 = a1 = a2 = 0.5
        t_down = 1*us
        order = 3

        self.ttl_sma.pulse(3*us)

        self.sawg0.amplitude1.set(0.)
        delay(1*us)
        self.sawg0.amplitude1.smooth(0., 1., 1*us, 0)
        #self.sawg0.amplitude1.smooth(0.5, 0., t_down, order)
        delay(1*us)
        self.sawg0.amplitude1.set(0.)



