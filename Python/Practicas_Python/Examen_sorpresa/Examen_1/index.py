'''
Implementa el código que, dado un número aleatorio del 1 al 100, pregunte al usuario por un número y 
le ofrezca información acerca de si ha acertado o si el número es más bajo o más alto que el número secreto. 
El programa terminará cuando el usuario acierte el número secreto o sobrepase el número máximo de intentos.

Para obtener el número secreto aleatorio, puedes utilizar la sentencia numero_secreto = random.randint(1, 100) 
de la librería random.
'''

import random

def jugar_adivinanza(max_intentos=10):
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print(" Bienvenido al juego de adivinanza del número secreto (1 al 100).")

    while intentos < max_intentos:
        try:
            numero_usuario = int(input(f"Intento {intentos + 1}/{max_intentos} - Ingresa tu número: "))
        except ValueError:
            print(" Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if numero_usuario == numero_secreto:
            print(f" ¡Felicidades! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos.")
            return
        elif numero_usuario < numero_secreto:
            print(" El número secreto es más alto.")
        else:
            print(" El número secreto es más bajo.")

    print(f" Has alcanzado los ({intentos}) intentos permitidos. El número secreto era {numero_secreto}.")
