from artiq.experiment import *


class ttlAll(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl0")
        self.setattr_device("ttl1")
        self.setattr_device("ttl2")
        self.setattr_device("ttl3")
        self.setattr_device("ttl4")
        self.setattr_device("ttl5")
        self.setattr_device("ttl6")
        self.setattr_device("ttl7")
        self.setattr_device("ttl8")
        self.setattr_device("led0")

    @kernel
    def run(self):
        self.core.reset()
        self.ttl0.output()
        self.ttl1.output()
        self.ttl2.output()
        self.ttl3.output()
        self.ttl4.output()
        self.ttl5.output()
        self.ttl6.output()
        self.ttl7.output()
        self.ttl8.output()


        while True:
            self.led0.pulse(100*ms)

            self.ttl0.pulse(1*us)
            self.ttl1.pulse(1*us)
            self.ttl2.pulse(1*us)
            self.ttl3.pulse(1*us)
            self.ttl4.pulse(1*us)
            self.ttl5.pulse(1*us)
            self.ttl6.pulse(1*us)
            self.ttl7.pulse(1*us)
            self.ttl8.pulse(1*us)