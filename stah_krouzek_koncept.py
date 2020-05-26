import os
import design_file as des

def d_c(d_ram, d_kom, t_kom, t_lak, n):
    d_avg = d_ram - (d_kom + 2*t_kom + 2*t_lak)
    red_avg = d_avg / n 
    Dc = round(d_ram - (n * red_avg),2)

def d_s(dc):
    Ds = dc + 0.15


def sekvencia_kruzkov(d_ram, d_kom, t_kom, t_lak, n):
    
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

kruzky = sekvencia_kruzkov(40.23, 25.4, 0.37, 0.04, 19)
des.vytvor_xls("C:\\Python\\Test\\navrh_naradi.xlsx", kruzky, 19)