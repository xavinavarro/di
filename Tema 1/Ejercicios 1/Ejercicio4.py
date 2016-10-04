#!/usr/bin/env python
#Supongamos s es una cadena de caracteres en minúscula.
#Escribir un programa que cuenta el número de vocales que figuran en la cadena s. vocales
#válidos son: "a", "e", "i", "o" y "u". Por ejemplo, si s = 'azcbobobegghakl', su programa debe
#imprimir:
#Número de vocales: 5

cadena = input ()
print ("Número de vocales: ")
print (cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u"))