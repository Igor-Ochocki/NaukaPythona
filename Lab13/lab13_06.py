# https://www.tutorialspoint.com/python3/tk_button.htm
# zmodyfikuj program, aby na dole okna pojawiała się informacja, która pobierana jest z pola typu Entry

from tkinter import *
from datetime import *
from tkinter import messagebox


top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)
F1 = Label(top, text = "Pobrany tekst: ")
F1.pack(side = LEFT)
F1.place(relx=0, rely=0.7)
F1 = Entry.get()

top.mainloop()
