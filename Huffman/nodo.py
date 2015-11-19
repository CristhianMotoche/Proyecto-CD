class Nodo(object):
    izq      = None
    der      = None
    elemento = None
    peso     = 0

    def __init__(self, elemento, peso):
        self.elemento = elemento
        self.peso = peso

    def setHijos(self, hijoIzq, hijoDer):
        self.izq = hijoIzq
        self.der = hijoDer

    def __repr__(self):
        return "%s - %s " % (self.elemento, self.peso)

    def __lt__(self, nodo):
        return self.peso < nodo.peso
