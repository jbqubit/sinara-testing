from artiq import *
import numpy as np
import time

class TestHDF5(EnvExperiment):
    """Test HDF5"""
    def build(self):
        pass

    def run(self):

        tests = [
            True,
            [True, False],
            int(1234),
            [1, 2, 3]*3,
            float(1234),
            [1.1, 1.2, 1.3]*3,
            complex(1, 1),
            [complex(1,1), complex(1,2), complex(1,3)]*3,
            "asdf",
            ["asdf", "lkj"]*3,
            np.array(np.random.random(10), dtype=np.float32),
            np.array(np.random.random(10), dtype=np.float64),
            np.array(np.random.random(10), dtype=np.int32),
            np.array(np.random.random(10), dtype=np.int64),
            np.array(np.random.random(10), dtype=np.complex64),
            np.array(np.random.rand(10, 10), dtype=np.float32),
            np.array(np.random.rand(10, 10, 10), dtype=np.float32)
        ]

        for t in tests:
            self.set_dataset("test", t,
                              persist=False, save=False, broadcast=False)
            self.set_dataset("test", t,
                              persist=False, save=False, broadcast=True)
            self.set_dataset("test", t,
                              persist=False, save=True, broadcast=False)
            self.set_dataset("test", t,
                              persist=True, save=False, broadcast=False)
            self.set_dataset("test", t,
                              persist=True, save=True, broadcast=True)
