from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """
    purpose: measure response of AD9154-FMC-EBZ to step stimulus
    test: step sawg1.offset
    setup: scope trigger on ttl_sma; 200ns/div, 100mV/div
    expectation:
        balun high-pass dominates
        317 mV peak decays to 1/e in 140 ns
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
        self.ttl_sma.output()
        delay(10 * ms)
        self.test()

    @kernel
    def test(self):
        while True:
            self.ttl_sma.pulse(1 * us)
            self.sawg1.offset.set(0.99)
            delay(1*us)
            self.sawg1.offset.set(0.0)

            delay(1 * ms)
