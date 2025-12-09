import sys

def main():
    print("Argumentos recibidos:", sys.argv)

    if len(sys.argv) >= 4:
        nombre = sys.argv[1]
        edad = sys.argv[2]
        ciudad = sys.argv[3]
        print(f"Hola, {nombre} 👋 Tienes {edad} años y vives en {ciudad}.")
    elif len(sys.argv) > 1:
        print("Faltan argumentos. Se esperaban: nombre, edad y ciudad.")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()
