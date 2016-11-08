'''
Escriba un programa que calcule términos de una sucesión del tipo Un+1 = a Un + b. El programa
tiene que pedir el valor de a, de b y del término U0 y el número de términos a calcular.
'''

#!/usr/bin/env python

a = int (input("Valor de a: "))
b = int (input("Valor de b: "))
u = int (input("Valor de U(0): "))
cantidad = int (input("Numeros a mostar: "))
lista = []

sucesion = u
lista.append(sucesion)
z = 1 
x = 1
while(x < cantidad):
	sucesion = a * sucesion + b
	lista[0:z] += [str(sucesion)]
	z += 1
	x += 1

print ("Sucesión: ", lista)