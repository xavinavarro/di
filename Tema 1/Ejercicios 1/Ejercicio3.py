#!/usr/bin/env python
#Definir una función ​isVowel2 (char)​ que devuelve True si char es una vocal ( "a", "e", "i",
#"o", o "u"), y False en caso contrario. Se puede asumir que char es una sola letra de
#cualquier caso (es decir, 'A' y 'a' son ambos válidos).
#Esta función es similar al problema anterior - pero esta vez, utilice la palabra clave “in”. Su
#función debe tomar en una sola cadena y devolver un valor lógico..
#def isVowel2(char):
#	 '''
#	 char: a single letter of any case
# 	returns: True if char is a vowel and False otherwise.
# 	'''
	# Your code here

char = input ()
def isVowel(char):
	if char in "aeiouAEIOU":
		return True
	else: 
		return False

print (isVowel(char))