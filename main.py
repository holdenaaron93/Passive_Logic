
import pandas as pd
from pump import Pump
from solar import Solar
from application import Application
from tkinter import Tk 


n_p = .85 #efficency from pump
w_p = 1 #work from pump

T_i = 60
filepath = 'H2O_TempSat-1.csv'
df = pd.read_csv(filepath)

if __name__ == "__main__":

    solar = Solar(df)
    pump = Pump(df, n_p, w_p)
    root = Tk()
    root.title("solar temperature")
    app = Application(root, solar, pump)
    root.mainloop()