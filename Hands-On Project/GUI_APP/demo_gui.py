# imports

import tkinter
from tkinter import *

from tkinter import messagebox
# initalisation

root = tkinter.Tk()

root.title("Demo_GUI")
root.geometry("600x600")


# label
# label = tkinter.Label(root,text="Hey Python").pack()



# b = Button(root,text="Click me ",bg = "orange",fg="red")
# b.grid(row=4,column=4)


# b1 = Button(root,text="Login ",bg = "orange",fg="red")
# b1.grid(row=5,column=5)


# radio 
# r = Radiobutton(root,text="Python",value=1)
# r.grid(column=2,row=2)

# r1 = Radiobutton(root,text="Script",value=2)
# r1.grid(column=2,row=3)

# r2 = Radiobutton(root,text="Java",value=3)
# r2.grid(column=2,row=4)

# r3 = Radiobutton(root,text="C++",value=4)
# r3.grid(column=2,row=5)


# # # entry
t = Entry(root,width=40)
t.grid(column=3,row=6)

# # message 
def Button1():
	messagebox.showinfo("status","Hello Python")

b1=Button(root , text = "Python Life",command=Button1)
b1.pack()
b1.grid(column=4,row=7)



root.mainloop()
