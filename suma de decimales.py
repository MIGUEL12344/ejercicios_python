num_numeros = int(input("¿Cuántos números vas a introducir?: "))
suma = 0

for i in range(num_numeros):
    numero = float(input("Introduce el número " + str(i + 1 ) + ": "))
    suma += numero

print("La suma de los números introducidos es:", suma)