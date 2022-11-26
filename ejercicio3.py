"""
Escribe un programa que lea (entrada por teclado) una frase, y la pase como 
parámetro a un procedimiento, y éste debe mostrar la frase con un carácter 
en cada línea.
"""
frase=input("Escriba cualquier frase:\n")

def desestructura(frase):
    for caracter in frase:
        print(caracter)

desestructura(frase)