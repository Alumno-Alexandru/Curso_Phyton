import sys
'''
creamos variable para numero
Pedimos al usuario que introduzca un numero.
validar que el usuario introduzca un numero entero
imprimir el numero multiplicado por un rango de 1 a 10 y el resultado
'''
global numero 

def pintar_tabla_multiplicar(numero):
    for i in range(10):
        print(f"{numero} * {i+1} = {numero * (i+1)}")

# Imprimimos el numero multiplicado por un rango de 1 a 10
def pedir_numero():
    global numero
    while numero < 1 or numero > 10:
        try:
            numero = int(input("¿Que tabla de multiplicar quieres? (entre 1 y 10): "))
        except ValueError:
            print("Por favor, introduce un número entre 1 al 10.")
        except: 
            print("Ha ocurrido un error inesperado.")
    pintar_tabla_multiplicar(numero)

def ejecutar_con_argumento():
    if len(sys.argv)<1 and len(sys.argv)>1:
        print("Número de argumentos incorrecto.")
    else:
        pintar_tabla_multiplicar(sys.argv[1])
