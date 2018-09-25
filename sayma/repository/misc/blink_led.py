from artiq.experiment import *


class BlinkSaymaLED(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("led0")
        self.setattr_device("led1")

        self.setattr_device("ttl_sma_out")


    @kernel
    def run(self):
        self.core.reset()
        self.ttl_sma_out.output()

        for i in range(20): 
            div = 10.0
            self.ttl_sma_out.pulse(1*us)
            delay(1000/div*ms)
            self.led0.pulse(1000/div*ms)
            delay(500/div*ms)
            self.led0.pulse(500/div*ms)
            delay(250/div*ms)
            self.led0.pulse(250/div*ms)
            delay(125/div*ms)
            self.led0.pulse(125/div*ms)
            print(i)