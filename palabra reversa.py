# Solicita al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")

# Itera sobre cada letra de la palabra empezando desde el final
for letra in reversed(palabra):
    print(letra)