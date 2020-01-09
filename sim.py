
import numpy as np
class Sim:

    def __init__(self, df):
        self.T_in =0
        self.T_out=0
        self.P_in=0
        self.P_out=0
        self.df = df



    def v_lookup(self,value1, value2, T):
        # Identify Indexis to interpolate from
        i = 0
        ls1 = self.df[value1].values
        ls2 = self.df[value2].values

        while ls1[i] < T and  i < len(ls1) - 1:
            i += 1

        v1_lower = ls1[i - 1]
        v1_upper = ls1[i]
        v2_lower = ls2[i - 1]
        v2_upper = ls2[i]


        return np.interp(T, [v1_lower, v1_upper], [v2_lower, v2_upper])

