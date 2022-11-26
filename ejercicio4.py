"""
Escribe un programa que pida una frase (entrada por teclado), y le pase como 
parámetro a una función dicha frase. La función debe sustituir todos los 
espacios en blanco de una frase por un asterisco, y devolver el resultado
para que el programa principal la imprima por pantalla.
"""
#Definimos la variable frase que guarda la frase introducida por el usuario
frase = input("Escriba una frase:\n")

#Definimos la función que tiene por parámetro la frase
def asterisco(frase):
    #Definimos un bucle que recorre cada letra de la frase
    for letra in frase:
        #Si encuentra un carácter vacio lo sustituirá por un asterisco
        if letra==" ":
            letra="*"
        fraseTransfor=print(letra, end="")
    return fraseTransfor
#Llamamos a la función
asterisco(frase)

"""Autor: Raquel Arqués Toro"""