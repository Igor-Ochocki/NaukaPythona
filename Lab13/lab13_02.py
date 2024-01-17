# Dołożyć dodatkowo dwie nowe etykiety i rozłożyć w nowej linii (całość w kształcie /)
# zamienić widżety dostępne w module tkinter.ttk (nowszym) (Frame i Label)

from tkinter import *
from tkinter import ttk

# część główna
root = Tk()
# ustawienie tytułu okna głównego:
root.title("Interfejs GUI")
# rozmiar wyrażony w pikselach:
root.geometry("300x100")
# uruchamia pętlę zdarzeń obiektu root:

# utworzenie w oknie ramki jako pojemnika na inne widżety tzn. przechowuje inne elementy:
# za każdym razem, gdy tworzony jest nowy widżet
# należy przekazać do jego konstruktora obiekt nadrzędny (root):
app = Frame(root)

# Metodę grid() posiadają wszystkie widżety.
# Jest ona związana z menedżerem układów (ang. layout manager),
# który umożliwia rozplanowanie położenia widżetów.
app.grid()
# pozostałe metody związane z układem widżetów: # app.pack() # app.place()

# utwórz w ramce etykietę:
lbl = Label(app, text="Hello Python!")
# przy przekazaniu obiektu app do konstruktora obiektu klasy Label powoduje to,
# że ramka, do której odwołuje się zmienna app, staje się obiektem nadrzędnym widżetu Label.

# polecenie poniższe zapewnia widoczność etykiety.
lbl.grid()

# uruchomienie pętli zdarzeń obiektu root:
root.mainloop()
