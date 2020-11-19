from tkinter import *
import backend

class Window():
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Návrh nářadí")

        # Nadobka
        nad1 = Label(window, text = "Nádobka")
        nad1.grid(row=4, column=0)

        nad2 = Label(window, text = "Průměr nádobky")
        nad2.grid(row=5, column=1)

        nad3 = Label(window, text = "Výška nádobky")
        nad3.grid(row=6, column=1)

        nad4 = Label(window, text = "Tloušťka komínku")
        nad4.grid(row=7, column=1)

        nad5 = Label(window, text = "Tloušťka vnitřního laku")
        nad5.grid(row=8, column=1)

        nad6 = Label(window, text = "Tloušťka vnějšího laku")
        nad6.grid(row=9, column=1)

        nad7 = Label(window, text = "Průměr komínku")
        nad7.grid(row=10, column=1)

        nad8 = Label(window, text = "Tlaková specifikace")
        nad8.grid(row=11, column=1)

        self.prumNad_value = DoubleVar()
        self.prumNad = Entry(window,textvariable=self.prumNad_value, width=5)
        self.prumNad.grid(row=5, column=2)

        self.vysNad_value = IntVar()
        self.vysNad = Entry(window,textvariable=self.vysNad_value, width=5)
        self.vysNad.grid(row=6, column=2)

        self.tlKom_value = DoubleVar()
        self.tlKom = Entry(window,textvariable=self.tlKom_value, width=5)
        self.tlKom.grid(row=7, column=2)

        self.tlIntLak_value = DoubleVar()
        self.tlIntLak = Entry(window,textvariable=self.tlIntLak_value, width=5)
        self.tlIntLak.grid(row=8, column=2)

        self.tlExtLAk_value = DoubleVar()
        self.tlExtLAk = Entry(window,textvariable=self.tlExtLAk_value, width=5)
        self.tlExtLAk.grid(row=9, column=2)

        self.prumKom_value = DoubleVar()
        self.prumKom = Entry(window,textvariable=self.prumKom_value, width=5)
        self.prumKom.grid(row=10, column=2)

        self.tlak_value = IntVar()
        self.tlak = Entry(window,textvariable=self.tlak_value, width=5)
        self.tlak.grid(row=11, column=2)

        jedn4 = Label(window, text = "mm")
        jedn4.grid(row=5, column=3)

        jedn5 = Label(window, text = "mm")
        jedn5.grid(row=6, column=3)

        jedn6 = Label(window, text = "mm")
        jedn6.grid(row=7, column=3)

        jedn7 = Label(window, text = "mm")
        jedn7.grid(row=8, column=3)

        jedn8 = Label(window, text = "mm")
        jedn8.grid(row=9, column=3)

        jedn9 = Label(window, text = "mm")
        jedn9.grid(row=10, column=3)

        jedn10 = Label(window, text = "bar")
        jedn10.grid(row=11, column=3)

        # rameno
        ram1 = Label(window, text = "Rameno")
        ram1.grid(row=13, column=0)

        ram2 = Label(window, text = "Průměr ramena")
        ram2.grid(row=14, column=1)

        ram3 = Label(window, text = "Tloušťka ramena")
        ram3.grid(row=15, column=1)

        ram4 = Label(window, text = "Ůhel ramena")
        ram4.grid(row=18, column=1)

        ram5 = Label(window, text = "Počet tahu")
        ram5.grid(row=19, column=1)

        ram6 = Label(window, text = "Vule chytáku")
        ram6.grid(row=17, column=1)

        ram7 = Label(window, text = "Tvar ramene")
        ram7.grid(row=20, column=1)

        self.prumRam_value = DoubleVar()
        self.prumRam = Entry(window,textvariable=self.prumRam_value, width=5)
        self.prumRam.grid(row=14, column=2)

        self.tlRam_value = DoubleVar()
        self.tlRam = Entry(window,textvariable=self.tlRam_value, width=5)
        self.tlRam.grid(row=15, column=2)

        self.uhRam_value = DoubleVar()
        self.uhRam = Entry(window,textvariable=self.uhRam_value, width=5)
        self.uhRam.grid(row=18, column=2)

        self.pocTah_value = IntVar()
        self.pocTah = Entry(window,textvariable=self.pocTah_value, width=5)
        self.pocTah.grid(row=19, column=2)

        self.vuleChyt_value = DoubleVar()
        self.vuleChyt = Entry(window,textvariable=self.vuleChyt_value, width=5)
        self.vuleChyt.grid(row=17, column=2)

        self.tvarRam_value = StringVar()
        self.tvarRam = Entry(window,textvariable=self.tvarRam_value, width=5)
        self.tvarRam.grid(row=20, column=2)

        jedn11 = Label(window, text = "mm")
        jedn11.grid(row=14, column=3)

        jedn12 = Label(window, text = "mm")
        jedn12.grid(row=15, column=3)

        jedn13 = Label(window, text = "°")
        jedn13.grid(row=18, column=3)

        jedn14 = Label(window, text = "-")
        jedn14.grid(row=19, column=3)

        jedn15 = Label(window, text = "mm")
        jedn15.grid(row=17, column=3)

        jedn16 = Label(window, text = "-")
        jedn16.grid(row=20, column=3)

        # Cesta projektu
        projectPath = Label(window, text = "Cesta projektu:")
        projectPath.grid(row=21, column=0)

        self.projPath_value = StringVar()
        self.projPath = Entry(window,textvariable=self.projPath_value, width=40)
        self.projPath.grid(row=21, column=1, columnspan=3)
        
        b4=Button(window, text="Vytvor", width = 5, command=self.createDir)
        b4.grid(row=21, column=4)

        # Oznacenie naradia
        oznNar = Label(window, text = "Oznacenie naradia:")
        oznNar.grid(row=22, column=0)

        self.oznNar_value = StringVar()
        self.oznNar = Entry(window,textvariable=self.oznNar_value, width=34)
        self.oznNar.grid(row=22, column=1, columnspan=2)

        self.initNo_value = StringVar()
        self.initNo = Entry(window,textvariable=self.initNo_value, width=5)
        self.initNo.grid(row=22, column=3)

        b5=Button(window, text="Vytvor", width = 5,command=self.set_numbering)
        b5.grid(row=22, column=4)

        # Tlacitka
        b1=Button(window, text="OK",  width = 10)
        b1.grid(row=23, column=0)

        b2=Button(window, text="Reset", width = 10)
        b2.grid(row=23, column=1)

        b3=Button(window, text="Konec", width = 10, command=self.window.destroy)
        b3.grid(row=23, column=2)

# FUNCTIONS
    def createDir(self):
        self.path = self.projPath_value.get() 
        backend.Folder().createWrkDir(self.path)
    
    def get_numbering(self):
        self.d_nad = self.prumNad_value.get()
        self.h_nad = self.vysNad_value.get()
        self.tlak = self.tlak_value.get()
        self.tvar_ramena = self.tvarRam_value.get()
        self.poc_cislo = self.initNo_value.get()
        return(f"NA-{self.d_nad}-{self.h_nad}-{self.tlak}-{self.tvar_ramena}{self.poc_cislo}")

    def set_numbering(self):
        self.oznNar.insert(END,self.get_numbering())


window=Tk()
Window(window)
window.mainloop()