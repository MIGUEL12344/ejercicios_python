# > Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
# > 
# > - Verificar el saldo de su cuenta.
# > - Depositar dinero en su cuenta.
# > - Retirar dinero de su cuenta.
# > - Salir del programa.
# > El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
# > 
# > - Verificar saldo
# > - Depositar dinero
# > - Retirar dinero
# > - Salir
saldo=30
while True:
    print("\tCAJERO AUTOMATICO SENSESI")
    print(f"""    USTED CUENTA CON {saldo}s/ EN SU CUENTA
1. verificar saldo
2. depositar dinero
3. retirar dinero
4. salir""")
    opcion=int(input("ingrese opcion->> "))
    if opcion == 1:
        print(f"\nusted tiene {saldo}s/ en su cuenta\n")
    if opcion == 2:
        print("cuanto dinero desea depositar")
        deposito=int(input())
        saldo+=deposito
        print(f"\nse realizo un deposito de {deposito}s/ actualmente cuenta con {saldo}s/ en su cuenta\n")
    if opcion == 3:
        print("cuanto dinero desea retirar")
        retiro=int(input())
        saldo-=retiro
        print(f"\nusted retiro {retiro}s/ su saldo actual es de {saldo}s/\n")
    if opcion == 4:
        print("\ngracias por su visita")
        break