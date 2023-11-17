Algoritmo DFD
	Definir a, b, n, x, suma como entero
	a = 1
	b= 1000000
	
	Para i <- a Hasta b Hacer
		n = i
		suma = 0
		Mientras n > 0 Hacer
			x = n mod 10
			suma = suma + x
			n = trunc(n / 10)
		FinMientras
		Si suma mod 3 = 0 y i mod 2 = 0
			Mostrar "El numero ", i," es par y divisble por 3"
		FinSi
	Fin Para

	
FinAlgoritmo
