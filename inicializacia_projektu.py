from os import makedirs
    
# Vytvori podadresare projektu
def vytvor_strom_projektu(seznam):
    cesta = input('Zadaj cestu projektu: ')
    for i in seznam:
        makedirs(cesta + "\\" + i)

# Vygeneruje system oznacenia podla pouzivatela
def vytvor_oznacenie(d_nad, tlak, tvar_ramena, poc_tahov, h_nad = "h"):
    stat_nazov = []
    cisla_nar = []
    ozn_nar = []
        
    while True:  
        prompt = input("Zadaj moznost:\n"
                "1 - Vygenerovat oznacenie zo zadanych parametrov\n"
                "2 - Vytvorit oznacenie podla uzivatela\n")
        
        if prompt == "1":
                stat_ozn = ("NA-" + d_nad + "-" + h_nad + "-" + tlak + "-" + tvar_ramena)
        elif prompt == "2":
            stat_ozn = input("Zadaj staticku cast oznacenia naradia: ")
        else:
            print("\nNeplatna moznost! Skus znova!")
            continue
        
        poc_cislo = input("Uved cislo prveho stahovacieho kruzku: ")
        for i in range(poc_tahov):
            stat_nazov.append(stat_ozn)
            cisl_ozn = int(poc_cislo) + i
            cisla_nar.append(str(cisl_ozn))
            ozn_nar.append(stat_nazov[i] + "-" + str(cisla_nar[i]))
            
        return ozn_nar

def rozsah_oznacenia(naradie, poc_cislo, poc_tahov):
    prve_cisla = [poc_cislo]
    for i in naradie:
        if poc_tahov % 10 == 0:
            dalsie_cislo = int(((prve_cisla[-1]) + (poc_tahov - 1)) + 1)
        else:
            dalsie_cislo = int(((prve_cisla[-1]) + (poc_tahov - 1) ) / 10) * 10 + 11
        prve_cisla.append(dalsie_cislo)
    
    return(prve_cisla)

  
seznam_naradi = [
    "Stahovaci krouzky", 
    "Chytaky", 
    "Vodici pouzdra", 
    "Navadeci krouzky", 
    "Drzaky chytaku",
    "Sroubove cepy",
    "Trny",
    "Pruziny",
    ]

pocet_tahov = 9
start_cislo = 101

stah_kruzky = vytvor_oznacenie("45", "12", "FTP", pocet_tahov)
print(stah_kruzky)

rozsahy = rozsah_oznacenia(seznam_naradi, start_cislo, pocet_tahov)
print(rozsahy)