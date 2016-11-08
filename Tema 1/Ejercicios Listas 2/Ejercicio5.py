'''
Escriba un programa que calcule términos de la sucesión Un+1 = 3 Un + 1 si Un es impar y U n+1 =
Un / 2 si Un es par. El programa tiene que pedir el término U0 y el número de términos a calcular.
Cálculo de términos de la sucesión U(n+1)=3.U(n)+1 si n es impar y U(n)=U(n)/2 si n es par.
'''

#!/usr/bin/env python

u = int (input("Valor de U(0): "))
cantidad = int (input("Terminos: "))
sucesion = []

sucesiones = u 
sucesion.append(u) 
i = 1 
x = 1 
while (i < cantidad): 
	if (sucesiones % 2 == 0 ): 
		sucesiones = int (sucesiones / 2)
		sucesion[0:x] += [str(sucesiones)]
		x += 1
	else: 
		sucesiones = int (3 * sucesiones + 1)
		sucesion[0:x] += [str(sucesiones)] 
		x += 1
	i += 1

print ("Sucesion:", sucesion)