#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos
#palabras y sustituya la primera por la segunda en la lista.

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

    buscar = input("Sustituir la palabra: ")
    sustituir = input("por la palabra: ")
    for i in range(len(lista)):
        if lista[i] == buscar:
            lista[i] = sustituir
    print("La lista final es :", lista)