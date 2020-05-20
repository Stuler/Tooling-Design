# Modul vytvori navrhovy excel
# Funkcie modulu sluzia na vytvorenie tabuliek s rozmermi jednotlivych naradi
# a na vytvorenie tabuliek pre parametricke modelovanie sucasti

import stah_krouzek_koncept
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

# Vytvori navrhovy subor MS Excel
def vytvor_xls(cesta, data, pocet_tahov):
    wb = Workbook()
    dest = cesta + "\\navrh_naradi.xlsx"
    ws = wb.active
    ws.title = "Naradi"
    
    for row in range(1, pocet_tahov):
        ws.append(range(data))

    wb.save(dest)
