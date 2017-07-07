from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_sat0
    purpose: test saturation of summing junction prior to DAC output
    test: sawg0 is reference tone; clamp amplitude of sawg1
    setup: scope trigger on ttl_sma; 20ns/div, 100mV/div
    expectation:
        a0=1 is 300 mV amplitude
        symmetric clipping of sawg1 at +a0/2 and -a0/2
        see discussion for impact of output balun at low frequencies
        https://github.com/m-labs/artiq/issues/762
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
        f0 = 5*MHz
        t0 = 1*us
        a0 = 1.0
        asat = 0.5

        while True:
            self.sawg0.amplitude1.set(a0)
            self.sawg0.frequency1.set(f0)
            self.sawg1.amplitude1.set(a0)
            self.sawg1.frequency1.set(f0)
            self.sawg1.config.set_out_max(asat)
            delay(1*us)
            self.sawg1.config.set_out_min(-1*asat)

            self.ttl_sma.pulse(1*us)
            delay(1 * ms)
