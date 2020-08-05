import os

import design_file_2 as des
from inicializacia_projektu import vytvor_oznacenie as ozn
from inicializacia_projektu import vytvor_strom_projektu as strom
from main import dutinka, nadobka, rameno


def sekvence_dc(d_ram, d_kom, t_kom, t_lak, n):
    d_avg = d_ram - (d_kom + 2*t_kom + 2*t_lak)
    red_avg = d_avg / n 

    sekv_Dc = []
    
    for i in range(1, n+1):
        Dc = round(d_ram - (i * red_avg),2)
        sekv_Dc.append(Dc)

    return sekv_Dc

def sekvence_ds(rozmery_dc):

    sekv_Ds = []
    
    for i in (rozmery_dc):
        Ds = round(i + 0.15, 2)
        sekv_Ds.append(Ds)

    return (sekv_Ds)

def sekvencia_kruzkov(rozmery_Dc, rozmery_Ds, pocet_tahov):
    
    cisla_tahu = []
            
    for i in range(1, pocet_tahov+1):
        cisla_tahu.append(i)

    oznacenie = ozn(str(int(nadobka.d_nad)), str(int(nadobka.tlak)),rameno.tvar_ram, 19, str(int(nadobka.h_nad)))
    stah_krouzek = list(zip(cisla_tahu, oznacenie, rozmery_Ds, rozmery_Dc))
    return(stah_krouzek)


d_c = sekvence_dc(40.23, 25.4, 0.37, 0.04, 19)
d_s = sekvence_ds(d_c)
kruzky = sekvencia_kruzkov(d_c, d_s, 19)

des.vytvor_data("C:\\Python\\Test\\navrh_naradi.xlsx", kruzky, 19)
print(d_c)
