

def statusRuleta(ruleta):
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


"""def ruleta():
    
    status = statusRuleta(ruleta)"""

ruleta = [0] * 37
statusRuleta(ruleta)
active = True
while active:
    validaAccion= True
    while validaAccion:
        accion = int(input("Si desea ver los numeros que NO han salido sorteados presione 1\nSi desea actuializar un numero en la ruleta presione 2\nSi desea obtener el porcentaje de sorteo de un numero presione 3: "))
        print("================================")
        if accion == 1 or accion == 2 or accion == 3:
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






