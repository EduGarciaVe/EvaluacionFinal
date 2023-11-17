
def ingresoCantidad():
    n=0
    validaCantidadMediciones = False
    while validaCantidadMediciones == False:
        n = int(input("Ingrese la cantidad de mediciones "))
        if n > 0:
            validaCantidadMediciones = True
        else:
            print("Error, ingrese un numero sobre cero")
    return n

def ingresoMediciones(n):
    mediciones = []
    for m in range (0,n):
        validaMediciones = False
        while validaMediciones == False:
            medicion = int(input(f"Ingrese medicion {m+1}: "))
            if medicion >= 0 and medicion <= 150:
                mediciones.append(medicion)
                validaMediciones = True
            else:
                print ("Error, ingrese una medida en el intervalo de 0 a 150")
    return mediciones


def calcularPromedio(mediciones, n):
    agua = sum(mediciones) / n
    return agua

def resultado(agua):
    print(f"El promedio de agua caida es: {agua}")

def main():
    n = ingresoCantidad()
    mediciones = ingresoMediciones(n)
    agua = calcularPromedio(mediciones,n)
    resultado(agua)



main()
    