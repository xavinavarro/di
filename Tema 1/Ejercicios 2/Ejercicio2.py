#!/usr/bin/env python

def gcdIter(a, b):
	resto = 0
	while (b > 0):
		resto = b
		b = a % b
		a = resto 
	return a

a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))

print ("Maximo comun divisor entre ", a, " y ", b, " es : ", gcdIter(a, b))