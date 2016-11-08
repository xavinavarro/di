'''
Escriba un programa que pida un número y a continuación escriba la lista de todos los divisores
del número (incluidos el uno y él mismo).
'''

#!/usr/bin/env python

numero = int (input("Numero: "))
lista = []

i = 1 
x = 0 
while (i <= numero):
	if (numero % i == 0):
		lista[0:x] += [str(i)]
		x += 1
		i += 1 
	else:
		i += 1 

print ("Divisores: ", lista)