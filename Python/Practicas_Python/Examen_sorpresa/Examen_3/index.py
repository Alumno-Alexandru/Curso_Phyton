'''
3. Implementa un traductor de español a código morse. Se debe pedir una palabra o frase en español y 
traducir a código morse según la siguiente tabla. Las palabras se separarán mediante saltos de línea y 
las letras mediante un espacio en blanco.
A: .-       B: -...     C: -.-.     D: -..      E: .  
F: ..-.     G: --.      H: ....     I: ..       J: .---  
K: -.-      L: .-..     M: --       N: -.       O: ---  
P: .--.     Q: --.-     R: .-.      S: ...      T: -  
U: ..-      V: ...-     W: .--      X: -..-     Y: -.--  
Z: --..

Por ejemplo, dada la frase Hola Mundo, el programa ofrecerá a su salida:
.... --- .-.. .-  
-- ..- -. -.. ---
'''

# Diccionario con las equivalencias de letras a código Morse
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def texto_a_morse(texto: str) -> str:
    """Traduce un texto en español a código Morse."""
    texto = texto.upper()  # Convertir a mayúsculas
    palabras = texto.split()  # Separar palabras por espacios
    resultado = []

    for palabra in palabras:
        letras_morse = []
        for letra in palabra:
            if letra in MORSE_CODE:
                letras_morse.append(MORSE_CODE[letra])
        resultado.append(" ".join(letras_morse))  # Unir letras con espacios

    return "\n".join(resultado)  # Separar palabras con saltos de línea

def ejecutar_traductor():
    """Función que pide al usuario una frase y la traduce."""
    texto = input(" Escribe una palabra o frase en español: ")
    morse = texto_a_morse(texto)
    print(" Traducción a código Morse:")
    print(morse)