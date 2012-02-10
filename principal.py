#!/usr/bin/python

import os

#Creado por:
# Nelson Mauricio Navarro Canales 
# Erick Samael Hernandez
# Edwin David Portillo Hernandez
# Danny Stanley Ascencio Pineda
# Hector Alexander Velasquez Yanes
 
print "\tMenu"
print '1 -> Factorial'
print '2 -> Numero Primo'
print '3 -> Raiz'
print '4 -> Palindromo'
print '5 -> Desarrolladores'
print '6 -> Salir'

opcion = input("Seleccione una opcion: ")

if opcion == 1:
	print "\tCalcular Factorial"
	from archivos.operaciones import factorial
	re = factorial(num = int(raw_input("Introducir Numero: ")))
	print "El factorial es ", re
	
if opcion == 2:
	print "\tCalcular Numeros Primos"
	from archivos.operaciones import numero_primo
	re = numero_primo(num = int(raw_input("Introducir Numero: ")))	
	print re
	
if opcion == 3:
	print "\tCalcular Raiz Cuadrada"
	from archivos.operaciones import raiz
	re = raiz(num = int(raw_input("Introducir Numero: ")))
	print "La raiz cuadrada es: ", re
	
if opcion == 4:
	print "\tDeterminar Palindromos"
	from archivos.operaciones import palindromo
	cadena = palindromo(string = str(raw_input("Intrucir una cadena: ")))
	print cadena
	
if opcion == 5:
	from archivos.operaciones import desarrolladores
	nombres=desarrolladores()
	
elif opcion == 6:
	print "\tAviso"
	s = str(raw_input('Seguro que quiere Salir Si o No: '))
	if s == "si":
		exit()
	elif s == "no":
		print "Continuar"
	else:
		os.system('title Error de Escritura & color C0 & echo ERROR Solo se escribe si para salir o no para volver al menu & ping -n 5 127.0.0.1>nul')
elif opcion <1 or opcion >5:
        os.system('title Error de Escritura & color C0 & echo ERROR Solo se permiten los numeros del menu es decir del 1 al 6!! & ping -n 5 127.0.0.1>nul')
        
        print 'Por favor introducir un numero valido '
