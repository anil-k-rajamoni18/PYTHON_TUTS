#imports
import tkinter

from  tkinter import *

#main windows

root = tkinter.Tk()

root.title("DEMO GUI")

root.geometry("600x600")

#widgets

# Label

label = tkinter.Label(root,text="Hey Python").pack()

label1 = tkinter.Label(root,text="Hi").pack()



#run the gui app

root.mainloop()
