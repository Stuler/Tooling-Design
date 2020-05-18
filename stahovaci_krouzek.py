from nadobka import Nadobka as Nad
from nadobka import Dutinka as Dut
from nadobka import Rameno as Ram

class Stah_krouzek:
    def __init__(self, Dc, Ds):
        self.Ds = float(Ds)
        self.Dc = self.Ds + 0.15

crown_nad = Nad(45, 136, 0.37, 0.03, 0.04)
crown_dut = Dut(45, 0.24, 150)
crown_ram = Ram(39.3,0.24, 43, 19)

print(str(crown_nad))