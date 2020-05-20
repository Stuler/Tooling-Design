from nadobka import Nadobka as Nad
from nadobka import Dutinka as Dut
from nadobka import Rameno as Ram

class Stah_krouzek(Nad, Ram):
    def __init__(self, d_ram, t_ram, d_kom, t_kom, t_vnut_lak, t_vonk_lak, n, Dc, Ds):
        super().__init__(d_ram, t_ram, d_kom, t_kom, t_vnut_lak, t_vonk_lak, n)
        stredny_prumer = ((d_kom + t_kom + t_vnut_lak + t_vonk_lak) + (d_ram + t_vnut_lak + t_vonk_lak)) / 2
        celk_red = (d_ram + t_vnut_lak + t_vonk_lak) - (d_kom + t_kom + t_vnut_lak + t_vonk_lak)
        red_na_tah = celk_red / n
        Dc_1 = d_ram - red_na_tah

    def sekvence_krouzku(self, krouzky):
        self.krouzky = {}
        for i in range(n):
            pass

        
         

crown_nad = Nad(45, 136, 0.37, 0.03, 0.04)
crown_dut = Dut(45, 0.24, 150)
crown_ram = Ram(39.3,0.24, 43, 19)

print(str(crown_nad))