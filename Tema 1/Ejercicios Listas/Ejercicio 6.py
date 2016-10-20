#Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una
#segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de
#crear una lista distinta).


#!/usr/bin/env python


numero = int(input("Dime cuantas palabras tiene la lista: "))

if numero < 1:
    print("No es posible crear una lista sin palabras.")
else:
    lista = []
    for i in range(numero):
        print("Dime la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    inversa = []
    for i in lista:
        inversa = [i] + inversa
    print("La lista inversa es:", inversa)