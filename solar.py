
from sim import Sim
import numpy as np

class Solar(Sim):

    def __init(self, df):
        super().__init__(df)

    def run(self,T_in, D, m_dot, L_radiation, q_dprime):
        self.T_out = 98 ##Guess Value
        self.T_in = T_in
        error = 1

        while error >= .0001:
            T_out2 = self.T_out
            T_m = (self.T_out + self.T_in) / 2
            cp = self.v_lookup('Temp','Cpf', T_m)
            if not cp:
                return None
            #upadte state
            self.T_out = (np.pi * D * L_radiation * q_dprime) / (m_dot * cp * 1000) + self.T_in
            error = abs(self.T_out - T_out2)


        return self.T_out
