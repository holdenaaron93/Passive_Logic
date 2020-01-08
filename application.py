
from tkinter import *

"""
        self.T_in = app.T_out_tank_s.get()
        D = app.D_s.get()
        m_dot = app.m_s.get()
        L_radiation = app.L_s.get()
        q_dprime = app.solar_s.get()

        input parameters: T_in, D, m_dot, L_radiation, q_dprime
"""

"""
        self.T_out = solar1.T_out
        self.P_in = self.v_lookup('Temp','P_kPa',self.T_in)
        
"""

class Application(Frame):
    def __init__(self,root,solar,pump):
        super(Application, self).__init__()
        Frame.__init__(self,root)
        self.root = root
        self.solar = solar
        self.pump = pump
        self.grid()
        self.create_sliders()

    def handle_solar_run(self,x):
        T_out = self.solar.run(self.T_out_tank_s.get(), 
                               self.D_s.get(), 
                               self.m_s.get(), 
                               self.L_s.get(), 
                               self.solar_s.get())
        #print(T_out)

        ## this is where you would use the value for T_out for displaying on GUI

    def handle_pump_run(self,x):
        P_out = self.pump.run(self.pump.v_lookup('Temp', 'P_kPa', self.handle_solar_run(x)))
        #print(P_out)

    def create_sliders(self):

        solar_l = Label(self.root, text="Solar Radiation")
        self.solar_s = Scale(self.root, from_=0, to=3000, orient=HORIZONTAL, command=self.handle_solar_run)

        D_l = Label(self.root, text="Duct Diameter")
        self.D_s = Scale(self.root, from_=.01, to=1, orient=HORIZONTAL, resolution=.01, command=self.handle_solar_run)

        L_l = Label(self.root, text="Radiation Exposed Duct")
        self.L_s = Scale(self.root, from_=.2, to=10, orient=HORIZONTAL, resolution=0.2, command=self.handle_solar_run)

        m_l = Label(self.root, text="Mass flow Rate")
        self.m_s = Scale(self.root, from_=.01, to=2, orient=HORIZONTAL, resolution=0.01, command=self.handle_solar_run)

        T_out_tank_l = Label(self.root, text='Tank Outlet Temp')
        self.T_out_tank_s = Scale(self.root, from_=1, to=99, orient=HORIZONTAL, command=self.handle_solar_run)

        Air_l = Label(self.root, text="Ambient Air Temp")
        self.Air_s = Scale(self.root, from_=10, to=75, orient=HORIZONTAL, command=self.handle_pump_run)
        #self.Air_s = Scale(root, from_=10, to=75, orient=HORIZONTAL, command=handle_pump_run)

        #Solar_T_out = Label(root,text=sim.T_out)

        self.solar_s.set(2000)
        self.D_s.set(.06)
        self.L_s.set(6.65)
        self.m_s.set(.01)
        self.T_out_tank_s.set(20)
        self.Air_s.set(25)

        solar_l.grid()
        self.solar_s.grid()
        D_l.grid()
        self.D_s.grid()
        L_l.grid()
        self.L_s.grid()
        m_l.grid()
        self.m_s.grid()
        T_out_tank_l.grid()
        self.T_out_tank_s.grid()
        Air_l.grid()
        self.Air_s.grid()