#This will be a citation generator

import tkinter as tk

mw = tk.Tk()
mw.geometry('300x200')
mw.title("BEST Citation Generator")
greeting = tk.Label(text="Hello! Please pick which format you would like to use!") #Greeting message prompting user to select which format they would like to use
greeting.grid(row = 0)


def OpenNewWindow_op1(): #Opens a new window for MLA9
    nw1 = tk.Toplevel(mw) #Where nw means "new window"
    nw1.title("MLA9 Citation Generator")
    nw1.geometry('400x400')
    tk.Label(nw1, text="Please input all the information known below!").pack()
    tk.Label(nw1, text="First name")

def OpenNewWindow_op2(): #Opens a new window for APA7
    nw2 = tk.Toplevel(mw)
    nw2.title("APA7 Citation Generator")
    nw2.geometry('400x400')
    tk.Label(nw2, text="Please input all the information known below!").pack()


def OpenNewWindow_op3(): #Opens a new window for Chicago style
    nw3 = tk.Toplevel(mw)
    nw3.title("CHICAGO Citation Generator")
    nw3.geometry('400x400')
    tk.Label(nw3, text="Please input all the information known below!").pack()

def SeeCitations():  # Opens a new window for viewing the citations
    nw4 = tk.Toplevel(mw)
    nw4.title("Citation Viewer")
    nw4.geometry('400x400')
    #If (no citations)
        #tk.label("No citations so far!")
    #else:
        #display citations


def MLA9_Variables():
    Firstname1 = fn1.get(nw1)
    Lastname1 = ln1.get(nw1)
    ArticleTitle1 = at1.get(nw1)
    WebsiteTitle1 = wt1.get(nw1)
    Publisher1 = pub1.get(nw1)
    Date1 = date1.get(nw1) #In the form of Day, month, year
    URL1 = url1.get(nw1)


op1 = tk.Button(mw, text='MLA9', command=OpenNewWindow_op1)
op1.grid(row = 1, column = 0, padx = 5, pady=5)

op2 = tk.Button(mw, text='APA7', command=OpenNewWindow_op2)
op2.grid(row = 2, column = 0, padx = 5, pady=5)

op3 = tk.Button(mw, text='CHICAGO', command=OpenNewWindow_op3)
op3.grid(row = 3, column = 0, padx = 5, pady=5)

op4 = tk.Button(mw, text='Citation Viewer', command=SeeCitations)
op4.grid(row = 3, column = 0, padx = 5, pady = 5)

mw.mainloop()