from tkinter import *
from nadobka import Nadobka as nad
from nadobka import Dutinka as dut
from nadobka import Rameno as ram

class Window():
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Návrh nářadí")

        # Dutinka
        dut1 = Label(window, text = "Dutinka")
        dut1.grid(row=0, column=0)

        dut2 = Label(window, text = "Průměr dutinky")
        dut2.grid(row=1, column=1)

        dut3 = Label(window, text = "Tloušťka dutinky")
        dut3.grid(row=2, column=1)

        dut4 = Label(window, text = "Výška dutinky")
        dut4.grid(row=3, column=1)

        self.prumDut_value = DoubleVar()
        self.prumDut = Entry(window,textvariable=self.prumDut_value, width=5)
        self.prumDut.grid(row=1, column=2)

        self.tlDut_value = DoubleVar()
        self.tlDut = Entry(window,textvariable=self.tlDut_value, width=5)
        self.tlDut.grid(row=2, column=2)

        self.vysDut_value = IntVar()
        self.vysDut = Entry(window,textvariable=self.vysDut_value, width=5)
        self.vysDut.grid(row=3, column=2)

        jedn1 = Label(window, text = "mm")
        jedn1.grid(row=1, column=3)

        jedn2 = Label(window, text = "mm")
        jedn2.grid(row=2, column=3)

        jedn3 = Label(window, text = "mm")
        jedn3.grid(row=3, column=3)

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
        ram4.grid(row=19, column=1)

        ram5 = Label(window, text = "Počet tahu")
        ram5.grid(row=17, column=1)

        ram6 = Label(window, text = "Vule chytáku")
        ram6.grid(row=18, column=1)

        self.prumRam_value = DoubleVar()
        self.prumRam = Entry(window,textvariable=self.prumRam_value, width=5)
        self.prumRam.grid(row=14, column=2)

        self.tlRam_value = DoubleVar()
        self.tlRam = Entry(window,textvariable=self.tlRam_value, width=5)
        self.tlRam.grid(row=15, column=2)

        self.uhRam_value = DoubleVar()
        self.uhRam = Entry(window,textvariable=self.uhRam_value, width=5)
        self.uhRam.grid(row=19, column=2)

        self.pocTah_value = IntVar()
        self.pocTah = Entry(window,textvariable=self.pocTah_value, width=5)
        self.pocTah.grid(row=17, column=2)

        self.vuleChyt_value = DoubleVar()
        self.vuleChyt = Entry(window,textvariable=self.vuleChyt_value, width=5)
        self.vuleChyt.grid(row=18, column=2)

        jedn11 = Label(window, text = "mm")
        jedn11.grid(row=14, column=3)

        jedn12 = Label(window, text = "mm")
        jedn12.grid(row=15, column=3)

        jedn13 = Label(window, text = "°")
        jedn13.grid(row=19, column=3)

        jedn14 = Label(window, text = "-")
        jedn14.grid(row=17, column=3)

        jedn15 = Label(window, text = "mm")
        jedn15.grid(row=18, column=3)

        # Tlacitka
        b1=Button(window, text="OK",  width = 10)
        b1.grid(row=20, column=0)

        b2=Button(window, text="Reset", width = 10)
        b2.grid(row=20, column=1)

        b3=Button(window, text="Konec", width = 10, command=self.window.destroy)
        b3.grid(row=20, column=2)

window=Tk()
Window(window)
window.mainloop()