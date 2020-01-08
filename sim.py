

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
        ls1 = self.df[value1]
        ls2 = self.df[value2]

        while ls1[i] < T:
            i += 1
        print(ls1[i])
        print('Input Temperature value',T)

        # Interpolate
        v1_lower = ls1[i]
        v2_upper = ls1[i + 1]
        value_lower = ls2[i]
        value_upper = ls2[i + 1]

        m = (value_upper - value_lower) / (v2_upper - v1_lower)
        b = value_upper - (v2_upper * m)

        # calc  value
        value = T * m + b

        return value