from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_ap3
    sawg0 is a reference channel
    sawg1 has its phase swept in a loop
    """
    def build(self):
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
        delay(300 * us)

        for ph in range(0, 300):
            for i in range(0, 100):
                self.test(ph/100.0)
                self.ttl_sma.pulse(3 * us)
                delay(1 * ms)

    @kernel
    def test(self, ph):
        # test: t1
        f0 = 10*MHz
        t = 500*ns
        a0 = 0.80

        # prepare
        self.sawg0.frequency1.set(f0)
        self.sawg0.amplitude1.set(a0)
        self.sawg1.frequency1.set(f0)
        self.sawg1.amplitude1.set(a0)

        delay(t)
        self.sawg1.phase1.set(ph)
        delay(t)

        # switch RF off
        self.sawg0.amplitude1.set(0.)
        self.sawg1.amplitude1.set(0.)
