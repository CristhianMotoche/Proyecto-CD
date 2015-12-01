
#!/usr/bin/python3
from harmonic import *
from utilidades import *
import threading
import datetime
import math

def colectarDigitos(d, n, m):
    global allDigits
    harmonic = Harmonic()
    allDigits.append(harmonic.sum(d, n, m))

def main():
    global allDigits
    allDigits = []
    limits = []

    d = int(input("Ingrese D (1 <= D <= 10^5): \n>>"))
    n = int(input("Ingrese N (1 <= N <= 10^8): \n>>"))
    threads = int(input("Ingrese numero de threads: \n>>"))

    ini = datetime.datetime.now()
    for i in range(threads):
        if i < n:
            max = i*n//threads + 1
            min = (i+1)*n//threads
            limits.append((max,min))

    ts = []
    for t in range(len(limits)):
        ts.append(threading.Thread(target=colectarDigitos, args=(d,limits[t][1],limits[t][0])))

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    suma = sumarDigitos(allDigits)
    suma.reverse()
    print(convertir(suma))

    print("Tiempo: ")
    print(str(datetime.datetime.now() - ini) + " [s]")

if __name__=="__main__":
    main()
