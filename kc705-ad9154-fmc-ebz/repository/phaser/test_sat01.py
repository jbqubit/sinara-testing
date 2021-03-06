from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_sat01
    purpose: test saturation of summing junction involving offset (just before DAC output)
    test: sawg0 is reference tone; clamp amplitude of sawg1
    setup: scope run control single, manual trigger; 500ns/div, 100mV/div
    expectation:
        a0=1 is 120 mV amplitude
        if max=0.5 then sawg1 should not exceed 60 mV
        if min=-0.5 then sawg1 should not exceed -60 mV
    observation:
        maximum is violated
        minimum is not sharply clamped at -0.5
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
        aclip = 0.1

        while True:
            # starting condition
            self.sawg0.amplitude1.set(2*a0)
            self.sawg0.frequency1.set(f0)
            self.sawg1.amplitude1.set(a0)
            self.sawg1.frequency1.set(f0)
            self.sawg1.offset.set(a0)


            # set clipping amplitude
            self.sawg1.config.set_out_max(aclip)
            delay(1*us)
            self.sawg1.config.set_out_min(-aclip)

            self.ttl_sma.pulse(1 * us)
            delay(10 * us)

            #end
            delay(1*ms)