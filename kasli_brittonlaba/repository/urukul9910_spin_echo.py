from artiq.experiment import *


class Urukul9910spinEchoDemo(EnvExperiment):
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl0")
        self.setattr_device("ttl1")
        self.setattr_device("urukul0_cpld")
        self.urukul0_ch0 = self.get_device("urukul0_ch0")
        self.urukul0_ch1 = self.get_device("urukul0_ch1")
        self.setattr_device("led0")

    @kernel
    def run(self):
        self.core.reset()
        self.core.break_realtime()
        delay(1*ms)

        t_pi = 100*ns
        t_arm = 500*ns
        f0 = 10*MHz

        while True:
            self.ttl0.pulse(100*ns)  # start pulse
            self.urukul0_ch0.set(f0, 0.0)  # reference tone
            self.urukul0_ch1.set(f0, 0.0)  # carrier
            
            self.ttl1.pulse(t_pi/2)
            self.urukul0_ch1.set(f0, 0.5)
            delay(t_arm)
            self.ttl1.pulse(t_pi)
            self.urukul0_ch1.set(f0, 0.0)
            delay(t_arm)
            self.ttl1.pulse(t_pi/2)
            
            delay(1*ms) 
