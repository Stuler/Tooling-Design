from nadobka import Nadobka as nad
from nadobka import Dutinka as dut
from nadobka import Rameno as ram
from inicializacia_projektu import vytvor_strom_projektu as strom
from inicializacia_projektu import vygeneruj_oznacenie as gen

# Uzivatel zada cestu ku korenovemu adresaru projektu aj s nazvom projektu
# Napr C:\VAULTPRO_MCTEST\DWI\45\Crown
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

# Inicializacia nadobky, dutinky a ramena
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
    input("Tvar ramena: "),
    input("Pocet tahov: "),
        )

strom(seznam_naradi)