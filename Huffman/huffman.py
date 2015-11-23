from nodo import *
from cola import *
from utilidades import *

class Huffman(object):
    codigo = {}

    def __init__(self):
        super(Huffman, self).__init__()

    def generarCodigo(self, simbolo, nodo):
        if nodo.elemento:
            if not simbolo:
                self.codigo[nodo.elemento] = "0"
            else:
                self.codigo[nodo.elemento] = simbolo
        else:
            self.generarCodigo(simbolo + "0", nodo.izq)
            self.generarCodigo(simbolo + "1", nodo.der)

    def codificar(self, textoPlano):
        textoCodificado = ""
        acumulador = ""
        for caracter in textoPlano:
            if caracter in self.codigo:
                textoCodificado += self.codigo[caracter]
        return textoCodificado

    def decodificar(self, textoCodificado):
        codigoDecodificacion = reverse(self.codigo)
        textoPlano = ""
        acumulador = ""
        for caracter in textoCodificado:
            acumulador += caracter
            if acumulador in codigoDecodificacion:
                textoPlano += codigoDecodificacion[acumulador]
                acumulador = ""
        return textoPlano

    def getCodigo(self):
        return self.codigo
