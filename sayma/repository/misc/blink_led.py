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
        #self.ttl_sma1.output()

        for i in range(100):
            # self.led0.pulse(100*ms)
            # self.led1.pulse(100*ms)

            self.ttl_sma_out.pulse(i*us)
            # ttl_sma1 is set as input in gateware/target/sayma_amc
            # no output observed 
            #self.ttl_sma_out.pulse(i*us)  
            delay(1000*ms)
            self.led0.pulse(1000*ms)
            print(i)
