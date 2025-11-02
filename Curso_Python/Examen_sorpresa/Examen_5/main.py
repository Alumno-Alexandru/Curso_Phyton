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

from index import ejecutar_juego

def main():
    ejecutar_juego()

if __name__ == "__main__":
    main()