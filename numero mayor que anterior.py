print(" MAYORES QUE EL ANTERIOR ")
# Pregunta al usuario cuántos números va a introducir
cantidad_numeros = int(input("¿Cuántos números vas a introducir?: "))
if cantidad_numeros < 0:
    print("imposible")
    exit()    
# Inicializa una variable para almacenar el número anterior
numero_anterior = int(input("escriba un número: "))
# Itera para solicitar y verificar cada número
for i in range(cantidad_numeros - 1):
    numero_actual = int(input(f"escriba un número mas grande que {numero_anterior}: "))
    # Comprueba si el número actual es mayor que el número anterior
    if numero_actual <= numero_anterior:
        print(f"{numero_actual} no es mayor que {numero_anterior}.")
    numero_anterior = numero_actual
print(f"\n gracias por su colaboración ")