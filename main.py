from nadobka import Nadobka as nad
from nadobka import Dutinka as dut
from os import makedirs

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

# Inicializacia nadobky
nadobka = nad(
    input("Nazov projektu: "),
    input("Priemer nadobky: "),
    input("Vyska nadobky: "),
    input("Hrubka steny kominku: "),
    input("Hrubka vrstvy vnut. laku: "),
    input("Hrubka vrstvy vonk. laku: ")
        )