# Solicita al usuario que ingrese un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Verifica que el número sea positivo
if numero > 0:
    # Inicializa una variable vacía para almacenar los números impares
    impares =""
    # Recorre los números desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        # Si el número es impar, lo añade a la lista
        if i % 2 != 0:
            if impares:
                impares+=","
            impares+=str(i)
    # Imprime los números impares separados por comas
    print(impares,end=",")
else:
    print("El número ingresado no es positivo.")