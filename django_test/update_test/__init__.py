import Tkinter
import ttk 
 
master = Tkinter.Tk()
 
variable = Tkinter.StringVar(master)
variable.set("one") # default value
 
w = ttk.Combobox(master, textvariable=variable, values=["one", "two", "three"])
w.pack()
 
master.mainloop()