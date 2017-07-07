from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_rtio_conflict
    purpose: test trapping of RTIO errors
    test:
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

        # following causes no error
        # expectation: RTIO collision error
        with parallel:
            self.sawg0.amplitude1.set(0.5)
            self.sawg0.amplitude1.set(0.1)

        # following causes no error
        # expectation: RTIO collision error
        with parallel:
            self.sawg0.frequency1.set(10*MHz)
            self.sawg0.frequency1.set(20*MHz)

        # following causes RTIO collision error
        # expectation: no RTIO collision error
        with parallel:
            self.sawg1.config.set_duc_max(0.5)
            self.sawg1.config.set_duc_min(-0.5)

        # following causes no error
        # expectation: RTIO sequence error
        with parallel:
            self.sawg0.amplitude1.smooth(0.5, .0, 1*us, 3)
            self.sawg0.amplitude1.smooth(0.2, .0, 4*us, 3)

        # following causes no error
        # expectation: RTIO collision error
        with parallel:
            self.ttl_sma.output()
            self.ttl_sma.input()

        # following generates RTIO sequence error
        # expectation: RTIO sequence error
        with parallel:
            self.ttl_sma.pulse(0.5*us)
            self.ttl_sma.pulse(1.0*us)
        delay(1*ms)

