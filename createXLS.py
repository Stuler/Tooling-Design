

def create_XLS(path):
    wb = Workbook()
    dest = path
    ws1 = wb.active
    ws1.title = "Data"

    # Prvy stlpec
    ws1['B2'] = "Stena dutinky"
    ws1['B3'] = "Stena ramena"
    ws1['B4'] = "Stena kominku"

    ws1['B6'] = "Pocet tahu"
    ws1['B7'] = "Redukce"

    ws1['B9'] = "Zmena tloustky steny/tah"

    ws1.merge_cells('B11:B13')
    ws1['B11'] = "Tloustka laku"
    ws1['B14'] = "Vule chytaku"

    ws1['B17'] = "Prumer zacatku ramena"

    # Druhy stlpec
    ws1['C2'] = "tdutinka"
    ws1['C3'] = "trameno"
    ws1['C4'] = "tkominek"

    ws1['C6'] = "n"
    ws1['C7'] = "red"

    ws1['C9'] = "tdut/n"

    ws1['C11'] = "tvonklak"
    ws1['C12'] = "tvnutlak"
    ws1['C13'] = "tlakcelk"
    ws1['C14'] = "v"

    ws1['C16'] = "Dnad"
    ws1['C17'] = "Dram"

    # Treti stlpec
    ws1['D2'] = dutinka.t_dut
    ws1['D3'] = rameno.t_ram
    ws1['D4'] = nadobka.t_kom

    ws1['D6'] = rameno.n