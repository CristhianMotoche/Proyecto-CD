#!/usr/bin/python3
from harmonic import *
from utilidades import *
import threading
import math

def colectarDigitos(d, n, m):
    global allDigits
    harmonic = Harmonic()
    allDigits.append(harmonic.sum(d, n, m))

def main():
    global allDigits
    allDigits = []

    d = int(input("Ingrese D (1 <= D <= 10^5): \n>>"))
    n = int(input("Ingrese N (1 <= N <= 10^8): \n>>"))
    threads = 2

    if n%2 == 0:
        max = n//2
        min = n//2 - 1
    else:
        max = math.ceil(n/2)
        min = math.floor(n/2)

    t1 = threading.Thread(target=colectarDigitos, args=(d,n,max))
    t1.start()

    t2 = threading.Thread(target=colectarDigitos, args=(d,min,1))
    t2.start()

    t1.join()
    t2.join()

    suma = sumarDigitos(allDigits)
    suma.reverse()
    print(convertir(suma))

if __name__=="__main__":
    main()
