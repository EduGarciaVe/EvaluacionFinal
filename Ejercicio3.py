def statusRuleta(ruleta, numerosEnRuleta):  
    print(numerosEnRuleta)
    print(ruleta)
    

def noHanSalido(ruleta):
    for i in range (len(ruleta)):
        if ruleta[i] == 0:
            print(f"El numero {i}, NO ha salido sorteado")
    

def actualizarRuleta (ruleta,n):
    if n >=0 and n <= 36:
        ruleta[n] += 1
        print(ruleta[n])
    else :
        print (-1)

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
