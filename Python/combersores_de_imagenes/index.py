import aspose.words as aw
import os
from PIL import Image
from rembg import remove

# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "img", "camarero.jpg")
img_sin_fondo = os.path.join(script_dir, "img", "camarero_sinfondo.png")
output_path = os.path.join(script_dir, "img", "Output.svg")

def QuitarFondoImagen(image_path, output_path):
    """Quita el fondo de la imagen usando rembg"""
    # Abrimos la imagen y le asignamos una variable
    foto = Image.open(image_path)
    
    # Aplicamos la funcion para quitar fondo
    salida = remove(foto)
    salida.save(output_path)  # type: ignore
    
    print(f"Imagen sin fondo guardada en: {output_path}")
    return output_path

def convertir_a_svg(img_path, output_path):
    """Convierte la imagen a SVG"""
    # Crear documento e insertar la imagen
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    
    # Insertar la imagen en el documento
    shape = builder.insert_image(img_path)
    shape.get_shape_renderer().save(output_path, aw.saving.ImageSaveOptions(aw.SaveFormat.SVG))
    
    print(f"SVG guardado en: {output_path}")

# Ejecutar el proceso
if __name__ == "__main__":
    # Paso 1: Quitar fondo
    imagen_sin_fondo = QuitarFondoImagen(img_path, img_sin_fondo)
    
    # Paso 2: Convertir a SVG
    convertir_a_svg(imagen_sin_fondo, output_path)