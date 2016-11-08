'''
Escriba un programa que pida un número y a continuación escriba la lista de todos los números
primos hasta él..
'''

#!/usr/bin/env python

numero = int (input("Numero: "))
lista = []

y = 0 
for a in range(numero+1):
	x = 0 
	i = 1
	while (i <= a):
		if (a % i == 0):
			x += 1
			i += 1 
		else:
			i += 1 
	if (a != 0):
		if (x <= 2):
			lista[0:y] += [str(a)]
			y += 1

print ("Primos 0 hasta el numero ", numero, ":",lista)