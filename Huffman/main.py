#!/usr/bin/python3

from huffman import *
from tabla import printTablaHuffman
from concurrent.futures import ThreadPoolExecutor
import multiprocessing as mp
import datetime

def contarParaleloAparicionesDeTexto(textoInput, q):
    tabla = {}
    for caracter in textoInput:
        if caracter not in tabla:
            tabla[caracter] = 0
    for caracter in textoInput:
        tabla[caracter] += 1
    q.put(tabla)

def main():
    # INPUT
    #n = int(input("Ingrese el número de líneas que va a escribir: \n>>"))
    #textoLeido = leerNLineas(n)
    archivo = open('text.txt', 'r')
    textoLeido = archivo.read()
    threads = int(input("Ingrese el número de threads que desea \n>>>"))

    # CONTAR PESOS
    output = mp.Queue()
    n = len(textoLeido)
    x = []
    ini = 0
    fin = n//threads
    for _ in range(1, threads):
        x.append(textoLeido[ini:fin])
        ini = fin
        fin += n//threads
    x.append(textoLeido[ini:])

    init = datetime.datetime.now()

    ts = []
    for t in range(threads):
        ts.append(mp.Process(target=contarParaleloAparicionesDeTexto, args=(x[t],output)))

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    tabla = {}
    tablas = [output.get() for t in ts ]
    for tab in tablas:
        for key in tab:
            if key not in tabla:
                tabla[key] = 0
        for key in tab:
            tabla[key] += tab[key]

    # GENERAR ARBOL
    cola = encolarNodos(tabla)
    cola = generarArbol(cola)
    arbol = cola.pop()

    # GENERAR CODIGO HUFFMAN
    huffman = Huffman()
    huffman.generarCodigo('', arbol)
    codigoHuffman = huffman.getCodigo()

    # OUTPUT
    tablaResultado = []
    for key in sorted(codigoHuffman, key=codigoHuffman.get):
        tablaResultado.append([key, tabla[key], codigoHuffman[key]])
    printTablaHuffman(tablaResultado)

    print("Tiempo: ")
    print(str(datetime.datetime.now() - init) + " [s]")

    # Probar propiedad de codificación
    # Mensaje = DECODIFICAR(CODIFICAR(Mensaje))
    # Descomente esta línea para ver el mensaje original
    # print(huffman.decodificar(huffman.codificar(textoLeido)))

if __name__=="__main__":
    main()


