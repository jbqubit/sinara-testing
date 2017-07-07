from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_offset
    purpose: check sign of sawg1.offset
    expectation: see inline comments below
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
            # expect: positive polarity pulse
            # observe: positive polarity pulse
            self.sawg1.offset.set(0.99)
            delay(100*ns)
            self.sawg1.offset.set(0.0)
            delay(1*us)
            # expect: positive polarity pulse
            # observe: positive polarity pulse
            self.sawg1.offset.set(1.0)
            delay(100*ns)
            self.sawg1.offset.set(0.0)
            delay(1*us)
            # expect: negative polarity pulse
            # observe: negative polarity pulse
            self.sawg1.offset.set(-1.0)
            delay(100*ns)
            self.sawg1.offset.set(0.0)
            delay(1*us)

            delay(1 * ms)
