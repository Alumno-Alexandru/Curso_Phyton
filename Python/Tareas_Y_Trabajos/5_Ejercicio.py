import emoji

def calcular_imc_con_emoji(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc, 2)  # Redondeamos a 2 decimales
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado

# Ejemplo de uso
peso = 70
altura = 1.75
resultado_imc, estado = calcular_imc_con_emoji(peso, altura)
print(f"Tu IMC es {resultado_imc}. Estado: {estado}")
