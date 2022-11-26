"""
Escribe un programa que lea (entrada por teclado) el nombre y los dos apellidos 
de una persona (en tres cadenas de caracteres diferentes), los pase como 
parámetros a una función, y ésta debe unirlos y devolver una única cadena. 
La cadena final será imprimida por el programa por pantalla.
"""
#Pedir al usuario su nombre y apellidos por separado
nombre=input("Introduzca su nombre: ")
apellido1=input("Introduzca su primer apellido: ")
apellido2=input("Introduzca el segundo apellido: ")

#Definimos la función que recoge estos valores y los une
def transforma(nombre, apellido1, apellido2):
    completo = print(f"Su nombre completo es el siguiente: {nombre} {apellido1} {apellido2}")
    return completo
#Llamamos a la función
transforma(nombre, apellido1, apellido2)

"""Autor: Raquel Arques Toro"""