# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:00:54 2018

@author: wegmarken
"""
import tkinter as tk
import my_date_picker as mdp


root = tk.Tk()
root.title("Fin")
root.geometry("320x240")

mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


start_l = tk.Label(mainframe, text="Start")
start_e = tk.Entry(mainframe)
startd_l = tk.Label(mainframe, text="Start Date")
startd_e = tk.Entry(mainframe)

def startd_b_clicked():
    mdp.MyDatePicker(startd_e)

startd_b = tk.Button(mainframe, text="Date", bg="white", fg="blue", command=startd_b_clicked)
col = 1
row = 1
start_l.grid(column=col, row=row)
start_e.grid(column=col+1, row=row)
row = row + 1
startd_l.grid(column=col, row=row)
startd_e.grid(column=col+1, row=row)
startd_b.grid(column=col+2, row=row)
row = row + 1

def res_b_clicked():
    print(startd_e.get())

res_b = tk.Button(mainframe, text="Result", bg="white", fg="blue", command=res_b_clicked)
res_b.grid(column=col, row=row)

#comment
root.mainloop()



