import os
from PIL import Image
from rembg import remove

# Definimos variables - rutas relativas al script
script_dir = os.path.dirname(os.path.abspath(__file__))
path_in = os.path.join(script_dir, "./img/camarero.jpg")
path_out = os.path.join(script_dir, "camarero_sinfondo2.png")

#Abrimos la imagen y le asignamos una variable
foto = Image.open(path_in)

#Aplicamos la funcion para quitar fondo
salida = remove(foto)
salida.save(path_out) # type: ignore


