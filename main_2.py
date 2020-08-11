from nadobka import Nadobka as nad
from nadobka import Dutinka as dut
from nadobka import Rameno as ram

# Uzivatel zada cestu ku korenovemu adresaru projektu aj s nazvom projektu
# Napr C:\VAULTPRO_MCTEST\DWI\45\Crown
seznam_slozek = [
    "Sablony naradi",
    "Stahovaci krouzky", 
    "Chytaky", 
    "Vodici pouzdra", 
    "Navadeci krouzky", 
    "Drzaky chytaku",
    "Sroubove cepy",
    "Trny",
    "Pruziny",
    "Navrhove soubory",
    ]

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

# Inicializacia nadobky, dutinky a ramena
nadobka = nad(
    input("Nazov projektu: "),
    float((input("Priemer nadobky: "))),
    float(input("Vyska nadobky: ")),
    int(input("Tlaková špecifikácia: ")),
    float(input("Hrubka steny kominku: ")),
        )

dutinka = dut(
    float(input("Prumer dutinky: ")),
    float(input("Tloustka steny dutinky: ")),
    int(input("Vyska dutinky: ")),
        )

rameno = ram(
    float(input("Priemer nadobky vo vyske ramena: ")),
    float(input("Tloustka steny vo vyske ramena: ")),
    float(input("Uhol ramena: ")),
    input("Tvar ramena: "),
    int(input("Pocet tahov: ")),
        )

#strom(seznam_slozek)