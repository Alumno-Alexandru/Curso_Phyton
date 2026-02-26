from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv
from bson import ObjectId
from bson.errors import InvalidId
import gridfs
from gridfs.errors import NoFile
from werkzeug.utils import secure_filename
import io

load_dotenv()

app = Flask(__name__, template_folder='../html', static_folder='../css')

# Set a more secure default and check if it's being used.
default_key = 'a_truly_secret_key_that_is_long_and_random'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', default_key)
if app.config['SECRET_KEY'] == default_key:
    print("ADVERTENCIA: La SECRET_KEY no está configurada. Usando un valor predeterminado inseguro para desarrollo.")
    print("En producción, establezca una variable de entorno SECRET_KEY.")

# Conectar a MongoDB
mongo_uri = os.getenv('MONGO_URI_IN')
if not mongo_uri:
    # Fail fast if the database URI is not configured.
    raise ValueError("No se ha proporcionado la URI de MongoDB en la variable de entorno MONGO_URI_IN")

try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # The ismaster command is cheap and does not require auth. It forces a connection check.
    client.admin.command('ismaster')
    db = client['marketplace_db']
    projects_collection = db['projects']
    fs = gridfs.GridFS(db)
except ConnectionFailure as e:
    raise ConnectionFailure(f"No se pudo conectar a la base de datos MongoDB. Verifique la MONGO_URI_IN. Error: {e}")


@app.route('/')
def index():
    try:
        projects = list(projects_collection.find())
    except Exception as e:
        flash(f"Error al contactar la base de datos: {e}", "error")
        projects = []
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        precio_str = request.form.get('precio')
        categoria = request.form.get('categoria')

        if not all([titulo, descripcion, precio_str, categoria]):
            flash('Todos los campos son obligatorios.', 'error')
            return render_template('add.html', form_data=request.form), 400

        try:
            precio = float(precio_str)
        except (ValueError, TypeError):
            flash('El precio debe ser un número válido.', 'error')
            return render_template('add.html', form_data=request.form), 400

        # Manejar archivo HTML
        file = request.files.get('file')
        if not file or not file.filename:
            flash('Por favor, sube un archivo HTML.', 'error')
            return render_template('add.html', form_data=request.form), 400

        filename = secure_filename(file.filename)
        if not filename.endswith('.html'):
            flash('Solo se permite subir archivos HTML.', 'error')
            return render_template('add.html', form_data=request.form), 400

        try:
            # Validar contenido del archivo HTML
            content = file.read()  # Leer el archivo como binario
            content_str = content.decode('utf-8')
            if '<link' in content_str or ('<img src="' in content_str and not 'http' in content_str):
                flash('El archivo HTML no debe contener referencias locales a CSS o imágenes. Use URLs externas.', 'error')
                return render_template('add.html', form_data=request.form), 400

            # Guardar archivo en GridFS
            file_id = fs.put(content, filename=filename, content_type='text/html')
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", 'error')
            return render_template('add.html', form_data=request.form), 400

        project = {
            'titulo': titulo,
            'descripcion': descripcion,
            'precio': precio,
            'categoria': categoria,
            'file_id': file_id,
            'file_name': filename
        }
        projects_collection.insert_one(project)
        flash('Proyecto agregado exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')
@app.route('/ver_archivo/<filename>')
def ver_archivo(filename):
    try:
        grid_out = fs.get_last_version(filename=filename)
        return send_file(io.BytesIO(grid_out.read()), download_name=filename, mimetype=grid_out.content_type)
    except NoFile:
        flash('Archivo no encontrado.', 'error')
        return redirect(url_for('index'))

@app.route('/comprar/<id>', methods=['POST'])
def comprar(id):
    # Aquí podrías agregar lógica de compra real
    flash('¡Compra realizada con éxito!', 'success')
    return redirect(url_for('index'))

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        flash('ID de proyecto no válido.', 'error')
        return redirect(url_for('index'))

    project = projects_collection.find_one({'_id': object_id})
    if not project:
        flash('Proyecto no encontrado', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        precio_str = request.form.get('precio')
        categoria = request.form.get('categoria')

        if not all([titulo, descripcion, precio_str, categoria]):
            flash('Todos los campos son obligatorios.', 'error')
            return render_template('edit.html', project=project), 400

        try:
            precio = float(precio_str)
        except (ValueError, TypeError):
            flash('El precio debe ser un número válido.', 'error')
            return render_template('edit.html', project=project), 400

        projects_collection.update_one({'_id': object_id}, {'$set': {
            'titulo': titulo,
            'descripcion': descripcion,
            'precio': precio,
            'categoria': categoria
        }})
        flash('Proyecto actualizado', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', project=project)

@app.route('/delete/<id>')
def delete(id):
    try:
        object_id = ObjectId(id)
        result = projects_collection.delete_one({'_id': object_id})
        if result.deleted_count == 0:
            flash('Proyecto no encontrado.', 'warning')
        else:
            flash('Proyecto eliminado.', 'success')
    except InvalidId:
        flash('ID de proyecto no válido.', 'error')
    return redirect(url_for('index'))

@app.route('/upload_files', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file = request.files.get('file')

        if not file or not file.filename:
            flash('Por favor selecciona un archivo para subir.', 'error')
            return redirect(url_for('files'))

        filename = secure_filename(file.filename)
        if fs.exists({"filename": filename}):
            flash(f'El archivo "{filename}" ya existe. Por favor, elige otro nombre.', 'error')
            return redirect(url_for('files'))

        try:
            fs.put(file, filename=filename, content_type=file.content_type)
            flash('Archivo subido exitosamente.', 'success')
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", "error")

        return redirect(url_for('files'))

    return render_template('upload_files.html')

@app.route('/files')
def files():
    file_list = list(fs.find())
    return render_template('files.html', files=file_list)

@app.route('/file/<filename>')
def get_file(filename):
    try:
        grid_out = fs.get_last_version(filename=filename)
        # Use a wrapper for the file-like object to ensure it has a `name` attribute
        class FileWrapper:
            def __init__(self, file, filename):
                self.file = file
                self.name = filename
            def read(self, size=-1):
                return self.file.read(size)

        file_wrapper = FileWrapper(grid_out, grid_out.filename)
        
        return send_file(
            io.BytesIO(grid_out.read()),
            download_name=grid_out.filename,
            as_attachment=True,
            mimetype=grid_out.content_type
        )
    except NoFile:
        flash('Archivo no encontrado.', 'error')
        return redirect(url_for('files'))

@app.route('/delete_file/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        # Buscar y eliminar el archivo de GridFS
        file = fs.find_one({"filename": filename})
        if file:
            fs.delete(file._id)
            flash(f"El archivo '{filename}' ha sido eliminado exitosamente.", "success")
        else:
            flash(f"El archivo '{filename}' no fue encontrado.", "error")
    except Exception as e:
        flash(f"Error al eliminar el archivo: {e}", "error")
    return redirect(url_for('files'))

@app.route('/vista_proyecto/<project_id>', methods=['GET'])
def vista_proyecto(project_id):
    try:
        project = projects_collection.find_one({"_id": ObjectId(project_id)})
        if not project or "files" not in project:
            flash("El proyecto no tiene archivos asociados.", "error")
            return redirect(url_for('index'))

        # Buscar un archivo HTML en los archivos del proyecto
        html_file = next((file for file in project["files"] if file["filename"].endswith(".html")), None)
        if not html_file:
            flash("El proyecto no contiene un archivo HTML para mostrar.", "error")
            return redirect(url_for('index'))

        # Obtener el archivo HTML desde GridFS
        grid_out = fs.get(ObjectId(html_file["file_id"]))
        return send_file(io.BytesIO(grid_out.read()), mimetype="text/html")
    except Exception as e:
        flash(f"Error al cargar la vista del proyecto: {e}", "error")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)