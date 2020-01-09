
import pandas as pd
from pump import Pump
from solar import Solar
from application import Application
from tkinter import Tk 




T_i = 60
filepath = 'H2O_TempSat-1.csv'
df = pd.read_csv(filepath)

if __name__ == "__main__":

    solar = Solar(df)
    pump = Pump(df)
    root = Tk()
    root.title("Heat Transfer Sim")
    app = Application(root, solar, pump)
    root.mainloop()