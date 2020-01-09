
from sim import Sim
import numpy as np

class Pump(Sim):
    def __init__(self, df):
        super().__init__(df)


    def run(self, T_in, D , L_total,m_dot):



        #update states
        s_vol= self.v_lookup('Temp','S_volume', T_in)
        u = self.v_lookup('Temp', 'Viscosity', T_in)




        if not s_vol:
            return None
        if not u:
            return None


        vel = m_dot*s_vol*np.pi*D**2/4
        head_loss = self.Head_Loss(L_total,vel,D,s_vol,u)
        pump_head = head_loss * 1000

        return pump_head



    def Head_Loss(self,L_total,vel,D,s_vol,u):
        f = self.friction_factor(D,vel,s_vol,u)
        h_l = f * L_total/D*vel/(2*9.81)
        return h_l


    def friction_factor(self,D,vel,s_vol,u):
        Re = vel*D/(s_vol*u)
        if Re >= 2300:
            print("This Sim is not designed for turbulent flow")
        f = 64/Re
        return f
