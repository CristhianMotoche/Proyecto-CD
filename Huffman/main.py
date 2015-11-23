#!/usr/bin/python3

from huffman import *
from tabla import *
from concurrent.futures import ThreadPoolExecutor
import threading

def contarParaleloAparicionesDeTexto(textoInput):
    global tabla

    for caracter in textoInput:
        if caracter not in tabla:
            tabla[caracter] = 0
    for caracter in textoInput:
        tabla[caracter] += 1

def main():
    # INPUT
    #n = int(input("Ingrese el número de líneas que va a escribir: \n>>"))
    #textoLeido = leerNLineas(n)
    archivo = open('text.txt', 'r')
    textoLeido = archivo.read()

    # CONTAR PESOS
    global tabla
    tabla = {}
    n = len(textoLeido)//2
    x = [textoLeido[:n], textoLeido[n:]]

    t = ThreadPoolExecutor(max_workers=2)
    t.map(contarParaleloAparicionesDeTexto, x)
    t.shutdown()

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

    print(huffman.decodificar(huffman.codificar(textoLeido)))

if __name__=="__main__":
    main()


