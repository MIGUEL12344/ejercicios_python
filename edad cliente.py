print("""\t::::SALA DE JUEGOS::::""")

# Solicitar la edad del cliente
edad = int(input("Por favor, ingrese la edad del cliente: "))
#crear sentencias y una variable precio para el resultado de mi impresión final
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10
# Mostrar el precio de la entrada
print(f"El precio de la entrada es: {precio} soles")