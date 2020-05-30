import os
import design_file as des
import stah_krouzek_koncept as kr

def sekvencia_chytakov(dc_kr):

    sekv_D = []
    sekv_d = []

    for i in (dc_kr):
        D_ch =  round(i - 0.6, 2)
        d_ch = round(D_ch - 5.5, 2)
        sekv_D.append(D_ch)
        sekv_d.append(d_ch)

    chytaky = list(zip(sekv_D, sekv_d))
    return(chytaky)

rozmery_dc = kr.sekvence_dc(40.23, 25.4, 0.37, 0.04, 19)
rozmery_chytaku = sekvencia_chytakov(rozmery_dc)
print(rozmery_chytaku)