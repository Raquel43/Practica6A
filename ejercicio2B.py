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

def transforma(lista):
    completo = lista[0]
    for i in range(1,len(lista)):
        completo=completo+" "+lista[i]
    return completo
lista=[]
lista.append(nombre)
lista.append(apellido1)
lista.append(apellido2)

print(transforma(lista))
#Llamamos a la función
transforma(lista)

"""Autor: Raquel Arques Toro"""