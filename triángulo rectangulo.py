# Solicita al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Itera sobre cada fila del triángulo rectángulo
for i in range(1, numero + 1):
    # Imprime '*' en cada columna de la fila actual
    for j in range(i):
        print(numero,end="")
    # Imprime una nueva línea después de imprimir una fila completa
    print()