# - application = webapps(websites)
# - mobile apps
# - standalone apps

# import tkinter as tk
# #object for Tkinter.
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()

# #running app.
# r.mainloop()


# from tkinter import *
# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()


from tkinter import *
master = Tk()
master.geometry("400x400")
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(master, text='Select Gender').grid(row=3)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(master, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(master, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.grid(row=3, column=1)
C2.grid(row=4, column=1)

 
mainloop()