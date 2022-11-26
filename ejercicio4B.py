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
    fraseNueva=""
    for i in frase:
        if i==" ":
            i="*"
        fraseNueva+=i
    return fraseNueva
#Llamamos a la función
print(asterisco(frase))

"""Autor: Un alumno"""