def sumarDigitos(allDigits):
    sumaDigits = []
    suma = 0
    resto = 0
    for i in range(len(allDigits[0])):
        suma = 0
        for j in range(len(allDigits)):
            suma += allDigits[j][-(i+1)] + resto
            if suma > 10:
                resto = suma//10
                suma = suma - 10
            else:
                resto = 0
        sumaDigits.append(suma)
    return sumaDigits

def convertir(sumaDigits):
    sumaDigits.insert(1, '.')
    sumaDigits = map(str, sumaDigits)
    return "".join(sumaDigits)[:-11]
