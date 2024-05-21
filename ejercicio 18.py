# Escriba un programa que solicite una contraseña 
# (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
while True:
    contraseña=input("ingrese contraseña->  ")
    verif_contra=input("valide su contraseña -> ")
    if verif_contra == contraseña:
        print("guardo su contraseña exitosamente")
        break
    else:
        print("la contraseña no coincide\n")