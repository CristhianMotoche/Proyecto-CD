#!/usr/bin/python3

from huffman import *
from tabla import *

def main():
    # INPUT
    #n = int(input("Ingrese el número de líneas que va a escribir: \n>>"))
    #textoLeido = leerNLineas(n)
    archivo = open('text.txt', 'r')
    textoLeido = archivo.read()

    # CONTAR PESOS
    tabla = contarAparicionesDeTexto(textoLeido)

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

    # print(huffman.decodificar(huffman.codificar(textoLeido)))
if __name__=="__main__":
    main()
