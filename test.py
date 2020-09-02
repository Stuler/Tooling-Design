from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()

dest_filename = 'C:\\Python\\empty_book.xlsx'

ws1 = wb.active
ws1.title = "range names"

for row in range(1, 40):
    ws1.append(range(600))

ws2 = wb.create_sheet(title="Pi")

wb.save(filename = dest_filename)

prva_bunka = str("ws2['A4']")
cislo_bunky = str(prva_bunka[6])
bunka = [prva_bunka]
for i in range(1, 20):
    bunka_cislo = int(cislo_bunky)+i
    bunka.append("ws2['A"+str(bunka_cislo)+"']")

ws2.append(bunka)

cell_range = ws2['A3':'A23']
for cells in cell_range:
    for cell in cells:
        cell.value = 2

#for row in ws2.iter_cols(min_row=1, min_col=1, max_row = 19, max_col=1):  
#    for cell in row:  
#        ws2.append(bunka[1]) 


wb.save(filename = dest_filename)