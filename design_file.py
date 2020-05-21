# Modul vytvori navrhovy excel
# Funkcie modulu sluzia na vytvorenie tabuliek s rozmermi jednotlivych naradi
# a na vytvorenie tabuliek pre parametricke modelovanie sucasti

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

# Vytvori navrhovy subor MS Excel
def vytvor_xls(data, pocet_tahov):
    wb = Workbook()
    dest = "C:\\Python\\navrh_naradi.xlsx"
    ws = wb.active
    ws.title = "Naradi"

    rows = [
        ["Tah", "Ds", "Dc"]
    ]
          
    for row in rows:
        ws.append(row)
    
    for i in data:
        ws.append(i)   

    wb.save(dest)