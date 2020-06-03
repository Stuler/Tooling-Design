from os import makedirs
    
# Vytvori podadresare projektu
def vytvor_strom_projektu(seznam):
    cesta = input('Zadaj cestu projektu: ')
    for i in seznam:
        makedirs(cesta + "\\" + i)

# Vygeneruje system oznacenia podla specifikacii
def vygeneruj_oznacenie(d_nad, tlak, tvar_ramena, poc_tahov, poc_cislo, h_nad = "h"):
    stat_nazov = []
    cisla_nar = []
    ozn_nar = []

    for i in range(poc_tahov):
        stat_nazov.append("NA-" + d_nad + "-" + h_nad + "-" + tlak + "-" + tvar_ramena + "-")
    
    for i in range(poc_tahov):
        cisl_ozn = int(poc_cislo) + i
        cisla_nar.append(str(cisl_ozn))

    for i in range(poc_tahov):
        ozn_nar.append(stat_nazov[i] + str(cisla_nar[i]))

    return ozn_nar

# Vygeneruje system oznacenia podla pouzivatela
def vytvor_oznacenie(staticka_cast):
    pass


seznam_naradi = [
    "Sablony naradi",
    "Stahovaci krouzky", 
    "Chytaky", 
    "Vodici pouzdra", 
    "Navadeci krouzky", 
    "Drzaky chytaku",
    "Sroubove cepy",
    "Trny",
    "Pruziny",
    "Navrhove soubory",]


for i in seznam_naradi:
    stah_kruzky = vygeneruj_oznacenie("45", "12", "FTP", 21, "101")
    chytaky = vygeneruj_oznacenie("45", "12", "FTP", 21, "131")
print(stah_kruzky)
print(chytaky)