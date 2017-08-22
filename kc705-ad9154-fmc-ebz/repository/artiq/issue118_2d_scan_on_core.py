from artiq.experiment import *

class Issue118(EnvExperiment):
    """issue118.py
    purpose: test as per github Issue
    https://github.com/m-labs/artiq/issues/118
    """

    def build(self):
        self.setattr_device("core")
        self.setattr_device("led")
        self.setattr_device("ttl_sma")
        self.setattr_argument("a", Scannable(default=RangeScan(0, 10, 4)))
        self.setattr_argument("b", Scannable(default=RangeScan(0, 10, 4)))
        self.setattr_argument("c", Scannable(default=RangeScan(0, 10, 4)))
        self.msm = MultiScanManager(
            ("a", self.a),
            ("b", self.b),
            ("c", self.c),
        )

        self.msmaslist = []
        for point in self.msm:
            print("a={} b={} c={}".format(point.a, point.b, point.c))
            self.msmaslist.append([point.a, point.b, point.c])


    @kernel
    def run_fail(self):
        self.ttl_sma.output()
        for point in self.msm:
            self.ttl_sma.pulse(point.a*us)
            delay(point.b*us)
            self.ttl_sma.pulse(point.c*us)
            delay(1*ms)
        delay(1*ms)

    @kernel
    def run(self):
        delay(10*ms)
        #self.ttl_sma.output()
        #delay(10 * ms)

        a=0.; b=0.; c=0.
        for x in self.msmaslist:
            a = x[0]
            b = x[1]
            c = x[2]
        #     #print(a)
        #     #
            self.ttl_sma.pulse(a*us)
        #     # delay(b*us)
        #     # self.ttl_sma.pulse(c*us)
        #     delay(100*ms)
        delay(1*ms)