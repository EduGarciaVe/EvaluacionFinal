"""El medidor de lluvia es un sistema que permite recoger información sobre los mm de agua que han caído en Santiago. 
    Una muestra tendrá N mediciones, donde cada medición corresponde a una cantidad de mm de agua caída, por lo que 
    se pide que genere un programa en Python 3 capaz de: """

"""Solicitar la cantidad de mediciones a registrar para la muestra y guardar dicho número en la variable “N”.
    Se debe asegurar que “N” siempre sea un número entero positivo (en caso de que se ingrese cero o un numero
    negativo deberá solicitar, tantas veces como sea necesario, nuevamente el valor para “N” hasta que se cumpla lo requerido)."""
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

"""Solicitar y validar cada medición ingresada de modo que estén en el intervalo de 0 a 150 (ambos inclusive). 
    La validación es medición a medición. Es decir, cada vez que se ingrese una medición no válida (fuera del intervalo señalado)
    deberá enviar un mensaje que diga “Error, ingrese una medida en el intervalo de 0 a 150” y, luego, dar oportunidad de corregir dicha medida.
    Esto deberá ser realizado tantas veces como sea necesario. """

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

"""Una vez ingresadas las N mediciones válidas el programa imprimirá el mensaje: “El promedio de agua caída es:
    <AGUA>” donde <AGUA> representa el valor del promedio simple de todas las mediciones válidas que fueron ingresadas."""

def resultado(agua):
    print(f"El promedio de agua caida es: {agua}")

def main():
    n = ingresoCantidad()
    mediciones = ingresoMediciones(n)
    agua = calcularPromedio(mediciones,n)
    resultado(agua)



main()
    