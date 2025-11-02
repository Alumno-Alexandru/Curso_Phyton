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

from index import ejecutar_traductor

def main():
    ejecutar_traductor()

if __name__ == "__main__":
    main()