#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una
#palabra y elimine esa palabra de la lista.

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

    eliminar = input("Palabra a eliminar: ")
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == eliminar:
            del(lista[i])
    print("La lista final es:", lista)