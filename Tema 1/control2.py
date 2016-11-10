#!/usr/bin/env python
# ejemplo de if
salir = False
while not salir:
	entrada = input()
	if entrada == "adios":
		salir = True
	else:
		print (entrada)
		