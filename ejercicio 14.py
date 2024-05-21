#> Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. 
#Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario login correcto. Sino, llamando ala policía.
contraseña="fufifiente"
cont=3
while cont > 0 :
    password=input("ingrese contraseña-> ")
    if password == contraseña:
        print("login correcto")
        break
    else:
        cont-=1
        print(f"te quedan {cont} intentos")
        if cont == 0:
            print("llamando a la policia")