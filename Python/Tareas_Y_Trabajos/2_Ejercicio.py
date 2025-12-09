# Función para saludar
def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido."

# Función para calcular el IMC
def calcular_imc(peso, altura):
    if altura <= 0:
        return "Altura no válida."
    imc = peso / (altura ** 2)
    return round(imc, 2)

# --- Simulación de datos ingresados (Ejercicio 1) ---
nombre =input("Ingresa tu nombre: ")
peso = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

# --- Llamadas a las funciones ---
saludo = saludar(nombre)
imc = calcular_imc(peso, altura)

# --- Mostrar resultados ---
print(saludo)
print(f"Tu IMC es: {imc}")

