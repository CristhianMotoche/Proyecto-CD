from prettytable import PrettyTable

def printTablaHuffman(tabla):
    tablaBonita = PrettyTable(["simbolo", "peso", "codigo"])
    for fila in tabla:
        if fila[0] == ' ':
            tablaBonita.add_row(["espacio", fila[1], fila[2]])
        elif fila[0] == '\n':
            tablaBonita.add_row(["salto", fila[1], fila[2]])
        else:
            tablaBonita.add_row(fila)
    tablaBonita.align["codigo"] = 'r'
    tablaBonita.sortby = "peso"
    tablaBonita.reversesort = True
    print(tablaBonita)
