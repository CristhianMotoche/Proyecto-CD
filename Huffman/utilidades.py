from nodo import *
from cola import *


def leerNLineas(n):
    texto = ""

    for _ in range(n):
        linea = input()
        linea += '\n'
        texto += linea

    return texto

def contarAparicionesDeTexto(texto):
    diccionario = {}
    for caracter in texto:
        diccionario[caracter] = 0
    for caracter in texto:
        diccionario[caracter] += 1
    return diccionario

def encolarNodos(tabla):
    cola = Cola()
    for clave in tabla:
        cola.push(Nodo(clave, tabla[clave]))
    return cola

def generarArbol(cola):
    while len(cola.cola) > 1:
        izq = cola.pop()
        der = cola.pop()
        nodo = Nodo(None, der.peso + izq.peso)
        nodo.setHijos(izq, der)
        cola.push(nodo)
    return cola

def codificar(codigos, simbolo, nodo):
    if nodo.elemento:
        if not simbolo:
            codigos[nodo.elemento] = (nodo.peso, "0")
        else:
            codigos[nodo.elemento] = (nodo.peso, simbolo)
    else:
        codigos.update( codificar(codigos, simbolo + "0", nodo.izq) )
        codigos.update( codificar(codigos, simbolo + "1", nodo.der) )
    return codigos

def reverse(diccionario):
    nuevoDiccionario = {}
    for key in diccionario:
        nuevoDiccionario[diccionario[key]] = key
    return nuevoDiccionario
