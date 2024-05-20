print("NUMEROS NEGATIVOS ")
num_numeros = int(input("¿Cuántos números vas a introducir? "))
negativos = 0

for i in range(num_numeros):
    numero = float(input(f"Introduce el número {i+1}: "))
    if numero < 0:
        negativos += 1
print("Has introducido", negativos, "números negativo.")