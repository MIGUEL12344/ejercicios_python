# > amos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.
# > 
# > Esta calculadora funciona de la siguiente manera:
# > 
# > - Recogemos los datos A y B
# > - Si operación es 1 calcula la raíz cuadrada de la suma de A y B
# > - Si operación es 2 calcula A / B. Vigilamos que B no sea 0..
# > - Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5

#faltaaaaaaaaaaaa
while True:
    print("\tCALCULATOR")
    dato_a=int(input("ingrese dato a-> "))
    dato_b=int(input("ingrese dato b-> "))
    print("""1. calcular la raíz cuadrada de la suma de A y B
2.calcula A / B. Vigilamos que B no sea 0..
3.calcular ( A * B ) / 2.5
4. salir""")
    opcion=int(input("ingrese opcion-> "))
    if opcion == 1:
        raiz_cuadrada=(dato_a + dato_b)**0.5
        print(f"la raiz cuadrada del resultado es {raiz_cuadrada}\n")
    if opcion == 2:
        division=dato_a/dato_b
        print(f"la division es {division}\n")
        if dato_b == 0:
            print("division entre cero no aceptable")
    if opcion == 3:
        resultado=(dato_a*dato_b)/2.5
        print(f"el resultado es {resultado}\n")
    if opcion == 4:
        print("\ngracias por su visita")
        break