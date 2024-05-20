# Solicita al usuario que ingrese una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Inicializa un contador para contar el número de veces que aparece la letra
contador = 0

# Itera sobre cada caracter en la frase
for caracter in frase:
    # Comprueba si el caracter es igual a la letra ingresada por el usuario
    if caracter == letra:
        # Si es así, incrementa el contador
        contador += 1

# Muestra el resultado
print(f"La letra '{letra}' aparece {contador} veces en la frase.")