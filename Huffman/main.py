#!/usr/bin/python3

from utilidades import *
from tabla import *

def main():
    # n = int(input("Ingrese el número de líneas que va a escribir: \n>>"))
    #textoLeido = leerNLineas(n)

    archivo = open('text.txt', 'r')
    textoLeido = archivo.read()

    codigoHuffman = huffman(textoLeido)
    tabla = []

    for key in sorted(codigoHuffman, key=codigoHuffman.get):
        tabla.append([key, codigoHuffman[key][0], codigoHuffman[key][1]])
    printTablaHuffman(tabla)

def huffman(texto):
    tabla = contarAparicionesDeTexto(texto)
    cola = encolarNodos(tabla)
    cola = agruparNodos(cola)
    return codificar({}, "", cola.pop())

if __name__=="__main__":
    main()
