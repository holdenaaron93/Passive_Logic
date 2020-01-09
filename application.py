
from tkinter import *
import numpy as np

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
                               self.L_r_s.get(),
                               self.solar_s.get())

        if T_out > 112:
            solar_T_outv = Label(self.root, text='Boil!')


        #Creat GUI Widgets
        else:
            solar_T_outv = Label(self.root,text = np.around(T_out,decimals=1))

        #Display T_out Value to GUI
        solar_T_out = Label(self.root, text='Tank Inlet Temperature = ')
        solar_T_out.grid(row = 4, column = 2,rowspan =2)
        solar_T_outv.grid(row = 4, column = 3, rowspan=2)



        return T_out


    def handle_pump_run(self,x):
        head_loss = self.pump.run(self.handle_solar_run(x),
                              self.D_s.get(),
                              self.L_t_s.get(),
                              self.m_s.get())


        #Creat GUI Widgets
        head_lossl = Label(self.root, text = 'Head Loss = ')
        head_lossv = Label(self.root,text = np.around(head_loss,decimals=1))

        #Display T_out Value to GUI
        head_lossl.grid(row = 8, column = 2)
        head_lossv.grid(row = 8, column = 3)

    def handle_both(self,x):
        self.handle_pump_run(x)
        self.handle_solar_run(x)


    def create_sliders(self):

        solar_l = Label(self.root, text="Solar Radiation")
        self.solar_s = Scale(self.root, from_=0, to=3000, orient=HORIZONTAL, command=self.handle_solar_run)

        D_l = Label(self.root, text="Duct Diameter")
        self.D_s = Scale(self.root, from_=.01, to=1, orient=HORIZONTAL, resolution=.01, command=self.handle_both)

        L_r_l = Label(self.root, text="Length of Duct in Sun")
        self.L_r_s = Scale(self.root, from_=.2, to=10, orient=HORIZONTAL, resolution=0.2, command=self.handle_solar_run)

        m_l = Label(self.root, text="Mass flow Rate")
        self.m_s = Scale(self.root, from_=.01, to=2, orient=HORIZONTAL, resolution=0.01, command=self.handle_both)

        T_out_tank_l = Label(self.root, text='Tank Outlet Temp')
        self.T_out_tank_s = Scale(self.root, from_=1, to=99, orient=HORIZONTAL, command=self.handle_solar_run)

        L_t_l = Label(self.root, text="Total Duct length")
        self.L_t_s = Scale(self.root, from_=.2, to=10, orient=HORIZONTAL, resolution=0.2, command=self.handle_both)


        ##set slider initial values
        self.solar_s.set(2000)
        self.D_s.set(.06)
        self.L_r_s.set(6.65)
        self.m_s.set(.01)
        self.T_out_tank_s.set(20)
        self.L_t_s.set(8)

        #Snap labels and scales to gui
        ##solar
        solar_l.grid()
        self.solar_s.grid()
        D_l.grid()
        self.D_s.grid()
        L_r_l.grid()
        self.L_r_s.grid()
        m_l.grid()
        self.m_s.grid()

        ##tank
        T_out_tank_l.grid()
        self.T_out_tank_s.grid()



        ##pump
        L_t_l.grid()
        self.L_t_s.grid()