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

stah_kruzky = vytvor_oznacenie("45", "12", "FTP", 21)
print(stah_kruzky)

#stah_kruzky_2 = vytvor_oznacenie(21)
#print(stah_kruzky_2)