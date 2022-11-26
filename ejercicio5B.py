"""
Escribe un programa que te pida una frase y una vocal (entrada por teclado), 
y pase estos datos como parámetro a una función que se encargará de cambiar 
todas las vocales de la frase por la vocal seleccionada. Devolverá la función 
la frase modificada, y el programa principal la imprimirá:
"""
def vocales(frase, vocal):
    conjunto_vocales = "AEIOUaeiou"

    for i in conjunto_vocales:
        frase = frase.replace(i, vocal)
    return frase

# Introducimos las variables e imprimimos la función
frase = str(input("Introduce una frase: "))
vocal = str(input("Introduce una vocal: "))

print(vocales(frase, vocal))

"""Versión: Sergio"""