from os import makedirs
#from design_file import vytvor_xls
from nadobka import Nadobka
    
seznam_naradi = [
    "Sablony naradi"
    "Stahovaci krouzky", 
    "Chytaky", 
    "Vodici pouzdra", 
    "Navadeci krouzky", 
    "Drzaky chytaku",
    "Sroubove cepy",
    "Trny",
    "Pruziny",
    "Navrhove soubory",]

# Uzivatel zada cestu ku korenovemu adresaru projektu aj s nazvom projektu
# Napr C:\VAULTPRO_MCTEST\DWI\45\Crown
path = input('Zadaj cestu projektu: ')

# Vytvori podadresare projektu
for i in seznam_naradi:
    makedirs(path + "\\" + i)

# Vytvori nadobku
crown = Nadobka(45, 156, 0.37)

# Vytvori navrhovy excel
#vytvor_xls(path, 19)

