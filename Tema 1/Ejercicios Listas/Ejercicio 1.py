#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que
#pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
#programa tiene que escribir la lista

#!/usr/bin/env python
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("No es posible crear una lista sin palabras")
else:
    lista = []
    for i in range(numero):
        print("Dime la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista final es:", lista)