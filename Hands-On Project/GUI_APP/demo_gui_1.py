import tkinter as tk

from tkinter import ttk

from tkinter import scrolledtext

from tkinter import *

root = tk.Tk();


root.title("Demo_GUI2")
root.geometry("600x600")

ttk.Label(root,text="Python Life",background = "blue",foreground="white",
		font =("Times new roman",15)).grid(row=0,columns=1)

Button(root,text = "Click here " , bg = "orange",fg="red").grid(column=2,row=2)
# combobox 

n = tk.StringVar()
course = ttk.Combobox(root,width=27,textvariable=n)
course['values']=("Python",
					"Django",
					"machine learning")

course.grid(column=1,row=5)
course.current()


#scrolltext
text = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=10)

text.grid(column=0,pady=10,padx=10)
text.focus()

root.mainloop()