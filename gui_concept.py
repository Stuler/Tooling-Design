from tkinter import *
import backend

class Window():
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Návrh nářadí")

        # Nadobka
        nad1 = Label(window, text = "Nádobka")
        nad1.grid(row=0, column=0, sticky=W)

        nad2 = Label(window, text = "Průměr nádobky")
        nad2.grid(row=1, column=1, sticky=W)

        nad3 = Label(window, text = "Výška nádobky")
        nad3.grid(row=2, column=1, sticky=W)

        nad4 = Label(window, text = "Tloušťka komínku")
        nad4.grid(row=3, column=1, sticky=W)

        nad5 = Label(window, text = "Tloušťka vnitřního laku")
        nad5.grid(row=4, column=1, sticky=W)

        nad6 = Label(window, text = "Tloušťka vnějšího laku")
        nad6.grid(row=5, column=1, sticky=W)

        nad7 = Label(window, text = "Průměr komínku")
        nad7.grid(row=6, column=1, sticky=W)

        nad8 = Label(window, text = "Tlaková specifikace")
        nad8.grid(row=7, column=1, sticky=W)

        self.prumNad_value = IntVar(value=45)
        self.prumNad = Entry(window,textvariable=self.prumNad_value, width=5)
        self.prumNad.grid(row=1, column=2)

        self.vysNad_value = IntVar(value=159)
        self.vysNad = Entry(window,textvariable=self.vysNad_value, width=5)
        self.vysNad.grid(row=2, column=2)

        self.tlKom_value = DoubleVar(value=0.37)
        self.tlKom = Entry(window,textvariable=self.tlKom_value, width=5)
        self.tlKom.grid(row=3, column=2)

        self.tlIntLak_value = DoubleVar(value=0.02)
        self.tlIntLak = Entry(window,textvariable=self.tlIntLak_value, width=5)
        self.tlIntLak.grid(row=4, column=2)

        self.tlExtLAk_value = DoubleVar(value=0.02)
        self.tlExtLAk = Entry(window,textvariable=self.tlExtLAk_value, width=5)
        self.tlExtLAk.grid(row=5, column=2)

        self.prumKom_value = DoubleVar(value=25.4)
        self.prumKom = Entry(window,textvariable=self.prumKom_value, width=5)
        self.prumKom.grid(row=6, column=2)

        self.tlak_value = IntVar(value=12)
        self.tlak = Entry(window,textvariable=self.tlak_value, width=5)
        self.tlak.grid(row=7, column=2)

        jedn4 = Label(window, text = "mm")
        jedn4.grid(row=1, column=3, sticky=W)

        jedn5 = Label(window, text = "mm")
        jedn5.grid(row=2, column=3, sticky=W)

        jedn6 = Label(window, text = "mm")
        jedn6.grid(row=3, column=3, sticky=W)

        jedn7 = Label(window, text = "mm")
        jedn7.grid(row=4, column=3, sticky=W)

        jedn8 = Label(window, text = "mm")
        jedn8.grid(row=5, column=3, sticky=W)

        jedn9 = Label(window, text = "mm")
        jedn9.grid(row=6, column=3, sticky=W)

        jedn10 = Label(window, text = "bar")
        jedn10.grid(row=7, column=3, sticky=W)

        # rameno
        ram1 = Label(window, text = "Rameno")
        ram1.grid(row=8, column=0, sticky=W)

        ram2 = Label(window, text = "Průměr ramena")
        ram2.grid(row=9, column=1, sticky=W)

        ram3 = Label(window, text = "Tloušťka ramena")
        ram3.grid(row=10, column=1, sticky=W)

        ram6 = Label(window, text = "Vule chytáku")
        ram6.grid(row=11, column=1, sticky=W)

        ram4 = Label(window, text = "Ůhel ramena")
        ram4.grid(row=12, column=1, sticky=W)

        ram5 = Label(window, text = "Počet tahu")
        ram5.grid(row=13, column=1, sticky=W)

        ram7 = Label(window, text = "Tvar ramene")
        ram7.grid(row=14, column=1, sticky=W)

        self.prumRam_value = DoubleVar()
        self.prumRam = Entry(window,textvariable=self.prumRam_value, width=5)
        self.prumRam.grid(row=9, column=2)

        self.tlRam_value = DoubleVar()
        self.tlRam = Entry(window,textvariable=self.tlRam_value, width=5)
        self.tlRam.grid(row=10, column=2)

        self.vuleChyt_value = DoubleVar(value=0.03)
        self.vuleChyt = Entry(window,textvariable=self.vuleChyt_value, width=5)
        self.vuleChyt.grid(row=11, column=2)

        self.uhRam_value = DoubleVar()
        self.uhRam = Entry(window,textvariable=self.uhRam_value, width=5)
        self.uhRam.grid(row=12, column=2)

        self.pocTah_value = IntVar()
        self.pocTah = Entry(window,textvariable=self.pocTah_value, width=5)
        self.pocTah.grid(row=13, column=2)

        self.tvarRam_value = StringVar()
        self.tvarRam = Entry(window,textvariable=self.tvarRam_value, width=5)
        self.tvarRam.grid(row=14, column=2)

        jedn11 = Label(window, text = "mm")
        jedn11.grid(row=9, column=3, sticky=W)

        jedn12 = Label(window, text = "mm")
        jedn12.grid(row=10, column=3, sticky=W)

        jedn15 = Label(window, text = "mm")
        jedn15.grid(row=11, column=3, sticky=W)

        jedn13 = Label(window, text = "°")
        jedn13.grid(row=12, column=3, sticky=W)

        jedn14 = Label(window, text = "-")
        jedn14.grid(row=13, column=3, sticky=W)

        jedn16 = Label(window, text = "-")
        jedn16.grid(row=14, column=3, sticky=W)
        
        # Seznam naradi
        Label(window, text = "Seznam nářadí").grid(row=0, column=5, sticky=W)

        self.stKr = IntVar()
        Checkbutton(window, text="Stahovací kroužky", variable=self.stKr).grid(row=1, column=5, sticky=W)

        self.chytaky = IntVar()
        Checkbutton(window, text="Chytáky", variable=self.chytaky).grid(row=2, column=5, sticky=W)

        self.vodPzdra = IntVar()
        Checkbutton(window, text="Vodící pouzdra", variable=self.vodPzdra).grid(row=3, column=5, sticky=W)

        self.navKr = IntVar()
        Checkbutton(window, text="Naváděcí kroužky", variable=self.navKr).grid(row=4, column=5, sticky=W)

        self.drzChyt = IntVar()
        Checkbutton(window, text="Držáky chytáků", variable=self.drzChyt).grid(row=5, column=5, sticky=W)

        self.sroubCepy = IntVar()
        Checkbutton(window, text="Šroubové čepy", variable=self.sroubCepy).grid(row=6, column=5, sticky=W)

        self.trny = IntVar()
        Checkbutton(window, text="Trny", variable=self.trny).grid(row=7, column=5, sticky=W)

        self.pruziny = IntVar()
        Checkbutton(window, text="Pružiny", variable=self.pruziny).grid(row=8, column=5, sticky=W)

        Label(window, text = "Startovací číslo").grid(row=0, column=6, sticky=W)

        self.stKrInitVal = IntVar(value=101)
        self.stKrInit = Entry(window,textvariable=self.stKrInitVal, width=5)
        self.stKrInit.grid(row=1, column=6)

        self.chytakyInitVal = IntVar()
        self.chytakyInit = Entry(window,textvariable=self.chytakyInitVal, width=5)
        self.chytakyInit.grid(row=2, column=6)

        self.vodPzdraInitVal = IntVar()
        self.vodPzdraInit = Entry(window,textvariable=self.vodPzdraInitVal, width=5)
        self.vodPzdraInit.grid(row=3, column=6)

        self.navKrInitVal = IntVar()
        self.navKrInit = Entry(window,textvariable=self.navKrInitVal, width=5)
        self.navKrInit.grid(row=4, column=6)

        self.drzChytInitVal = IntVar()
        self.drzChytInit = Entry(window,textvariable=self.drzChytInitVal, width=5)
        self.drzChytInit.grid(row=5, column=6)

        self.sroubCepyInitVal = IntVar()
        self.sroubCepyInit = Entry(window,textvariable=self.sroubCepyInitVal, width=5)
        self.sroubCepyInit.grid(row=6, column=6)

        self.trnyInitVal = IntVar()
        self.trnyInit = Entry(window,textvariable=self.trnyInitVal, width=5)
        self.trnyInit.grid(row=7, column=6)

        self.pruzinyInitVal = IntVar()
        self.pruzinyInit = Entry(window,textvariable=self.pruzinyInitVal, width=5)
        self.pruzinyInit.grid(row=8, column=6)

        # Cesta projektu
        projectPath = Label(window, text = "Cesta projektu:")
        projectPath.grid(row=21, column=0, sticky=W)

        self.projPath_value = StringVar()
        self.projPath = Entry(window,textvariable=self.projPath_value, width=40)
        self.projPath.grid(row=21, column=1, columnspan=3)
        
        b4=Button(window, text="Vytvor", width = 5, command=self.createDir)
        b4.grid(row=21, column=4)

        # Oznacenie naradia
        oznNar = Label(window, text = "Oznacenie naradia:")
        oznNar.grid(row=22, column=0, sticky=W)

        self.oznNar_value = StringVar()
        self.oznNar = Entry(window,textvariable=self.oznNar_value, width=40)
        self.oznNar.grid(row=22, column=1, columnspan=3)

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
        return(f"NA-{self.d_nad}-{self.h_nad}-{self.tlak}-{self.tvar_ramena}-{self.poc_cislo}")

    def set_numbering(self):
        self.oznNar.delete(0,END)
        self.oznNar.insert(END,self.get_numbering())

window=Tk()
Window(window)
window.mainloop()