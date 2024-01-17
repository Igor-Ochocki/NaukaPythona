# Dołożyć przycisk do zamknięcia aplikacji
# zamienić widżety dostępne w module tkinter.ttk (nowszym) (Frame i Button)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

top = Tk()
top.geometry("150x100")


def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")


bttn1 = Button(top, text="Hello", command=helloCallBack)
bttn2 = Button(top, text="Zamknij program", command=top.quit)
bttn1.place(relx=0.5, rely=0.5, anchor=CENTER)
bttn2.place(relx=0.5, rely=0.9, anchor=S)
top.mainloop()
