from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 
 
val = IntVar(value=10)
 
ttk.Label(textvariable=val).pack(anchor=NW)
 
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=val)
horizontalScale.pack(anchor=NW)
 
root.mainloop()
