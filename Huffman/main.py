#!/usr/bin/python3

from utilidades import *

def main():
    # n = int(input("Ingrese el número de líneas que va a escribir: \n>>"))
    #textoLeido = leerNLineas(n)

    archivo = open('text.txt', 'r')
    textoLeido = archivo.read()

    codigoHuffman = huffman(textoLeido)
    for key in codigoHuffman:
        print( key, codigoHuffman[key][0], codigoHuffman[key][1] )

def huffman(texto):
    tabla = contarAparicionesDeTexto(texto)
    cola = encolarNodos(tabla)
    cola = agruparNodos(cola)
    return codificar({}, "", cola.pop())

if __name__=="__main__":
    main()
