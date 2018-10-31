from artiq.experiment import *


class Urukul9910Init(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("urukul0_cpld")
        self.urukul0 = [self.get_device("urukul0_ch"+str(n)) for n in range(4)]

    @kernel
    def run(self):
        self.core.break_realtime()
        self.core.reset()

        self.core.break_realtime()
        self.urukul0_cpld.init()

        for n in range(4):
            delay(10*ms)
            self.urukul0[n].init()