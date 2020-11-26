import xlwings as xw 

wb = xw.Book()
wb.save("Navrh_naradi.xlsx")

dataSheet = wb.sheets[0]
designSheet = wb.sheets[1]

