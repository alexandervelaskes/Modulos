#!/usr/bin/python

import math

# Funcion para calcular el factorial de un numero determinado
def factorial(num):
	factor = math.factorial(num)
	return factor


#Funcion para calcular si un numero es primo
def numero_primo(num):
	for i in range(2, num):
    		if num % i == 0:
        		return "No es un numero primo"
        	else:
			return "Es un numero primo"

	
#Funcion para calcular la raiz cuadrada de un numero determinado
def raiz(num):
	resultado = math.sqrt(num)
	return resultado


#Funcion que determina si una cadena en un palindromo
def palindromo(string):
	cadena = string[::-1]
	if string == cadena:
		return "Es un palindromo"
	else:
		return "No es un palindromo"


def desarrolladores():
	print "\tDesarrolladores"
	print "<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>"
	print "Nelson Mauricio Navarro Canales"
	print "Erick Samael Hernandez Herrera"
	print "Edwin David Portillo Hernandez"
	print "Danny Stanley Ascencio Pineda"
	print "Hector Alexander Velasquez Yanes"
	print "<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>"

