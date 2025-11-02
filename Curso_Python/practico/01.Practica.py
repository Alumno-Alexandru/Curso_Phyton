# Dados los catetos de un triangulo rectangulo,
# calcular su hipotenusa

import math

Primer_cateto = float(input("Introduce el cateto 1:  "))
Segundo_cateto = float(input("Introduce el cateto 2:  "))
print(math.sqrt(Primer_cateto**2 + Segundo_cateto**2))