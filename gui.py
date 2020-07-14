from tkinter import *

window=Tk()
window.title("Návrh nářadí")

# Dutinka
dut1 = Label(window, text = "Dutinka")
dut1.grid(row=0, column=0)

dut2 = Label(window, text = "Průměr dutinky")
dut2.grid(row=1, column=1)

dut3 = Label(window, text = "Tloušťka dutinky")
dut3.grid(row=2, column=1)

dut4 = Label(window, text = "Výška dutinky")
dut4.grid(row=3, column=1)

prum_dut_value = StringVar
prum_dut = Entry(window,textvariable=prum_dut_value, width=5)
prum_dut.grid(row=1, column=2)

tl_dut_value = StringVar
tl_dut = Entry(window,textvariable=prum_dut_value, width=5)
tl_dut.grid(row=2, column=2)

vys_dut_value = StringVar
vys_dut = Entry(window,textvariable=prum_dut_value, width=5)
vys_dut.grid(row=3, column=2)

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

prum_nad_value = StringVar
prum_nad = Entry(window,textvariable=prum_nad_value, width=5)
prum_nad.grid(row=5, column=2)

vys_nad_value = StringVar
vys_nad = Entry(window,textvariable=vys_nad_value, width=5)
vys_nad.grid(row=6, column=2)

tl_kom_value = StringVar
tl_kom = Entry(window,textvariable=tl_kom_value, width=5)
tl_kom.grid(row=7, column=2)

tl_lak_vnit_value = StringVar
tl_lak_vnit = Entry(window,textvariable=tl_lak_vnit_value, width=5)
tl_lak_vnit.grid(row=8, column=2)

tl_lak_ven_value = StringVar
tl_lak_ven = Entry(window,textvariable=tl_lak_ven_value, width=5)
tl_lak_ven.grid(row=9, column=2)

prum_kom_value = StringVar
prum_kom = Entry(window,textvariable=prum_kom_value, width=5)
prum_kom.grid(row=10, column=2)

tlak_value = StringVar
tlak = Entry(window,textvariable=tlak_value, width=5)
tlak.grid(row=11, column=2)

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
ram4.grid(row=16, column=1)

prum_ram_value = StringVar
prum_ram = Entry(window,textvariable=prum_ram_value, width=5)
prum_ram.grid(row=14, column=2)

tl_ram_value = StringVar
tl_ram = Entry(window,textvariable=tl_ram_value, width=5)
tl_ram.grid(row=15, column=2)

uh_ram_value = StringVar
uh_ram = Entry(window,textvariable=uh_ram_value, width=5)
uh_ram.grid(row=16, column=2)

jedn11 = Label(window, text = "mm")
jedn11.grid(row=14, column=3)

jedn12 = Label(window, text = "mm")
jedn12.grid(row=15, column=3)

jedn13 = Label(window, text = "°")
jedn13.grid(row=16, column=3)

# Tlacitka
b1=Button(window, text="OK", width = 10)
b1.grid(row=18, column=0)

b2=Button(window, text="Reset", width = 10)
b2.grid(row=18, column=1)

b3=Button(window, text="Konec", width = 10)
b3.grid(row=18, column=2)

window.mainloop()