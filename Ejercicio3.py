
"""La antigua ruleta de casino tenía los números del 0 al 36 y a los jugadores les costaba mucho realizar cálculos 
    matemáticos para apostar con las mayores probabilidades. Suponiendo que tenemos una lista llamada “ruleta” de 
    largo 37 y que en cada “casilla” (índice) se almacena la cantidad de veces que ese número salió sorteado 
    (ej. Si en la casilla 25 hay un 12 significa que el número 25 ha salido 12 veces), se pide que escriba las siguientes funciones:"""

def statusRuleta(ruleta, numerosEnRuleta):  
    print(numerosEnRuleta)
    print(ruleta)
    
"""noHanSalido(ruleta) que recibe la lista que representa la ruleta e imprime por pantalla 
    los números que no han sido sorteados (que no han salido)."""

def noHanSalido(ruleta):
    for i in range (len(ruleta)):
        if ruleta[i] == 0:
            print(f"El numero {i}, NO ha salido sorteado")
    
"""actualizarRuleta(ruleta, N) que recibe la lista que representa la ruleta y un número entero “N” y luego suma 1 a la cantidad 
    de veces que ha sido sorteado un número “N”. Debe validar que el valor de “N” sea un número entre 0 y 36 (ambos inclusive). 
    Si el número no corresponde al rango estipulado deberá imprimir el valor –1."""
def actualizarRuleta (ruleta,n):
    if n >=0 and n <= 36:
        ruleta[n] += 1
        print(ruleta[n])
    else :
        print (-1)

"""obtenerPorcentaje(ruleta, N) que recibe la lista que representa la ruleta y un número entero “N” y retorna el 
    porcentaje (número decimal) de veces que ha sido sorteado un número “N” sobre el total de veces que se ha tirado la ruleta.
    Asuma que, en este caso, el calor de “N” siempre será número entre 0 y 36 (ambos inclusive) y, por ende, no lo necesita validar."""

def obtenerPorcentaje (ruleta, n):
    if n >=0 and n <= 36:
        sumaRuleta = sum(ruleta)
        if ruleta[n] > 0:
            porcentaje = (ruleta[n] * 100) / sumaRuleta
            print(f"El numero {n} ha sido sorteado un {porcentaje} % de veces")
        else:
            print(f"El numero {n} ha sido sorteado 0 % de veces")
    else:
        print("Numero ingresado es incorrecto")

numerosEnRuleta =  list(range(37))
ruleta = [0] * 37
statusRuleta(ruleta,numerosEnRuleta)
active = True
while active:
    validaAccion= True
    while validaAccion:
        accion = int(input("Si desea ver los numeros que NO han salido sorteados presione 1\nSi desea actualizar un numero en la ruleta presione 2\nSi desea obtener el porcentaje de sorteo de un numero presione 3\nSi desea ver el estado de la ruta presione 4: "))
        print("================================")
        if accion in [1,2,3,4]:
            validaAccion = False
        else:
            print("La opcion ingresada no es valida")
            print("================================")
    if accion == 1:
        noHanSalido(ruleta)
        print("================================")
    elif accion == 2:
        n = int(input("Ingrese el numero a actualizar: "))
        actualizarRuleta(ruleta,n)
        statusRuleta(ruleta) 
        print("================================")
    elif accion == 3:
        n = int(input("Ingrese numero para calcular porcentaje de sorteo: "))
        obtenerPorcentaje(ruleta, n)
        print("================================")
    elif accion == 4:
        statusRuleta(ruleta,numerosEnRuleta)
        print("================================")
