from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """
    purpose: test saturation of summing junction prior to DUC
    test: sawg0 is reference tone
    setup: scope run control single, manual trigger; 500ns/div, 100mV/div
    expectation:
        with a0=1 sawg1 amplitude is 300 mV
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
        f0 = 20*MHz
        t0 = 1*us
        a0 = 0.5
        aclip = 0.5

        while True:
            # starting condition
            self.sawg0.amplitude1.set(2 * a0)
            self.sawg0.frequency1.set(f0)
            self.sawg1.amplitude1.set(a0)
            self.sawg1.frequency1.set(f0)
            self.sawg1.amplitude2.set(a0)
            self.sawg1.frequency2.set(f0)

            self.sawg1.config.set_duc_max(aclip)
            delay(1*us)
            self.sawg1.config.set_duc_min(-aclip)

            self.ttl_sma.pulse(1*us)

            # end
            delay(1*ms)