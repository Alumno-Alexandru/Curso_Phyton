'''
4. Implementa un programa que lea y almacene en un array una serie de temperaturas que irá introduciendo el usuario y
ofrezca un menú con la posibilidad de insertar nuevas temperaturas y calcule:

- la temperatura media
- la temperatura más alta
- la temperatura más baja

de los valores almacenados en el array. El programa parará solo mediante una opción del menú.
'''

# main.py

def mostrar_menu():
    """Muestra las opciones disponibles en el menú."""
    print("\n MENÚ DE TEMPERATURAS")
    print("1. Insertar varias Temperaturas (de uno en uno)")
    print("2. Mostrar temperatura media")
    print("3. Mostrar temperatura más alta")
    print("4. Mostrar temperatura más baja")
    print("5. Salir")


def insertar_temperatura(temperaturas):
    """Permite al usuario agregar una temperatura a la lista."""
    try:
        temp = float(input("Ingrese una temperatura: "))
        temperaturas.append(temp)
        print(f" Temperatura {temp}° añadida correctamente.")
    except ValueError:
        print(" Entrada no válida. Debe ser un número.")


def calcular_media(temperaturas):
    """Calcula y muestra la temperatura media."""
    if temperaturas:
        media = sum(temperaturas) / len(temperaturas)
        print(f"  Temperatura media: {media:.2f}°")
    else:
        print(" No hay temperaturas registradas.")


def mostrar_maxima(temperaturas):
    """Muestra la temperatura más alta."""
    if temperaturas:
        print(f" Temperatura más alta: {max(temperaturas)}°")
    else:
        print(" No hay temperaturas registradas.")


def mostrar_minima(temperaturas):
    """Muestra la temperatura más baja."""
    if temperaturas:
        print(f" Temperatura más baja: {min(temperaturas)}°")
    else:
        print(" No hay temperaturas registradas.")


def ejecutar_programa():
    """Función principal que ejecuta el menú interactivo."""
    temperaturas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            insertar_temperatura(temperaturas)
        elif opcion == '2':
            calcular_media(temperaturas)
        elif opcion == '3':
            mostrar_maxima(temperaturas)
        elif opcion == '4':
            mostrar_minima(temperaturas)
        elif opcion == '5':
            print(" Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Inténtelo nuevamente.")
