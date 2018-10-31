from artiq.experiment import *


class Urukul9910spinEchoDemo(EnvExperiment):
    """
    Demonstrate spin echo type experiment. Signals:
    * ttl4 is marker for start of experiment
    * ttl5 is marker for intervals when microwaves are applied to qubit
    * urukul0_ch0 is reference tone
    * urukul0_ch1 is carrier tone (spin flip)
    """
    def build(self):
        self.setattr_device("core")
        self.setattr_device("ttl4")
        self.setattr_device("ttl5")
        self.setattr_device("urukul0_cpld")
        self.urukul0_ch0 = self.get_device("urukul0_ch0")
        self.urukul0_ch1 = self.get_device("urukul0_ch1")
        self.ttl_urukul0_sw0 = self.get_device("ttl_urukul0_sw0")
        self.ttl_urukul0_sw1 = self.get_device("ttl_urukul0_sw1")
        self.setattr_device("led0")

    @kernel
    def carrier_pulse(self, f, t, p):
        self.urukul0_ch1.set(f, p)
        with parallel:
            self.ttl5.pulse(t)
            self.ttl_urukul0_sw1.pulse(t)

    @kernel
    def run(self):
        self.core.reset()
        self.core.break_realtime()
        delay(1*ms)

        t_pi = 1000*ns
        t_arm = 20*ns
        f0 = 10*MHz

        # reference tone
        self.urukul0_ch0.set(f0, 0.0, 1.0)  
        self.urukul0_ch0.set_att(0.0)
        self.ttl_urukul0_sw0.on()
        # carrier
        self.urukul0_ch1.set(f0, 0.0, 1.0)  
        self.urukul0_ch1.set_att(0.0)

        while True:
            self.ttl4.pulse(100*ns)  # start pulse            
            self.carrier_pulse(f0, t_pi/2, 0.0)
            delay(t_arm)
            self.carrier_pulse(f0, t_pi, 0.5)
            delay(t_arm)
            self.carrier_pulse(f0, t_pi/2, 0.0)

            self.led0.pulse(50*ms) 
            delay(50*ms)

