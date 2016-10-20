#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una
#palabra y diga cuántas veces aparece esa palabra en la lista.

#!/usr/bin/env python

numero = int(input("Dime cuantas palabras tendrá la lista: "))

if numero < 1:
    print("No es posible crear una lista sin palabras.")
else:
    lista = []
    for i in range(numero):
        print("Dime la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]

    print("La lista final es:", lista)

    buscar = input("Dígame la palabra a buscar: ")
    contador = 0

    for i in lista:
        if i == buscar:
            contador += 1;
    if contador == 0:

        print("La palabra '" + buscar + "' no esta en la lista.")
    elif contador == 1:
        print("La palabra '" + buscar + "' esta una vez en la lista.")
    else:
        print("La palabra '" + buscar + "' esta", contador, "veces en la lista.")