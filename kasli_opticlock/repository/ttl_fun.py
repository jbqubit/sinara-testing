from artiq.experiment import *


class TTLFun(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl4")
        self.setattr_device("ttl5")
        self.setattr_device("ttl9")

    @kernel
    def run(self):
        self.core.reset()
        while True:
            self.ttl4.pulse(1*ms)
            delay(1*ms)
            self.ttl5.pulse(1*ms)
            delay(1*ms)
            self.ttl9.pulse(1*ms)
            delay(100*ms)