"""
En este primer programa, vamos a 
practicar la sintaxis basica de Python.

"""

"""
usar Ctrl + K seguido de Ctrl + C para comentar
usar Ctrl + K seguido de Ctrl + U para descomentar.
"""


# Esto imprime "hola mundo" en pantalla:
edad = 20
print("Hola mundo, tengo", edad, "años")
precio = 19.99
print("El precio es", precio, "dolares")
nombre = "Python"
print("Estoy aprendiendo", nombre)
activo = True
print("El curso esta activo?", activo)
ventana = None
print("La ventana es", ventana)

print(type(edad), type(precio), type(nombre), type(activo), type(ventana))

lista = [1, 2, 3, 4, 5]
print(lista[3])
print(type(lista))

tupla = (1, 2, 3, 4, 5)
print(tupla[4])
print(type(tupla))

diccionario = {
    "nombre": "Paquito", 
    "apellido": "chocolatero",
    "Usuario": "chocopaquito",
    "contraseña": "1234"
    }

print(diccionario["Usuario"])

conjunto = {1, 2, 2, 3, "hola", "adios"}

print(list(conjunto)[2])
print(conjunto)

int("10")
str(10)
float("3.14")

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
print(numero1 + numero2)

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")


estado_web = 404

match estado_web:
        case 400:
             print ("Bad request")
        case 401 | 403:
             print("Not allowed")
        case 404:
             print ("Not found")
        case _:
             print("Something's wrong with the internet")

words = ["Python", "es", "genial"]
for w in words:
    print(w)

for nombre in lista:
    print(nombre)


