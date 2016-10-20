#Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los
#elementos repetidos (dejando únicamente el primero de los elementos repetidos).

#!/usr/bin/env python

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("No es posible crear una lista sin palabras.")
else:
    lista = []
    for i in range(numero):
        print("Dime la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]

   print("La lista creada es:", lista)

    for i in range(len(lista)-1, -1, -1):
        if lista[i] in lista[:i]:
            del(lista[i])
    print("La lista sin repeticiones es:", lista)