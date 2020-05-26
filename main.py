from nadobka import Nadobka as nad
from nadobka import Dutinka as dut
from nadobka import Rameno as ram
from os import makedirs

# Uzivatel zada cestu ku korenovemu adresaru projektu aj s nazvom projektu
# Napr C:\VAULTPRO_MCTEST\DWI\45\Crown
# Vytvori podadresare projektu
def vytvor_strom_projektu(seznam):
    cesta = input('Zadaj cestu projektu: ')
    for i in seznam:
        makedirs(cesta + "\\" + i)

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

vytvor_strom_projektu(seznam_naradi)

# Inicializacia nadobky
nadobka = nad(
    input("Nazov projektu: "),
    input("Priemer nadobky: "),
    input("Vyska nadobky: "),
    input("Tlaková špecifikácia: "),
    input("Hrubka steny kominku: "),
        )

dutinka = dut(
    input("Priemer dutinky: "),
    input("Tloustka steny dutinky: "),
    input("Vyska dutinky: "),
        )

rameno = ram(
    input("Priemer nadobky vo vyske ramena: "),
    input("Tloustka steny vo vyske ramena: "),
    input("Uhol ramena: "),
    input("Pocet tahov: ")
        )