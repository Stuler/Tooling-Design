from nadobka import Nadobka as Nad
from nadobka import Dutinka as Dut
from nadobka import Rameno as Ram

class Stah_krouzek(Nad, Ram):

    #def __init__(self, d_ram, t_ram, d_kom, t_kom, t_vnut_lak, t_vonk_lak, n, Dc, Ds):
    #    super().__init__(d_ram, t_ram, d_kom, t_kom, t_vnut_lak, t_vonk_lak, n)
    #    self.d_ram = d_ram
    #    self.t_ram = t_ram
    #    self.d_kom = d_kom
    #    self.t_kom = t_kom
    #    self.t_vnut_lak = t_vnut_lak
    #    self.t_vonk_lak = t_vonk_lak
    #    self.n = n
                                
    def sekvencia_kruzkov(self, d_ram, d_kom, t_kom, t_lak, n):
    
        d_avg = d_ram - (d_kom + 2*t_kom + 2*t_lak)
        red_avg = d_avg / n 

        cisla_tahu = []
        sekv_Dc = []
        sekv_Ds = []
            
        for i in range(1, n+1):
            cisla_tahu.append(i)

        for i in range(1, n+1):
            Dc = round(d_ram - (i * red_avg),2)
            sekv_Dc.append(Dc)

        for i in (sekv_Dc):
            Ds = round(i + 0.15, 2)
            sekv_Ds.append(Ds)

        stah_krouzek = list(zip(cisla_tahu, sekv_Ds, sekv_Dc))
        return(stah_krouzek)

    def dc_kruzku(self, sekv, c_tahu):
        dc_kr_tah = sekv[c_tahu-1][2]
        return dc_kr_tah

    def ds_kruzku(self, sekv, c_tahu):
        ds_kr_tah = sekv[c_tahu-1][1]
        return ds_kr_tah

crown_nad = Nad("Crown", 45, 136, 12, 0.37, 0.03, 0.04, 25.4)
crown_dut = Dut(45, 0.24, 150)
crown_ram = Ram(39.3,0.24, 43, 19)

kruzok = Stah_krouzek(crown_nad, crown_ram)
kruzok.sekvencia_kruzkov()