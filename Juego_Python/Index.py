import random
import emoji

# Diccionario de colores disponibles
COLORES = {
    "rojo": emoji.emojize(":red_circle:"),
    "azul": emoji.emojize(":blue_circle:"),
    "verde": emoji.emojize(":green_circle:"),
    "amarillo": emoji.emojize(":yellow_circle:"),
    "morado": emoji.emojize(":purple_circle:"),
    "naranja": emoji.emojize(":orange_circle:")
}

def generar_codigo(longitud=4):
    """Genera un código secreto aleatorio con colores"""
    return random.choices(list(COLORES.keys()), k=longitud)

def evaluar_intento(codigo, intento):
    """Genera feedback por cada posición del intento usando emoji"""
    feedback = [emoji.emojize(":minus:")] * len(codigo)  # por defecto ➖
    codigo_temp = codigo.copy()
    intento_temp = intento.copy()

    # Marcar aciertos exactos (circulo negro)
    for i in range(len(codigo)):
        if intento[i] == codigo[i]:
            feedback[i] = emoji.emojize(":black_circle:")
            codigo_temp[i] = None
            intento_temp[i] = None

    # Marcar aciertos de color mal ubicado (circulo blanco)
    for i in range(len(intento)):
        if intento_temp[i] and intento_temp[i] in codigo_temp:
            feedback[i] = emoji.emojize(":white_circle:")
            codigo_temp[codigo_temp.index(intento_temp[i])] = None

    return feedback

def jugar_mastermind():
    print("***Bienvenido a Mastermind con Colores***")
    print("Colores disponibles: " + ", ".join(COLORES.keys()))
    print("Ejemplo de entrada: rojo azul verde amarillo")
    print("Tienes 10 intentos.\n")

    codigo = generar_codigo()
    intentos = 10

    for intento_num in range(1, intentos + 1):
        while True:
            entrada = input(f"Intento {intento_num}/{intentos}: ").lower().split()
            if len(entrada) == 4 and all(c in COLORES for c in entrada):
                intento = entrada
                break
            print(" Entrada inválida. Debes escribir 4 colores válidos separados por espacio.")

        feedback = evaluar_intento(codigo, intento)

        # Mostrar intento con emojis de colores
        print(" ".join(COLORES[c] for c in intento))
        # Mostrar feedback debajo
        print(" ".join(feedback))

        if all(f == emoji.emojize(":black_circle:") for f in feedback):
            print(f" ¡Felicidades! Has adivinado el código en {intento_num} intentos.")
            return

    # Mostrar el código secreto con colores
    print(" Has perdido. El código era: " + " ".join(COLORES[c] for c in codigo))

# Ejecutar
if __name__ == "__main__":
    jugar_mastermind()
