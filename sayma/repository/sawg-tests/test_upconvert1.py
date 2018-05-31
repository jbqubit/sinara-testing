from artiq.experiment import *

class SAWGTest(EnvExperiment):
    """test_upconvert1
    purpose: test single-tone up conversion for sawg3
    test: mix LO = 150 MHz, IF = 25 MHz
    expectation:
        RF: LO+IF at approximately -13 dBm is the desired feature
        RF: LO-IF at approximately -13 dBm
    setup: spectrum analyzer with range set to 100 kHz to 500 MHz
    """
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("sawg3")
        f0 = 150*MHz
        f12 = 50*MHz


    @kernel
    def run(self):
        self.core.reset()
        delay(300*us)
        self.sawg3.reset()

        self.sawg3.frequency0.set(150*MHz)
        self.sawg3.amplitude1.set(0.5)
        self.sawg3.frequency1.set(25*MHz)