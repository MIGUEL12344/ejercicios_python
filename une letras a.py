# Solicita al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")

# Itera sobre cada letra de la palabra empezando desde el final
for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i], end="a")