from artiq.experiment import *


class SAWGTestSines(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl_sma_out")
        self.sawgs = [self.get_device("sawg"+str(i)) for i in range(8)]
        self.freq_list = self.linspace(100.0*MHz, 240.0*MHz, 100)
        # self.amp_list = self.linspace(0.0, 1.0, 100)
        self.t_list = self.linspace(1*us, 133*us, 100)

    def linspace(self, start, stop, num):
        dx = (stop-start)/(num-1) 
        return [start+n*dx for n in range(num)]

    @kernel
    def run(self):
        self.core.reset()
        delay(1*ms)
        
        while True:
            self.k1()            

    @kernel
    def k3(self):
        self.ttl_sma_out.output()
        for t in self.t_list:
            delay(20*us)
            self.ttl_sma_out.pulse(t)

    
    @kernel
    def k1(self):
        for freq in self.freq_list:
            delay(100*ms)
            print(freq)
            for sawg in self.sawgs:
                sawg.amplitude1.set(0.99)
                sawg.frequency0.set(freq)
                sawg.frequency1.set(50*MHz)
                sawg.frequency2.set(-50*MHz)
                delay(1*ms)
                
