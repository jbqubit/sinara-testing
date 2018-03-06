from artiq.experiment import *
import artiq.language

class TriggerTest(EnvExperiment):
    """test_ext_trig
    purpose: demonstrate external triggering of waveform sawg0 
    expectation: no phase offset between ttl_sma and sawg0 across multiple trigger events
    setup: 
        - ext_trig is square wave 1 kHz, 3 Vpp, 1.5 V offset, 50% duty cycle
        - apply ext_trig to USER_GPIO_N on KC705
        - apply ext_trig to CH0 on oscilloscope
        - apply sawg0 to CH1 on oscilloscope
        - trigger oscilloscope on CH0, 1 V amplitude, normal mode
        - set oscilloscope timebase to 1 us
    """
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("led")
        self.setattr_device("ttl_sma")
        self.setattr_device("sawg0")

    @kernel 
    def ext_trig(self, trig_period_mu, blocking=True):
        done = False
        while not done:
            t0 = now_mu()
            self.ttl_sma.gate_rising_mu(trig_period_mu)
            t1 = self.ttl_sma.timestamp_mu()
            if t1 > 0:  # rising edge during gate
                delay_mu(trig_period_mu + t1 - t0)
                done = True
            elif blocking:  # no rising edge during gate
                pass
            else:  # no rising edge during gate
                return  

    @kernel
    def run(self):
        self.core.reset()
        delay(300*us)
        self.sawg0.reset()
        self.ttl_sma.input()
        delay(10 * ms)
        

        f0 = 5*MHz
        a0 = 1.0
        trig_period = 1*ms
        
        self.sawg0.frequency1.set(f0)
        trig_period_mu = self.core.seconds_to_mu(trig_period)

        while True:
            self.ext_trig(trig_period_mu)
            self.sawg0.phase1.set(0.)    
            self.sawg0.amplitude1.set(a0)
            delay(trig_period/4)
            
            self.sawg0.amplitude1.set(0.)
