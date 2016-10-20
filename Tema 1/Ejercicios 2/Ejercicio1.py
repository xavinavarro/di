#!/usr/bin/env python
def iterPower (base, exp):
	mult = base 
	while exp > 1:
		base = base * mult
		exp = exp - 1
	return base

base = int(input("Base: ")) 
exp = int(input("Exponente: "))
print (iterPower(base, exp)) 