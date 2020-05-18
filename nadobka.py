class Dutinka:
    """
    Inicializuje dutinku s parametrami:
    Prumer dutinky, tloustka steny dutinky, vyska dutinky
    """
    def __init__(self, d_dut, t_dut, h_dut):
        self.d_dut = d_dut
        self.t_dut = t_dut
        self.h_dut = h_dut

class Nadobka:
    """
    Inicializuje nadobku s parametrami:
    Prumer nadobky, vyska nadobky,  
    tloustka vnitrniho laku, tloustka vnejsiho laku
    """
    def __init__(self, 
                d_nad, 
                h_nad,
                t_kom,
                t_vnut_lak = 0.02, 
                t_vonk_lak = 0.02,
                d_kom = 25.4
                ):
        self.d_nad = float(d_nad)
        self.h_nad = float(h_nad)
        self.t_kom = float(t_kom)
        self.t_vnut_lak = float(t_vnut_lak)
        self.t_vonk_lak = float(t_vonk_lak)
        self.t_lak = t_vonk_lak + t_vnut_lak

    def __str__(self):
        return (f"Prumer nadobky:  {self.d_nad}\n Vyska nadobky:  {self.h_nad}\n")

class Rameno:
    """
    Inicializuje vlastnosti ramene s parametrami:
    prumer zacatku ramene, vysledni tloustka ramene, uhel ramene
    """
    def __init__(self, d_ram, t_ram, uhol_ram, n):
        self.d_ram = d_ram
        self.t_ram = t_ram
        self.uhol_ram = uhol_ram
        self.n = n