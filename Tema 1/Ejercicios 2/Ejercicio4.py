#!/usr/bin/env python


def item_order (cadena): 
	#QUANTITY OF EACH ITEM
	ensalada = cadena.count("ensalada") 
	hamburguesa = cadena.count("hamburguesa")
	agua = cadena.count("agua")
	#PRINT CHAIN 
	print("Ensalada: ", ensalada, "Hamburguesa: ", hamburguesa, "Agua: ", agua)

pedido = input("Pedido realizado: ") 

item_order(pedido)