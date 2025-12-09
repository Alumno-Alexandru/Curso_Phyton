'''
Implementa una calculadora con las operaciones de suma(+), resta(-), multiplicación(*) y division(/).
El programa ofrecera un menu con las operaciones disponibles y pedira al usuario que introduzca
una opcion. A continuacion, pedira dos numeros y efectuara la operacion requerida.
'''

from index import Calculadora

def mostrar_menu():
    """Muestra el menú de opciones de la calculadora"""
    print("***CALCULADORA***")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")

def obtener_numeros():
    """Solicita dos números al usuario"""
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        return num1, num2
    except ValueError:
        print(" ERROR: Debe ingresar números válidos")
        return None, None

def main():
    """Función principal del programa"""
    calc = Calculadora()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print(" Opción inválida. Por favor, ingrese un número del 1 al 5.")
            continue
        
        if opcion == 5:
            print("\n¡Gracias por usar la calculadora! Hasta pronto.")
            break
        
        if opcion < 1 or opcion > 5:
            print(" Opción inválida. Por favor, seleccione una opción del 1 al 5.")
            continue
        
        # Obtener números
        num1, num2 = obtener_numeros()
        
        if num1 is None or num2 is None:
            continue
        
        # Realizar operación según la opción seleccionada
        try:
            if opcion == 1:
                resultado = calc.suma(num1, num2)
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            
            elif opcion == 2:
                resultado = calc.resta(num1, num2)
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            
            elif opcion == 3:
                resultado = calc.multiplicacion(num1, num2)
                print(f"\nResultado: {num1} * {num2} = {resultado}")
            
            elif opcion == 4:
                resultado = calc.division(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {resultado}")
        
        except ZeroDivisionError as e:
            print(f" ERROR: {e}")
        except Exception as e:
            print(f" ERROR inesperado: {e}")

if __name__ == "__main__":
    main()