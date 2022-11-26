"""
Escribe un programa que pida un texto por pantalla, 
este texto lo pase como parámetro a un procedimiento, 
y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

"""
#Declaramos la variable texto con el valor del resultado del input
texto=input("Escribe un texto:\n")
#Función que transforma el texto en minusculas y en mayusculas
def transformar(texto):
    print(texto.lower())
    print(texto.upper())
#Llamamos a la función
transformar(texto)

"""Autor: Raquel Arques Toro"""


