
from sim import Sim
import numpy as np

class Pump(Sim):
    def __init__(self, df, n_p, w_p):
        super().__init__(df)
        self.n_p = n_p
        self.w_p = w_p

    def run(self, P_in):

        #update states
        v1 = self.v_lookup('P_kPa','S_volume', P_in)
        if not v1:
            return None
        self.P_out = self.n_p * self.w_p / v1 + P_in
        return self.P_out
