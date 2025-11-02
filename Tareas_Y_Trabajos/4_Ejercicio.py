# Pedir nombre directamente (asumimos que siempre es texto válido)
nombre = input("Ingrese su nombre: ")

# Pedir edad en un bucle hasta que sea un número entero válido
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break  # Salir del bucle si la conversión fue exitosa
    except ValueError:
        print(" Error: Por favor, ingrese un número entero válido para la edad.")

# Pedir altura en un bucle hasta que sea un número flotante válido
while True:
    try:
        altura = float(input("Ingrese su altura en metros: "))
        break  # Salir del bucle si la conversión fue exitosa
    except ValueError:
        print(" Error: Por favor, ingrese un número válido para la altura (usa punto decimal si es necesario).")

# Mostrar los datos ingresados
print("\n Datos ingresados correctamente:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")