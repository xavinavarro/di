#Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de
#la primera lista los nombres de la segunda lista.

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

    numero2 = int(input("Cuantas palabras tiene la lista a eliminar: "))


    if numero2 < 1:
        print("No es posible crear una lista sin palabras.")
    else:
        eliminar = []
        for i in range(numero2):
            print("Dime la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            eliminar += [palabra]
        print("La lista de palabras a eliminar es:", eliminar)

        for i in eliminar:
            for j in range(len(lista)-1, -1, -1):
                if lista[j] == i:
                    del(lista[j])


print("La lista es ahora:", lista)