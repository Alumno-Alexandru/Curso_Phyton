# Pedir datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

# Mostrar mensaje usando f-string
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostrar tipo de dato de cada variable
print(f"Tipo de dato de nombre: {type(nombre)}")
print(f"Tipo de dato de edad: {type(edad)}")
print(f"Tipo de dato de altura: {type(altura)}")