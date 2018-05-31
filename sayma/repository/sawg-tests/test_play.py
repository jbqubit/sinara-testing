from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_simple_sin1
    purpose: test sinusoidal output
    expectation:
      - 10 MHz from sawg.frequency1 on sawg0 and sawg1
      - playback continues after program termination
    setup: scope single run, force trigger manually, 500ns/div, 100mV/div
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
        delay(300 * us)

        f0 = 10*MHz
        a0 = 0.1

        self.sawg0.frequency1.set(f0)
        self.sawg0.amplitude1.set(a0)
        self.sawg1.frequency1.set(f0)
        self.sawg1.amplitude1.set(a0)

        for i in range(10000):
            self.ttl_sma.pulse(1*ms)
            delay(1*ms)