from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_spline0
    purpose:
    test:
    expectation:
    setup:
    """
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("sawg0")
        self.setattr_device("sawg1")
        self.setattr_device("ttl_sma")

        name = self.__doc__.splitlines()[0].strip()
        print('name', name)

    @kernel
    def run(self):
        self.core.reset()
        delay(300 * us)
        self.sawg0.reset()
        self.sawg1.reset()
        self.ttl_sma.output()
        delay(5*ms)

        f0 = 10*MHz
        tt = 1000*ns

        while True:
            self.ttl_sma.pulse(1*us)
            delay(-0.5*us)
            self.sawg0.frequency1.set(f0)
            self.sawg0.phase1.set(0.)
            self.sawg1.frequency1.set(f0)
            self.sawg1.phase1.set(0.5)

            # 0th order
            self.sawg0.amplitude1.set_coeff([1., 0., 0., 0.])
            self.sawg1.amplitude1.smooth(0., 1., 1*ns, 0)  # implicit delay(1*ns)
            delay(tt/5)

            # 1st order
            self.sawg0.amplitude1.set_coeff([0., 1/tt, 0., 0.])
            self.sawg1.amplitude1.smooth(0., 1., tt, 1)  # implicit delay(tt)
            self.sawg1.amplitude1.set_coeff([1., 0., 0., 0.])
            self.sawg0.amplitude1.set_coeff([1., 0., 0., 0.])
            delay(tt)
            self.sawg0.amplitude1.set_coeff([1., -1/tt, 0., 0.])
            self.sawg1.amplitude1.smooth(1., 0., tt, 1)  # implicit delay(tt)
            self.sawg1.amplitude1.set_coeff([0., 0., 0., 0.])
            self.sawg0.amplitude1.set_coeff([0., 0., 0., 0.])

            # 2nd order
            self.sawg0.amplitude1.set_coeff([0., 0., 2/(tt*tt), 0.])
            self.sawg0.amplitude1.set_coeff([1., 0., 0., 0.])
            delay(tt)
            self.sawg0.amplitude1.set_coeff([1., 0., -2/(tt*tt), 0.])
            self.sawg0.amplitude1.set_coeff([0., 0., 0., 0.])

            # 3rd order
            self.sawg0.amplitude1.set_coeff([0., 0., 0., 6/(tt*tt*tt)])
            self.sawg1.amplitude1.smooth(0., 1., tt, 3)  # implicit delay(tt)
            self.sawg1.amplitude1.set_coeff([1., 0., 0., 0.])
            self.sawg0.amplitude1.set_coeff([1., 0., 0., 0.])
            delay(tt)
            self.sawg0.amplitude1.set_coeff([1., 0., 0., -6/(tt*tt*tt)])
            self.sawg1.amplitude1.smooth(1., 0., tt, 3)  # implicit delay(tt)
            self.sawg1.amplitude1.set_coeff([0., 0., 0., 0.])
            self.sawg0.amplitude1.set_coeff([0., 0., 0., 0.])

            # wrap up
            delay(5*ms)


