from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="iesazarquiel")

# CARGA DE DATOS
# Leemos el CSV al iniciar la aplicación.
# 'sep=";"' es crucial porque tu archivo usa punto y coma como separador.
try:
    df = pd.read_csv("datos_alumnos.csv" , sep=";" , encoding="utf-8")
except Exception as e:
    print(f"Error al leer el CSV: {e}")
    df = pd.DataFrame() # Crea un DataFrame vacío para evitar que la app se rompa

# Función auxiliar para obtener el nombre de la columna ID (por si varía)
def get_id_column():
    # Retorna 'ID' si existe, si no, busca variantes
    if 'ID' in df.columns:
        return 'ID'
    elif 'id' in df.columns:
        return 'id'
    elif 'id_alumno' in df.columns:
        return 'id_alumno'
    else:
        return df.columns[2]  # Por defecto, la tercera columna (donde está el ID)

# --- ENDPOINTS ---

@app.get("/info-alumnos")
def info_alumnos():
    """
    Devuelve todos los datos de los alumnos del CSV.
    No recibe parámetros.
    """
    if df.empty:
        return {"error": "No se han cargado datos del fichero CSV."}
    
    # Convertir el DataFrame a una lista de diccionarios
    alumnos = df.to_dict(orient='records')
    return {
        "total_alumnos": len(alumnos),
        "alumnos": alumnos
    }

@app.get("/columnas")
def get_columnas():
    """
    Devuelve todas las columnas disponibles en el CSV (para depuración).
    """
    if df.empty:
        return {"error": "No se han cargado datos del fichero CSV."}
    
    return {"columnas": df.columns.tolist(), "total_columnas": len(df.columns)}

@app.get("/asistencia")
def get_asistencia(id_alumno: int | None = None):
    """
    Devuelve nombre, apellidos y % de asistencia.
    Parámetro obligatorio: id_alumno
    """
    # 1. Validación de parámetros vacíos
    if id_alumno is None:
        return {
            "mensaje": "Falta el parámetro obligatorio para esta consulta.",
            "parametros_requeridos": 1,
            "uso_correcto": "/asistencia?id_alumno=NUMERO_ID"
        }

    # 2. Búsqueda del alumno
    col_id = get_id_column()
    alumno = df[df[col_id] == id_alumno]

    if alumno.empty:
        return {"error": f"No se encontró ningún alumno con el ID {id_alumno}"}

    # 3. Extracción de datos (iloc[0] toma la primera fila encontrada)
    datos = alumno.iloc[0]
    
    # Buscar columnas de forma flexible (sin importar mayúsculas)
    nombre = next((datos[col] for col in df.columns if col.lower() == 'nombre'), 'Desconocido')
    apellidos = next((datos[col] for col in df.columns if col.lower() == 'apellidos'), 'Desconocido')
    asistencia = next((datos[col] for col in df.columns if col.lower() == 'asistencia'), '0%')
    
    return {
        "nombre": nombre,
        "apellidos": apellidos,
        "asistencia": str(asistencia)
    }

@app.get("/notas")
def get_notas(id_alumno: int | None = None, nota_consultada: str | None = None):
    """
    Devuelve la calificación de una categoría específica.
    Parámetros obligatorios: id_alumno, nota_consultada
    Ejemplo: /notas?id_alumno=1001&nota_consultada=Parcial1
    """
    if df.empty:
        return {"error": "No se han cargado datos del fichero CSV."}
    
    # Obtener lista de notas disponibles dinámicamente
    col_id = get_id_column()
    notas_disponibles = [
        c for c in df.columns 
        if c.lower() not in ['id', 'nombre', 'apellidos', 'asistencia']
    ]
    
    # 1. Validación de parámetros vacíos
    if id_alumno is None or nota_consultada is None:
        return {
            "error": "Faltan parámetros obligatorios",
            "parametros_requeridos": ["id_alumno (int)", "nota_consultada (str)"],
            "notas_disponibles": notas_disponibles,
            "uso_correcto": "/notas?id_alumno=1001&nota_consultada=Parcial1"
        }

    # 2. Búsqueda del alumno
    alumno = df[df[col_id] == id_alumno]

    if alumno.empty:
        return {"error": f"No se encontró ningún alumno con el ID {id_alumno}"}
    
    # 3. Búsqueda flexible de la columna de nota (sin importar mayúsculas)
    columna_nota = None
    for col in df.columns:
        if col.lower() == nota_consultada.lower():
            columna_nota = col
            break
    
    if columna_nota is None:
        return {
            "error": f"La nota '{nota_consultada}' no existe.",
            "notas_disponibles": notas_disponibles,
            "uso_correcto": "/notas?id_alumno=1001&nota_consultada=Parcial1"
        }

    # 4. Resultado final
    datos = alumno.iloc[0]
    nombre = next((datos[col] for col in df.columns if col.lower() == 'nombre'), 'Desconocido')
    apellidos = next((datos[col] for col in df.columns if col.lower() == 'apellidos'), 'Desconocido')
    nota_valor = datos[columna_nota]
    
    return {
        "id": id_alumno,
        "nombre": nombre,
        "apellidos": apellidos,
        "nota": float(nota_valor) if nota_valor else None
    }