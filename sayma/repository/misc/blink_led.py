from artiq.experiment import *


class BlinkSaymaLED(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("led0")
        self.setattr_device("led123")
        self.setattr_device("ttl_sma0")
        self.setattr_device("ttl_sma1")

    @kernel
    def run(self):
        self.core.reset()
        self.ttl_sma0.output()
        self.ttl_sma1.output()
        while True:
            for _ in range(3):
                self.led0.pulse(100*ms)
                self.led123.pulse(100*ms)
                self.ttl_sma0.pulse(100*ms)
                self.ttl_sma1.pulse(100*ms)
                delay(100*ms)
            delay(500*ms)
