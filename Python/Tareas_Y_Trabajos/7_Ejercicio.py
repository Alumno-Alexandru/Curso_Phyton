entrada = input("Introduce una lista de números separados por coma (ej. 4,5,6,7): ")

# Convertimos la cadena en una lista de enteros
numeros = [int(num.strip()) for num in entrada.split(",")]

# Calculamos los valores
suma = sum(numeros)
promedio = suma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

# Mostramos los resultados con f-strings
print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")
