'''
5. Implementa el juego de hundir la flota. El tablero consiste en un array de dos dimensiones 10x10 y 
llevará asociado un barco que ocupe 3 casillas en horizontal o vertical, seleccionadas (p. ej. A1 donde 
A es la fila y 1 es la columna) y ofrezca retroalimentación para saber si ha dado en agua, ha dado al barco 
o si después de varios intentos lo ha hundido.

El tablero tendrá:
    - guiones para las partes de agua (-)
    - 3 B's para el barco (B)
    - X's para los lanzamientos que se vayan realizando (X)

El juego tendrá un número máximo de intentos y terminará cuando se sobrepasen o bien, cuando se hunda el barco. 
Al final del juego, se imprimirá el tablero con la situación final.
'''

import random

TAMANO_TABLERO = 10
INTENTOS_MAXIMOS = 15

def crear_tablero():
    """Crea un tablero vacío de 10x10 lleno de guiones."""
    return [['-' for _ in range(TAMANO_TABLERO)] for _ in range(TAMANO_TABLERO)]


def colocar_barco(tablero):
    """Coloca un barco de 3 casillas en el tablero, horizontal o verticalmente."""
    orientacion = random.choice(['H', 'V'])
    if orientacion == 'H':  # horizontal
        fila = random.randint(0, TAMANO_TABLERO - 1)
        col = random.randint(0, TAMANO_TABLERO - 3)
        for i in range(3):
            tablero[fila][col + i] = 'B'
    else:  # vertical
        fila = random.randint(0, TAMANO_TABLERO - 3)
        col = random.randint(0, TAMANO_TABLERO - 1)
        for i in range(3):
            tablero[fila + i][col] = 'B'


def mostrar_tablero(tablero, ocultar_barco=True):
    """Muestra el tablero. Si ocultar_barco=True, no muestra las 'B'."""
    print("\n    1 2 3 4 5 6 7 8 9 10")
    print("   ----------------------")
    letras = "ABCDEFGHIJ"
    for i, fila in enumerate(tablero):
        fila_visible = []
        for celda in fila:
            if ocultar_barco and celda == 'B':
                fila_visible.append('-')
            else:
                fila_visible.append(celda)
        print(f"{letras[i]} | {' '.join(fila_visible)}")


def coordenada_a_indices(coord):
    """Convierte una coordenada como 'A1' en índices (fila, columna)."""
    letras = "ABCDEFGHIJ"
    try:
        fila = letras.index(coord[0].upper())
        col = int(coord[1:]) - 1
        if 0 <= fila < TAMANO_TABLERO and 0 <= col < TAMANO_TABLERO:
            return fila, col
    except (ValueError, IndexError):
        pass
    return None


def realizar_disparo(tablero, fila, col):
    """Gestiona un disparo y devuelve el resultado."""
    if tablero[fila][col] == 'B':
        tablero[fila][col] = 'O'
        print(" ¡Has dado en el barco!")
        return "tocado"
    elif tablero[fila][col] == '-':
        tablero[fila][col] = 'X'
        print(" Agua...")
        return "agua"
    elif tablero[fila][col] == 'X':
        print(" Ya habías disparado en esa posición.")
        return "repetido"
    return None


def barco_hundido(tablero):
    """Verifica si el barco ha sido hundido."""
    for fila in tablero:
        if 'B' in fila:
            return False
    return True


def ejecutar_juego():
    """Función principal del juego."""
    tablero = crear_tablero()
    colocar_barco(tablero)

    print(" Bienvenido al juego de Hundir la Flota ")
    print("Introduce coordenadas como A1, B5, J10, etc.")
    intentos = 0

    while intentos < INTENTOS_MAXIMOS:
        mostrar_tablero(tablero)
        coord = input(f"Intento {intentos + 1}/{INTENTOS_MAXIMOS} - Dispara a una coordenada: ").strip().upper()
        indices = coordenada_a_indices(coord)

        if not indices:
            print(" Coordenada inválida. Usa formato como A1 o D7.")
            continue

        resultado = realizar_disparo(tablero, *indices)
        if resultado in ["agua", "tocado"]:
            intentos += 1

        if barco_hundido(tablero):
            print(" ¡Felicidades! Has hundido el barco en", intentos, "intentos.")
            mostrar_tablero(tablero, ocultar_barco=False)
            break
    else:
        print(" Se acabaron los intentos. El barco sigue a flote...")
        mostrar_tablero(tablero, ocultar_barco=False)
