def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    if edad is None:
        edad_texto = "no se especificó la edad"
    else:
        edad_texto = f"tiene {edad} años"

    if aficiones:
        aficiones_texto = ", ".join(aficiones)
        print(f"{nombre} {edad_texto} y le gusta: {aficiones_texto}")
    else:
        print(f"{nombre} {edad_texto} y no indicó aficiones.")


# 1. Nombre, edad y varias aficiones
presentar_persona("Ana", 25, "leer", "correr", "viajar")

# 2. Solo nombre y edad
presentar_persona("Luis", 30)

# 3. Solo aficiones (usando nombre por defecto y sin edad)
presentar_persona(*[], *["cine", "fotografía"])

# 4. Sin argumentos
presentar_persona()
