#This will be a citation generator

import tkinter as tk

mw = tk.Tk()
mw.geometry('400x400')
mw.title("BEST Citation Generator")
greeting = tk.Label(text="Hello! Please pick which format you would like to use!")
greeting.grid(row = 0)


def OpenNewWindow_op1(): #Opens a new window for op1
    nw1 = tk.Toplevel(mw)
    nw1.title("op1 Citation Generator")
    nw1.geometry('400x400')


def OpenNewWindow_op2(): #Opens a new window for op2
    nw2 = tk.Toplevel(mw)
    nw2.title("op2 Citation Generator")
    nw2.geometry('400x400')


def OpenNewWindow_op3(): #Opens a new window for op3
    nw3 = tk.Toplevel(mw)
    nw3.title("op3 Citation Generator")
    nw3.geometry('400x400')


op1 = tk.Button(mw, text='Op1', command=OpenNewWindow_op1)
op1.grid(row = 1, column = 0, padx = 10)

op2 = tk.Button(mw, text='Op2', command=OpenNewWindow_op2)
op2.grid(row = 1, column = 1, padx = 10)

op3 = tk.Button(mw, text='Op3', command=OpenNewWindow_op3)
op3.grid(row = 1, column = 2, padx = 10)



mw.mainloop()