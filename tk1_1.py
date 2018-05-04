# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:00:54 2018

@author: wegmarken
"""
import tkinter as tk
import my_date_picker as mdp
from datetime import datetime
import math
import configparser

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

class Config:
    def __init__(self):
        filename = "config.ini"
        config = configparser.ConfigParser()
        rd = config.read(filename)
        if rd == []:
            config["DEFAULT"] = {"IniAmount": "1000", "MonthlyIncome": "100"}
            with open(filename, 'w') as configfile:
                config.write(configfile)
        self.ini_amount = float(config["DEFAULT"]["IniAmount"])
        self.monthly_income = float(config["DEFAULT"]["MonthlyIncome"])

class MainGUI:
    def __init__(self, root):
        root = root
        root.title("Fin")
        root.geometry("640x480")

        self.mainframe = tk.Frame(root)
        self.mainframe.grid(column=0, row=0)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

    def add_date_field(self, row, col, var, ltext):
        label = tk.Label(self.mainframe, text=ltext)
        entry = tk.Entry(self.mainframe, textvariable=var)
        btn = tk.Button(self.mainframe, text="Date", bg="white", fg="blue", command=lambda: mdp.MyDatePicker(entry))
        label.grid(column=col, row=row)
        entry.grid(column=col + 1, row=row)
        btn.grid(column=col + 2, row=row)

    def add_result_field(self, row, col, func, var):
        btn = tk.Button(self.mainframe, text="Result", bg="white", fg="blue", command=func)
        label = tk.Label(self.mainframe, textvariable=var)
        btn.grid(column=col, row=row)
        label.grid(column=col + 1, row=row)

    def add_num_entry_field(self, row, col, var, ltext):
        label = tk.Label(self.mainframe, text=ltext)
        entry = tk.Entry(self.mainframe, textvariable=var)
        label.grid(column=col, row=row)
        entry.grid(column=col + 1, row=row)



root = tk.Tk()
m_gui = MainGUI(root)

config = Config()
today = datetime.today().strftime('%Y-%m-%d')

start_amount = tk.DoubleVar()
start_amount.set(config.ini_amount)
m_gui.add_num_entry_field(row=1, col=1, var=start_amount, ltext="Start Amount")

start_date = tk.StringVar()
start_date.set(today)
m_gui.add_date_field(row=2, col=1, var=start_date, ltext="Start Date")

month_income = tk.DoubleVar()
month_income.set(config.monthly_income)
m_gui.add_num_entry_field(row=3, col=1, var=month_income, ltext="Monthly Income")

end_mi_date = tk.StringVar()
end_mi_date.set(today)
m_gui.add_date_field(row=4, col=1, var=end_mi_date, ltext="End In. Date")

end_date = tk.StringVar()
end_date.set(today)
m_gui.add_date_field(row=5, col=1, var=end_date, ltext="End Date")
res = tk.DoubleVar()
def fres():
    d1 = days_between(end_mi_date.get(), start_date.get())
    to_add = math.floor(d1/30)*month_income.get()
    res.set(start_amount.get() + to_add)

m_gui.add_result_field(row=7, col=1, func=fres, var=res)

root.mainloop()




