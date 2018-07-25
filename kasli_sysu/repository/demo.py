from artiq.experiment import *


class UrukulTest(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("urukul0_cpld")
        self.urukul0s = [self.get_device("urukul0_ch"+str(i)) for i in range(4)]
        self.ttl = self.get_device("ttl0")

    @kernel
    def run(self):
        f = 3.0*MHz
        dt = 2*us

        # self.core.reset()
        # delay(10*ms)
        # self.ttl.output()
        # delay(10*ms)

        # for j in range(4):
        #     self.urukul0s[j].init()

        # delay(10*ms)

        # while True:
        #     delay(10*ms)
        #     with parallel:
        #         self.urukul0s[0].set(f, 0., 1.)
        #         self.urukul0s[1].set(f, 0., 1.)
        #         self.ttl.pulse(dt)
        #         self.urukul0s[0].sw.pulse(dt)
        #         self.urukul0s[1].sw.pulse(dt)

        #         # for j in range(4):
        #         #     self.urukul0s[j].sw.pulse(2*us)
        #     delay(10*ms)
                    