'''
Implementa el código que, dado un número aleatorio del 1 al 100, pregunte al usuario por un número y 
le ofrezca información acerca de si ha acertado o si el número es más bajo o más alto que el número secreto. 
El programa terminará cuando el usuario acierte el número secreto o sobrepase el número máximo de intentos.

Para obtener el número secreto aleatorio, puedes utilizar la sentencia numero_secreto = random.randint(1, 100) 
de la librería random.
'''

from index import jugar_adivinanza

def main():
    jugar_adivinanza()

if __name__ == "__main__":
    main()