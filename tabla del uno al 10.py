# Muestra la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        print(f"""{i} x {j} = {i * j}""")
    print("")  # Imprime una línea en blanco para separar cada tabla