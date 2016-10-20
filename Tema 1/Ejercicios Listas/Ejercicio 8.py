#Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las
#siguientes listas (en las que no debe haber repeticiones):

#!/usr/bin/env python

numero = int(input("Dime cuantas palabras tiene la primera lista: "))

if numero < 1:
    print("No es posible crear una lista sin palabras.")
else:
    primera = []
    for i in range(numero):
        print("Dime la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        primera += [palabra]
    print("La primera lista es:", primera)

    for i in range(len(primera)-1, -1, -1):
        if primera[i] in primera[:i]:
            del(primera[i])


    numero2 = int(input("Dime cuantas palabras tiene la segunda lista: "))

    if numero2 < 1:
        print("No es posible crear una lista sin palabras.")
    else:
        segunda = []
        for i in range(numero2):
            print("Dime la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            segunda += [palabra]
        print("La segunda lista es:", segunda)

        for i in range(len(segunda)-1, -1, -1):
            if segunda[i] in segunda[:i]:
                del(segunda[i])
  

        comunes = []
        for i in primera:
            if i in segunda:
                comunes += [i]
        print("Palabras que aparecen en las dos listas:", comunes)

        soloPrimera = []
        for i in primera:
            if i not in segunda:
                soloPrimera += [i]
        print("Palabras que solo aparecen en la primera lista:", soloPrimera)

        soloSegunda = []
        for i in segunda:
            if i not in primera:
                soloSegunda += [i]
        print("Palabras que solo aparecen en la segunda lista:", soloSegunda)

        todas = comunes + soloPrimera + soloSegunda
        print("Todas las palabras:", todas)