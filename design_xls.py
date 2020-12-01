import xlwings as xw 

wb = xw.Book()
wb.save("Navrh_naradi.xlsx")

dataSheet = wb.sheets[0]

dataSheet.range("B2").options(transpose=True).value = ["Stěna dutinky", 
                                                        "Stěna ramena", 
                                                        "Stěna komínku"]

dataSheet.range("C2").options(transpose=True).value = ["t_DUT", 
                                                        "t_RAM", 
                                                        "t_KOM"]

dataSheet.range("D2").options(transpose=True).value = ["t_DUT", 
                                                        "t_RAM", 
                                                        "t_KOM"]




