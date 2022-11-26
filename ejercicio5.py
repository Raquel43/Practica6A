"""
Escribe un programa que te pida una frase y una vocal (entrada por teclado), 
y pase estos datos como parámetro a una función que se encargará de cambiar 
todas las vocales de la frase por la vocal seleccionada. Devolverá la función 
la frase modificada, y el programa principal la imprimirá:
"""
frase=input("Escriba una frase:\n")
vocal=input("Escriba una vocal: ")

def transformar(frase, vocal):
    for letra in frase:
        letras = ["a","e","i","o","u"]
        for i in letras:
            if letra==i or letra==i.upper():
                letra=vocal
        resultado=print(letra, end="")
    return resultado

transformar(frase, vocal)

