# > Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:
# > 
# > - Debe permitir agregar nuevas tareas a la lista.
# > - Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
# > - Debe mostrar la lista actual de tareas pendientes.
# > - Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
# > El menú debe presentar las siguientes opciones:
# > 
# > - Agregar tarea
# > - Marcar tarea como completada
# > - Mostrar tareas
# > - Salir
tareas = []

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        tarea = input("Ingrese la nueva tarea: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada con éxito.")
    
    elif opcion == '2':
        if not tareas:
            print("No hay tareas para marcar como completadas.")
        else:
            print("Lista de tareas pendientes:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")
            indice_str = input("Ingrese el número de la tarea completada: ")
            if indice_str.isdigit():
                indice = int(indice_str) - 1
                if 0 <= indice < len(tareas):
                    tarea = tareas.pop(indice)
                    print(f"Tarea '{tarea}' marcada como completada y eliminada de la lista.")
                else:
                    print("Número de tarea inválido.")
            else:
                print("Entrada inválida, por favor ingrese un número.")
    
    elif opcion == '3':
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("Lista de tareas pendientes:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")
    
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida, por favor seleccione una opción del 1 al 4.")