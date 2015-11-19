from prettytable import PrettyTable

def printTablaHuffman(tabla):
    tablaBonita = PrettyTable(["simbolo", "peso", "codigo"])
    for fila in tabla:
        tablaBonita.add_row(fila)
    tablaBonita.sort_key("peso")
    print(tablaBonita)
