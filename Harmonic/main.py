
#!/usr/bin/python3
from harmonic import *
from utilidades import *
import multiprocessing as mp
import threading
import datetime
import math

def colectarDigitos(d, n, m, q):
    harmonic = Harmonic()
    q.put(harmonic.sum(d, n, m))

def main():
    output = mp.Queue()
    allDigits = []
    limits = []

    d = int(input("Ingrese D (1 <= D <= 10^5): \n>>"))
    n = int(input("Ingrese N (1 <= N <= 10^8): \n>>"))
    threads = int(input("Ingrese numero de threads: \n>>"))

    ini = datetime.datetime.now()
    i = 0
    while i != threads:
        max = i*n//threads + 1
        min = (i+1)*n//threads
        limits.append((max,min))
        i+=1

    print(limits)

    ts = []
    for t in range(len(limits)):
        ts.append(mp.Process(target=colectarDigitos, args=(d,limits[t][1],limits[t][0], output)))

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    allDigits = [output.get() for t in ts]
    suma = sumarDigitos(allDigits)
    suma.reverse()
    print(convertir(suma))

    print("Tiempo: ")
    print(str(datetime.datetime.now() - ini) + " [s]")

if __name__=="__main__":
    main()
