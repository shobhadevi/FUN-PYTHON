from tkinter import *
from tkinter.ttk import *
tk=Tk()
load=Progressbar(tk,orient=HORIZONTAL,length=1000,mode='determinate')
def bar():
    import time
    load['value']=20
    tk.update_idletasks()
    time.sleep(1)
    load['value']=50
    tk.update_idletasks()
    time.sleep(1)
    load['value']=100
    tk.update_idletasks()
    time.sleep(1)
    load['value']=150
    tk.update_idletasks()
    time.sleep(1)
    load['value']=170
    tk.update_idletasks()
    time.sleep(1)
    load['value']=1000
    tk.update_idletasks()
    time.sleep(1)
load.pack()
Button(tk,text='START',command=bar).pack()
mainloop()





