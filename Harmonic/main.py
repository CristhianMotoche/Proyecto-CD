#!/usr/bin/python3
from harmonic import *


def main():
    harmonic = Harmonic()
    d = int(input("Ingrese D (1 <= D <= 10^5): \n>>"))
    n = int(input("Ingrese N (1 <= N <= 10^8): \n>>"))

    print(harmonic.sum(d,n))

if __name__=="__main__":
    main()

