

class Sim:

    def __init__(self, df):
        self.T_in =0
        self.T_out=0
        self.P_in=0
        self.P_out=0
        self.df = df

    def interpolate(self, T, v1_lower, v1_upper, v2_lower, v2_upper):
        try:
            v1_lower = float(v1_lower)
            v1_upper = float(v1_upper)
            v2_lower = float(v2_lower)
            v2_upper = float(v2_upper)
        except ValueError:
            print("interpolat parameters were incorrect")

        m = (v2_upper - v2_lower) / (v1_upper - v1_lower)
        b = v2_upper - (v1_upper * m)
        return T * m + b



    def v_lookup(self,value1, value2, T):
        # Identify Indexis to interpolate from

        i = 0
        ls1 = self.df[value1].values
        ls2 = self.df[value2].values

        # try:
        while ls1[i] < T and i < len(ls1) - 1:
            print(i)
            i += 1
    
        v1_lower = ls1[i - 1]
        v1_upper = ls1[i]
        v2_lower = ls2[i - 1]
        v2_upper = ls2[i]
        # except IndexError:
        #     return None

        return self.interpolate(T, v1_lower, v1_upper, v2_lower, v2_upper)