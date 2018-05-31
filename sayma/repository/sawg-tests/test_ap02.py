from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_ap02
    purpose: test absolute alignment of sawg0.frequency2 sawg1.frequency2
    test: make sawg0 and sawg1 phase aligned
    expectation: no phase offset between sawg0 and sawg1
    setup: scope single run, manually trigger acquisition; 10ns/div, 100mV/div
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
        delay(300 * us)
        self.sawg0.reset()
        self.sawg1.reset()
        self.ttl_sma.output()
        delay(1 * ms)

        f0 = 50*MHz
        a0 = 0.5

        self.sawg0.amplitude2.set(a0)
        self.sawg0.frequency2.set(f0)
        self.sawg0.phase2.set(0.)
        self.sawg1.amplitude2.set(a0)
        self.sawg1.frequency2.set(f0)
        self.sawg1.phase2.set(0.)

