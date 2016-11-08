'''
Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la
lista por orden alfabético.
'''

#!/usr/bin/env python

posiciones = int (input("Palabras que tiene la lista: "))
lista = []
i = 1
while (i <= posiciones):
	lista[0:i] += [str(input("Elemento: "))]
	i += 1

print ("Lista sin ordenar: ", lista)

lista.sort()
print ("Lista ordenada: ", lista)