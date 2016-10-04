#1.Suponga que dos variables, valores varA y varB, están asignados, ya sean números o cadenas.
#Escribir una pieza de código Python que imprime uno de los siguientes mensajes:
#"Cadena involucrada", si bien varA o varB son cadenas
#"Grande" si varA es mayor que varB
#"Igual" si varA es igual a varB
#"Más pequeño" si varA es menor que varB
#Escribir el código asumiendo varA y varB ya están definidos


#!/usr/bin/env python

varA = 11
varB = 11

if type (varA) == int and type (varB) == int:
	if varA < varB:
		print ("Mas pequeño")
	elif varA == varB:
		print ("Igual")
	else:
		print ("Grande")

if type (varA) == str or type (varB) == str:
	print ("Cadena involucrada")